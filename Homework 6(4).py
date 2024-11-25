departments_dict = {
    'HR': [
        {'firstName': 'Natia', 'lastName': 'Kvirkvelia', 'age':34, 'salary':100},
        {'firstName': 'Natia', 'lastName': 'Kvirkvelia', 'age':34, 'salary':70}
    ],
    'Marketing':[
        {'firstName': 'Khatia', 'lastName': 'Kvirkvelia', 'age':30, 'salary':50},
        {'firstName': 'Khatia', 'lastName': 'Kvirkvelia', 'age':30, 'salary':10}
    ],
    'Risks':[
        {'firstName': 'Tatia', 'lastName': 'Kvirkvelia', 'age':28, 'salary':20},
        {'firstName': 'Tatia', 'lastName': 'Kvirkvelia', 'age':28, 'salary':80}
    ]
}

for department, employees in departments_dict.items():

    total_salary = sum(employee["salary"] for employee in employees)
    avg_salary = total_salary / len(employees)

    print(f"Average salary in {department}: {avg_salary}")