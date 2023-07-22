import random

print ('Welcome To Your Password Generator')

chars = 'abcdefghijklmonopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

number = input ('Amount of passwords to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are you passwords:')

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
        print(passwords)

input("Press ENTER to exit")