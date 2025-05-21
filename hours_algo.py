import csv
from datetime import datetime

CSV_FILE = 'Netherlands.csv'  # Change to your CSV file path
THRESHOLD = 20

def read_2024_entries(filename):
    entries = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Assumes there is a 'date' column in YYYY-MM-DD HH:MM:SS format and a 'value' column
            date_str = row['Datetime (UTC)']
            price_str = row['Price (EUR/MWhe)']
            
            # Skip rows with empty price values
            if not price_str:
                continue
                
            try:
                value = float(price_str)
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                if date.year == 2024:
                    entries.append(value)
            except ValueError:
                # Skip rows with invalid data
                continue
    return entries

def count_consecutive_under_threshold(entries, threshold):
    count = 0
    i = 0
    while i < len(entries) - 1:
        if entries[i] < threshold and entries[i+1] < threshold:
            count += 2
            i += 2
            # Continue counting if more than 2 in a row
            while i < len(entries) and entries[i] < threshold:
                count += 1
                i += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    entries = read_2024_entries(CSV_FILE)
    result = count_consecutive_under_threshold(entries, THRESHOLD)
    print(f"Number of entries in 2024 with at least 2 consecutive values under {THRESHOLD}: {result}")