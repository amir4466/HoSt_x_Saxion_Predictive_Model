import csv
from datetime import datetime

CSV_FILE = 'Data/Netherlands_Op_Hours.csv' # Change to your CSV file path
THRESHOLD = 1.77  # Change to your desired threshold value

def read_entries_by_year(filename):
    entries_by_year = {}
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
                year = date.year
                
                # Only include years from 2015 to 2025
                if 2015 <= year <= 2025:
                    if year not in entries_by_year:
                        entries_by_year[year] = []
                    entries_by_year[year].append(value)
            except ValueError:
                # Skip rows with invalid data
                continue
    return entries_by_year

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

def analyze_years(start_year=2015, end_year=2025, csv_file='Netherlands.csv', threshold=THRESHOLD):
    """
    Analyze the data for a range of years and return the results.
    
    Args:
        start_year: First year to analyze
        end_year: Last year to analyze
        csv_file: Path to CSV file
        threshold: Price threshold
        
    Returns:
        Dictionary with years as keys and hours under threshold as values
    """
    entries_by_year = read_entries_by_year(csv_file)
    results = {}
    
    for year in sorted(entries_by_year.keys()):
        if start_year <= year <= end_year:
            entries = entries_by_year[year]
            result = count_consecutive_under_threshold(entries, threshold)
            results[year] = result
    
    return results

if __name__ == '__main__':
    results = analyze_years()
    
    print(f"Analysis of hours with at least 2 consecutive values under {THRESHOLD} EUR/MWhe:")
    print("=" * 60)
    
    for year, hours in results.items():
        print(f"Year {year}: {hours} hours")
    
    # Calculate total across all years
    total_hours = sum(results.values())
    print("=" * 60)
    print(f"Total hours (2015-2025): {total_hours}")