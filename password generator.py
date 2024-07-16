import random#importing random library to give random symbols,letters,digits

import string#importing string library to make the password data as string 

length=int(input('Enter the required length of the password:'));#length of the password


words = string.ascii_letters#creating ascii_letters  
numbers = string.digits#creating digits
symbols = string.punctuation#creating punctuation(symbols)

random_password= words + numbers + symbols

#creating a list of random choices of words,numbers and symbols
password = [
    random.choice(words),
    random.choice(numbers),
    random.choice(symbols)
]

#assigning the overall password combined with required details and required length
password += random.choices(random_password,k=length-3)# length-3 represents the remaining random choices to be added as 3 choices already been made

random.shuffle(password)#suffling the pasword randomly everytime the code runs
    
print("Generated password:", ''.join(password))
