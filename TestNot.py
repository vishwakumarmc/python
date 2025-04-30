students =  ['Vishwa', 'Sachin', 'Sandeep', 'Pradeep']

for student in students:
    if student == 'Sachin':
        continue
    print(student)

if 'Vasantha' not in students:
    print('Not available in list')