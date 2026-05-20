import time
print('Welcomne to the Linge Alarm!')

try:
    user_question = int(input('Please enter your alarm time in seconds:'))
    for x in range(user_question, 0, -1):
        hours = x // 60
        minutes = (x % 60) // 60
        seconds = (x % 60)
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)
    print('Time is up!')
except ValueError:
    print('Please enter only in seconds')
    exit()


