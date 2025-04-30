# PythonHacks

This is a practice repository where I run code and push it for quick revision later. It contains code from the book "Data Science from Scratch" by Joel Grus.

The scripts and notebooks are very useful when working on formal projects or competitions.

## About DSS
### Chapters Progress

| Chapter | Status                | Notebook Link                                  |
|---------|-----------------------|------------------------------------------------|
| 1       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook1.ipynb) |
| 2       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook2.ipynb) |
| 3       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook3.ipynb) |
| 4       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook4.ipynb) |
| 5       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook5.ipynb) |
| 6       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook6.ipynb) |
| 7       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook7.ipynb) |
| 8       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook8.ipynb) |
| 9       | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/PythonHacks/master?filepath=path/to/Notebook9.ipynb) |
| 11      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_10_working_data.ipynb) |
| 10      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_11_ml.ipynb) |
| 12      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_12_knn.ipynb) |
| 13      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_13_naive_bayes.ipynb) |
| 14      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_14_simple_linear_regres.ipynb)|
| 15      | Done                  | [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/nikhilsingh13/PythonHacks/blob/main/notebooks/DSS_15_multiple_regression.ipynb)|
| 16      | **Currently Reading** |                                                |
| 17      | Pending               |                                                |
| 18      | Pending               |                                                |
| 19      | Pending               |                                                |
| 20      | Pending               |                                                |
| 21      | Pending               |                                                |
| 22      | Pending               |                                                |
| 23      | Pending               |                                                |
| 24      | Pending               |                                                |
| 25      | Pending               |                                                |
| 26      | Pending               |                                                |
| 27      | Pending               |                                                |

#### Chapter 9
Commands used in Chapter 9:

```bash
# This command counts the number of lines containing digits
cat DSS/random-text.txt | python DSS/egrep.py "[0-9]" | python DSS/line_count.py
# expected answer: 2

# This command finds the most common words. If no number is passed, default to 5 words.
cat DSS/random-text.txt | python DSS/most_common_words.py
cat DSS/random-text.txt | python DSS/most_common_words.py 10
```
