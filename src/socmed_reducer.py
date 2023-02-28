import csv
import sys

def socmed_reducer():
    # headers
    header = ['social_media', 'date', 'count']

    # CSV writer
    csvW = csv.writer(sys.stdout)

    # Write the headers as the first row of the output CSV file
    csvW.writerow(header)

    # Process the input 
    # Also write the output into CSV file
    for line in sys.stdin:
        # Split the line into socmed, date, count (key value pairs)
        socmed, date, count = line.strip().split('\t')
        # Write the key-value pair to CSV
        csvW.writerow([socmed, date, count])
