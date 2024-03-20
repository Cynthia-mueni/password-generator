import random
letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['~','#','$','%','*','+']

print("Welcome to Cynthia's password generator")

nl= int(input('How many letters do you want?'))

nn = int(input("How many numbers do you want?"))

ns= int(input("How many symbols do you want"))


#Easy level

password=""

for char in range (1,nl+ 1):
    pas= random.choice(letters)
    password +=pas