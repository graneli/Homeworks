import csv
headers = ['Index', 'Organization Id', 'Name', 'Website', 'Country', 'Description', 'Founded', 'Industry', 'Number of employees']
new_list = []

with open("organizations-100.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter=',')

    for row in csv_dict_reader:
        info = {
            'Index': row['Index'],
            'Organization Id': row['Organization Id'],
            'Name': row['Name'],
            'Website': row['Website'],
            'Country': row['Country'],
            'Description': row['Description'],
            'Founded': row['Founded'],
            'Industry': row['Industry'],
            'Number of employees': int(row['Number of employees'])
        }
        new_list.append(info)

new_list.sort(key=lambda x: x['Number of employees'])

with open("sorted_csv.csv", 'w', newline='') as sorted_csvfile:
    writer = csv.DictWriter(sorted_csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_list)
