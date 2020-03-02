# fiz = input("Type Fizz: ")
# buz = input("Type Buzz: ")
#
#
# def fizbiz(count):
#     for i in range(count):
#         if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
#             print("fizbuz")
#         elif (i + 1) % 5 == 0:
#             print(buz)
#         elif (i + 1) % 3 == 0:
#             print(fiz)
#         else:
#             print(i + 1)
#
# fizbiz(10)

# for num in range (1,21):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 5 == 0:
#         string = string + "Buzz"
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)
#     print(string)

# from random import randrange
#
# wordlist = ["destination", "random", "youtube", "names", "wannabe"]
#
# randomNum = randrange(5)
# print(randomNum)
# word = wordlist[randomNum]
#
#
# def getChar():
#     guessing = input("Guess a letter: ")
#     allowChars = "abcdefghijklmnopqrstuvwxyz"
#     while (len(guessing) != 1 or guessing not in allowChars):
#         guessing = input("You have entered wrong pattern. Please enter one letter")
#     return guessing
#
#
# wordIsNotComplete = True
# numOfLetters = len(word)
# while wordIsNotComplete:
#     guessing = getChar()
#     if guessing in word:
#         word = word.replace(guessing, '')
#         numOfLetters = numOfLetters - 1
#         print(str(numOfLetters) + " left")
#     else:
#         print("wrong letter, guess again")
#     if (numOfLetters == 0):
#         print("Congrats, you got the word")
#         break

def printRepeating(arr,size) :
    count = [0] * size
    print(" Repeating elements are ")
    for i in range(0, size) :
        if(count[arr[i]] == 1) :
            print(arr[i])
        else :
            count[arr[i]] = count[arr[i]] + 1

arr = [0, 2, 4, 1, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)