import random
letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['~','#','$','%','*','+']

print("Welcome to Cynthia's password generator")

d= int(input('How many letters do you want?'))

a = int(input("How many numbers do you want?"))

s= int(input("How many symbols do you want?"))


#Easy level

password_list=[]

for char in range (0,d):
    pas= random.choice(letters)
    password_list +=pas

for num in range(0,a):
    pas=random.choice(numbers)
    password_list +=pas

for sym in range(0,s):
    pas= random.choice(symbols)
    password_list +=pas
    
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char
    print(password)

