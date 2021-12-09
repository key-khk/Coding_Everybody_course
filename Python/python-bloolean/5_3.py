person = {'name':'egoing', 'address':'Seoul', 'intrest':'web'}
print(person['name'])
print('----------------------------')
for key in person:
    print(key, person[key])
print('----------------------------')

persons = [
    {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
    {'name':'basta', 'address':'Seoul', 'interest':'IOT'},
    {'name':'blackdew', 'address':'Tongyeong', 'interest':'ML'}
]
print('==== persons ====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('=================')


