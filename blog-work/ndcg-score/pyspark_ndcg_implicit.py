import findspark
findspark.init()

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.mllib.evaluation import RankingMetrics
from pyspark.sql.functions import col

import os
import gc
import psutil

# freeing up & checking up memory before execution
def free_memory():
    gc.collect()  # Garbage collection
    process = psutil.Process(os.getpid())
    print(f"Memory usage before execution: {process.memory_info().rss / (1024 * 1024)} MB")

free_memory()

spark = SparkSession.builder.master("local[*]").appName("PySpark_NDCG_implicit").getOrCreate()

#  LastFM dataset
file_path = f"{os.getcwd()}/lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv"
raw_data = pd.read_table(file_path)

# basic cleaning
raw_data = raw_data.drop(raw_data.columns[1], axis=1)
raw_data.columns = ["user", "artist", "plays"]
raw_data = raw_data.dropna().copy()

# fixing categorical IDs
raw_data["user"] = raw_data["user"].astype("category")
raw_data["artist"] = raw_data["artist"].astype("category")
raw_data["user_id"] = raw_data["user"].cat.codes
raw_data["artist_id"] = raw_data["artist"].cat.codes

# fixed number of users
selected_users = raw_data["user_id"].unique()[:10000]  # fixed user set
sampled_data_A = raw_data[raw_data["user_id"].isin(selected_users)]  # All products

# picking only highly played products for comparison
top_played_artists = raw_data.groupby("artist_id")["plays"].sum().sort_values(ascending=False).index[:5000]

# filtered products
sampled_data_B = sampled_data_A[sampled_data_A["artist_id"].isin(top_played_artists)]  

# PySpark df comparison
als_df_A = spark.createDataFrame(sampled_data_A[["user_id", "artist_id", "plays"]])
als_df_B = spark.createDataFrame(sampled_data_B[["user_id", "artist_id", "plays"]])

# columns for ALS
def prepare_als_df(df):
    return df.withColumnRenamed("user_id", "user") \
             .withColumnRenamed("artist_id", "item") \
             .withColumnRenamed("plays", "rating") \
             .withColumn("user", col("user").cast("integer")) \
             .withColumn("item", col("item").cast("integer")) \
             .withColumn("rating", col("rating").cast("float"))

als_df_A = prepare_als_df(als_df_A)
als_df_B = prepare_als_df(als_df_B)

# Train ALS models
als = ALS(rank=10, 
          seed=123, 
          maxIter=5, 
          regParam=0.1, 
          userCol="user", 
          itemCol="item", 
          ratingCol="rating", 
          coldStartStrategy="drop")

model_A = als.fit(als_df_A)
model_B = als.fit(als_df_B)

# recommendations
predictions_A = model_A.recommendForAllUsers(10)
predictions_B = model_B.recommendForAllUsers(10)

# data for RankingMetrics
def extract_recommendations(row):
    return (row["user"], [rec["item"] for rec in row["recommendations"]])

pred_rdd_A = predictions_A.rdd.map(extract_recommendations)
pred_rdd_B = predictions_B.rdd.map(extract_recommendations)

true_rdd_A = (als_df_A
              .groupBy("user")
              .agg({"item": "collect_list"})
              .rdd.map(lambda x: (x["user"], x["collect_list(item)"])))

true_rdd_B = (als_df_B
              .groupBy("user")
              .agg({"item": "collect_list"})
              .rdd.map(lambda x: (x["user"], x["collect_list(item)"])))

# predictions with ground truth
joined_A = pred_rdd_A.join(true_rdd_A).map(lambda x: (x[1][0], x[1][1]))
joined_B = pred_rdd_B.join(true_rdd_B).map(lambda x: (x[1][0], x[1][1]))

# NDCG Scores
metrics_A = RankingMetrics(joined_A)
metrics_B = RankingMetrics(joined_B)

ndcg_A = metrics_A.ndcgAt(10)
ndcg_B = metrics_B.ndcgAt(10)

# results
print(f"NDCG@10 - All Products: {ndcg_A:.4f}")
print(f"NDCG@10 - Top Played Products Only: {ndcg_B:.4f}")

# Stop Spark Session
spark.stop()

# The NDCG score is not as good as expected.
# Script complete   