
"""
Project: Data ETL (Extract, Transform, Load)

Description: This project automates the process of extracting data from one data source,
transforming it, and loading it into another destination, such as a database or a CSV file.
It allows you to perform data manipulation and integration tasks efficiently.

For this example, let's consider extracting data from a CSV file,
transforming it by capitalizing the names, and loading it into another CSV file.

Input CSV File: input_data.csv
id,name,age
1,john,25
2,mary,30
3,alex,28

Output CSV File: output_data.csv
id,name,age
1,JOHN,25
2,MARY,30
3,ALEX,28
 """
import csv

def etl_process(input_file, output_file):
    with open(input_file, 'r') as csv_in:
        with open(output_file, 'w', newline='') as csv_out:
            reader = csv.DictReader(csv_in)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                row['name'] = row['name'].upper()
                writer.writerow(row)

if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"

    etl_process(input_file, output_file)
    print("ETL process completed.")