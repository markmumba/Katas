# .................................................................
# code to reverse a list given letter to dictate which side to do so 
# .................................................................
# def flip(d, a):
#     if d == "R":
#        a.sort()
#        return a
#     else:
#         a.sort(reverse=True)
#         return a
   
# words= flip('L',[2,4,3,5,6,7,8,6,1])
# print(words)


# ...................................................................
# code to return the value sitting in the even idexes inside the list
# ...................................................................
# def odd_place(my_list):
#     empty = []
#     for i in range(len(my_list)):
#         if i % 2 ==0:
#             empty.append(my_list[i])
#     print(empty)          
# my_list=odd_place([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])            


# ............................................................................
#  returns a list of all the powers of 2 with the exponent ranging from 0 to n
# ............................................................................
# import math

# def powers_of_two(n):
#     empty=[]
#     for num in range(n+1):
#         empty.append(int(math.pow(2,num)))
#     print (empty)  
# test=powers_of_two(4)

# ..................
# Magic 8 Ball game
# .................

# import random

# print("Enter your Question")
# inputed=input()
# answers=["It is Certain.",
# "It is decidedly so.",
# "Without a doubt.",
# "Yes definitely.",
# "You may rely on .",
# "As I see it, yes.",
# "Most likely.",
# "Outlook good.",
# "Yes.",
# "Signs point to yes.",
# "Reply hazy, try again.",
# "Ask again later.",
# "Better not tell you now.",
# "Cannot predict now.",
# "Concentrate and ask again.",
# "Don't count on it.",
# "My reply is no.",
# "My sources say no.",
# "Outlook not so good.",
# "Very doubtful."]
# answer=random.choice(answers)
# print(answer)

# ..............................................................................................................
#  capitilize the first letter then use the postion of the letter to get the rest of the letters in lower case 
# .............................................................................................................
# def accum(s):
#     roj=""
#     letters=list(s)
#     # print(letters)
#     for letter in letters:
#        roj+=letter.capitalize()+(letter*letters.index(letter)).lower()+"-"
#     return roj
    
# test=accum("MjtkuBovqrU")
# print(test)


# ...................................................................................
# Adding to list together to get sum of the numbers on the same idexes 
# ............................................................................

# arr1=[2,3,4,5,6,7,5,3]
# arr2=[3,4,7,4,2,1,5,0]

# sumed = 0
# empty=[]
# for i in range(0,len(arr1)):
#         sumed=arr1[i]+arr2[i]
#         empty.append(sumed)

# print( empty )
        

# ........................................................................................
# Looking for letter that is not repeated  in the string 
# ........................................................................................
# def removeRepeat(s):
#     listed = list(s)
#     for letter in listed:
#         if listed.count(letter)==1:
#             return letter

# test = removeRepeat('bbbbeeekkkkggggllllllsssstjjjjj')
# print(test)
        