#This class helps to add multiple pieces of information to the dictionary
class Password:
    def __init__(self, password, strength):
        self.__password = password
        self.__strength = strength
    def setPass(self, password):
        self.__password = password
    def setStr(self, strength):
        self.__strength = strength
    def getPass(self):
        return self.__password
    def getStr(self):
        return self.__strength
    def __str__(self):
        return 'Password: ' + self.__password + \
               '\nPassword Strength: ' + self.__strength

import pickle#to encrypt and decrypt dictionary
import random #to get a random piece from the dictionary

get = 1
gen = 2
delete = 3
customAdd = 4
PRINT = 5
QUIT = 6

file = 'passwordGen.dat'

def main():
    passDict = getPasswords()

    #User chooses what the program should do to the password list
    #Then the program executes what the user wants
    choice = 0
    while choice != QUIT:
        choice = getChoice()
        if choice == get:
            getRand(passDict)
        elif choice == gen:
            generatePassword(passDict)
        elif choice == delete:
            remove(passDict)
        elif choice == customAdd:
            custom(passDict)
        elif choice == PRINT:
            printDict(passDict)  
    saveList(passDict)
#Decrypts the file, if no dictionary it creates one
def getPasswords():
    try:
        inFile = open(file, 'rb')
        passDict = pickle.load(inFile)
        inFile.close()
    except:
        passDict = {}
    return passDict
#Display choices for the user
def getChoice():
    print('1. Get a random password from list')
    print('2. Generate a new password and add to list')
    print('3. Delete a password from the list')
    print('4. Add custom password to list')
    print('5. Print all passwords')
    print('6. Exit program')
    print()
    choice = int(input('Enter a number option from above:'))
    while choice < get or choice > QUIT:
        choice = int(input('Enter a valid option:'))
    return choice
#Makes a list out of the dictionary and then
#Selects a random password from the list to display
def getRand(passDict):
    try:
        tempOut, tempOther = random.choice(list(passDict.items()))
        print(passDict.get(tempOut, 'Invalid'))
        print()
    except:
        print('No passwords in list')
#Gets input/info from user then generates a password from the info
#The password is then added to the dictionary
def generatePassword(passDict):
    print('Enter some information')
    color = input('Enter a color (or any word you want):')
    info = input('Enter another word:')
    other = int(input('Enter a number:'))
    chars = ['*','(',')','$','#','@','!']

    password = str(info + color[-3:] + str(other) + random.choice(chars))
    print('The password is:', password)
    strenTemp = str(input('Password Strength: '))
    strength = ('Password strength:', strenTemp)
    
    passClass = Password(password, strenTemp)
    if password not in passDict:
        passDict[password] = passClass
        print(password, 'has been added to the list')
    else:
        print('That password already exists')
#Removes a password, specified by the user, from the dictionary
def remove(passDict):
    password = input('Enter a password to remove: ')
    if password in passDict:
        del passDict[password]
        print('Password deleted')
    else:
        print('Password not found')
#Lets the user add a password manually
def custom(passDict):
    temp = str(input('Enter a password to add to your list: '))
    strenTemp = str(input('Password Strength: '))
    strength = ('Password strength:', strenTemp)

    passClass = Password(temp, strenTemp)
    if temp not in passDict:
        passDict[temp] = passClass
        print(temp, 'has been added to your list')
    else:
        print('This password is already in the list')
#Encrypts the file
def saveList(passDict):
    outFile = open(file, 'wb')
    pickle.dump(passDict, outFile)
    outFile.close()
#Prints every piece in the dictionary
def printDict(passDict):
    for i in passDict:
        print(passDict.get(i, 'Invalid'))
        print()
main()
