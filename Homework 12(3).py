import csv
headers = ['Organization Id', 'Name', 'Website','Industry', 'Number of employees']
new_list = []

with open("organizations-100.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter=',')

    for row in csv_dict_reader:
        if row['Website'].startswith('https://'):
            info = {
            'Organization Id': row['Organization Id'],
            'Name': row['Name'],
            'Website': row['Website'],
            'Industry': row['Industry'],
            'Number of employees': int(row['Number of employees'])
        }
        new_list.append(info)

with open("ssl_companies.csv", 'w', newline='') as sorted_csvfile:
    writer = csv.DictWriter(sorted_csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_list)
