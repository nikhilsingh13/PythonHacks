import time
import numpy as np
from surprise import Dataset, SVD, SVDpp, NMF, KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline, SlopeOne, CoClustering
from surprise.model_selection import train_test_split
from sklearn.metrics import ndcg_score

# dataset with a fixed random state
# default from surpriselib
data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# ground truth dictionary: {uid: {iid: rating}}
test_gt = {}
for uid, iid, rating in testset:
    test_gt.setdefault(uid, {})[iid] = rating

# trainset items for prediction
all_items = sorted([trainset.to_raw_iid(i) for i in trainset.all_items()])
item_to_idx = {iid: idx for idx, iid in enumerate(all_items)}
n_items = len(all_items)

# algos (all are imported from surpriselib)
algos = {
    'SVD': SVD(),
    'SVD++': SVDpp(),
    'NMF': NMF(),
    'KNNBasic': KNNBasic(),
    'KNNWithMeans': KNNWithMeans(),
    'KNNWithZScore': KNNWithZScore(),
    'KNNBaseline': KNNBaseline(),
    'SlopeOne': SlopeOne(),
    'CoClustering': CoClustering()
}

results = {}
users = list(test_gt.keys())

for name, algo in algos.items():
    start_time = time.time()
    algo.fit(trainset)
    y_true = []
    y_score = []
    for uid in users:
        true_ratings = np.zeros(n_items)
        preds = np.zeros(n_items)
        # ground truth ratings for that user uid
        for iid, rating in test_gt[uid].items():
            if iid in item_to_idx:
                true_ratings[item_to_idx[iid]] = rating
        # predicting score for each known item
        for iid, idx in item_to_idx.items():
            preds[idx] = algo.predict(uid, iid).est
        y_true.append(true_ratings)
        y_score.append(preds)
    y_true_arr = np.array(y_true)
    y_score_arr = np.array(y_score)

    # here, the ndcg_score function is from sklearn
    ndcg = ndcg_score(y_true_arr, y_score_arr, k=10)
    
    # calculating the different algo runtime
    runtime = time.time() - start_time

    results[name] = {'ndcg': ndcg, 'runtime': runtime}
    print(f"{name}: NDCG@10 = {ndcg:.4f}, Runtime = {runtime:.2f} seconds")

# if no change were made to the code, SVD++ should be the best algo.
# script complete