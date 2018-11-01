import pandas as pd
import argparse
from csvsort import csvsort

def main():
    parser = argparse.ArgumentParser(
        description='Merge two large csv files and sort them.')
    parser.add_argument('files', metavar='file', type=str, nargs='+',
                        help='a file to be concatenated with other files and then sorted')
    parser.add_argument('-o', '--output-file', dest='output_file', type=str, default='out.csv',
                        help='output file that is all files concatenated and sorted (default: out.csv)')

    args = parser.parse_args()
    files = args.files
    out = args.output_file

    with open(files[0], 'r') as first, open(out, 'w') as new:
        new.write(next(first))

    chunksize = 10 ** 6
    for csv_file in files:
        for chunk in pd.read_csv(csv_file, chunksize=chunksize, header=0):
            chunk.to_csv(out, header=False, mode='a')
    csvsort(out, [4])
    


    print(files)


if __name__ == '__main__':
    main()
