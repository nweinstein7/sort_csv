# Sort CSV

Take in a list of .csv files, merge them together, and sort them by the 4th column which is a datetime string.

## Running

To run:

1. Install dependencies (once):

```pip install -r requirements.txt```

2. Run:

```
python sort_csv.py ./full/path/to/file1 ./full/path/to/file2
```

## Run unit tests

`python -m unittest test_sort_csv`