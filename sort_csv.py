import pandas as pd
import argparse
import csv

SORT_COLUMN = 'TRAN_EVNT_DATETIME'

def combine_and_sort(file1, file2, out):
    '''
    Combine the two csvs and sort them

    Args:
        file1: the full path to the first file
        file2: the full path to the second file
        out: the path to the output file
    '''
    first = pd.read_csv(file1, header=0, quotechar='"', sep=',', quoting=csv.QUOTE_ALL, engine='python')
    second = pd.read_csv(file2, header=0, quotechar='"', sep=',', quoting=csv.QUOTE_ALL, engine='python')
    combined = first.append(second, ignore_index=True)
    combined[SORT_COLUMN] = pd.to_datetime(combined[SORT_COLUMN])
    combined = combined.sort_values(by=[SORT_COLUMN])
    combined.to_csv(out, index=False, quoting=csv.QUOTE_ALL)

def main():
    parser = argparse.ArgumentParser(
        description='Merge two large csv files and sort them.')
    parser.add_argument('files', metavar='file', type=str, nargs=2,
                        help='a file to be concatenated with other files and then sorted')
    parser.add_argument('-o', '--output-file', dest='output_file', type=str, default='out.csv',
                        help='output file that is all files concatenated and sorted (default: out.csv)')

    args = parser.parse_args()
    files = args.files
    out = args.output_file
    combine_and_sort(files[0], files[1], out)


if __name__ == '__main__':
    main()
