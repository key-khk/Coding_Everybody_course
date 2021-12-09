persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]

print(persons[0][0])

print('----------------------------')

for person in persons:
   print(person[0]+','+person[1]+','+person[2])

print('----------------------------')
person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)

print('----------------------------')
name, address, interest = ['egoing', 'Seoul', 'Web']
print(name, address, interest)

print('----------------------------')
persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]
for name, address, interest in persons:
    print(name+','+address+','+interest)