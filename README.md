# PythonHacks

This is a practice repository where I run code and push it for quick revision later. It contains code from the book "Data Science from Scratch" by Joel Grus.

The scripts and notebooks are very useful when working on formal projects or competitions.

## About DSS
### Chapters Progress

| Chapter | Status                |
|---------|-----------------------|
| 1       | Done                  |
| 2       | Done                  |
| 3       | Done                  |
| 4       | Done                  |
| 5       | Done                  |
| 6       | Done                  |
| 7       | Done                  |
| 8       | Done                  |
| 9       | Done                  |
| 10      | Done                  |
| 11      | **Currently Reading** |
| 12      | Pending               |
| 13      | Pending               |
| 14      | Pending               |
| 15      | Pending               |
| 16      | Pending               |
| 17      | Pending               |
| 18      | Pending               |
| 19      | Pending               |
| 20      | Pending               |
| 21      | Pending               |
| 22      | Pending               |
| 23      | Pending               |
| 24      | Pending               |
| 25      | Pending               |
| 26      | Pending               |
| 27      | Pending               |

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
