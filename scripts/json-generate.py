import sys
import csv
import json

schools = {}

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_first_row = True

    for row in csv_reader:
        if is_first_row:
            is_first_row = False
            continue

        key = row[4] + ' (' + row[3] + ')'
        school_name = row[1] + ' (' + row[5] + ')'

        if key not in schools:
            schools[key] = []

        schools[key].append(school_name)

json_data = app_json = json.dumps(schools)
print(json_data)
