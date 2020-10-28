import sys
import csv
import json

postal_codes = {}

with open('cp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    is_first_row = True

    for row in csv_reader:
        if is_first_row:
            is_first_row = False
            continue
        key = row[0]
        value = row[1]

        postal_codes[key] = value

schools = {}

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_first_row = True

    for row in csv_reader:
        if is_first_row:
            is_first_row = False
            continue

        postal_code = row[8]
        locality = row[4]
        province = row[3]
        school_name = row[1] + ' (' + row[5] + ')'

        if postal_code in postal_codes and locality != postal_codes[postal_code]:
            key = locality + ' / ' + postal_codes[postal_code] + ' (' + province + ')'
        else:
            key = locality + ' (' + province + ')'

        if key not in schools:
            schools[key] = []

        schools[key].append(school_name)

json_data = app_json = json.dumps(schools)
print(json_data)
