'''
import random

a = random.randint(0, 10)
b = random.randint(0, 10)
sum = a + b
print(f"{a}+{b}=...?")
sum1 = int(input())
if sum1 == sum:
    print("Great!")
else:
    print("Try again")
    sum2 = int(input())
    if sum2 == sum:
        print("Great!!")
    else:
        print("Try again")
        sum3 = int(input())
        if sum3 == sum:
            print("Great!!")
        else:
            print("Loser!!!!!")

'''

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
