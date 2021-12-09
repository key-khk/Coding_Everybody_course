input_id = input('ID:')
id = 'egoing'
input_password = input('PW:')
pw = '111'
if input_id == id:
    if input_password == pw:
        print('welcome')
    else:
        print('Worg password')
else:
    print('Worg id')