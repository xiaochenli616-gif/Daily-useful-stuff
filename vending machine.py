menu = {'pizza': 2.00,
        'nachos': 4.50,
        'popcorn':6.00,
        'oreo': 6.00,
        'cookie': 3.5}

cart=[]
total=0

print('Welcome to our vending machine')
print('-------- MENU ----------')
for key,value in menu.items():
    print(f'{key:10}: ${value:.2f}')
print('------------------------')

while True:
    user = input('Select an item(Exit to quit):')
    if user == 'Exit':
        break
    else:
        if user in menu:
            cart.append(user)
            total = total + menu.get(user)
        else:
            print('Items not found!')

print('-----Your Order Summary-----')
for user in cart:
    print(user)
print(f'Total:${total}')
print('----------------------------')

user2 = input('Would you want receipt?')