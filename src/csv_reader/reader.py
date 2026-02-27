import csv
import sys

def read_csv(file_path):
    rows = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows

def main():
    if len(sys.argv) < 2:
        print("Usage: csv-reader <csv-file>")
        sys.exit(1)
    file_path = sys.argv[1]
    rows = read_csv(file_path)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
