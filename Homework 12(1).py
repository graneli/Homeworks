import csv
headers = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
new_list = []

with open("titanic.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)

    for row in csv_dict_reader:
        if row['Survived'] == '1':
            survivor_info = {
                'PassengerId': row['PassengerId'],
                'Survived': row['Survived'],
                'Pclass': row['Pclass'],
                'Name': row['Name'],
                'Sex': row['Sex'],
                'Age': row['Age'],
                'SibSp': row['SibSp'],
                'Parch': row['Parch'],
                'Ticket': row['Ticket'],
                'Fare': row['Fare'],
                'Cabin': row['Cabin'],
                'Embarked': row['Embarked']
            }
            new_list.append(survivor_info)

with open("survived.csv", 'w', newline='') as newfile:
    csv_writer = csv.DictWriter(newfile, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(new_list)

