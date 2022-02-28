
# def frequencySort(s:str) -> str:
#     '''
#     This is a function that checks a string  and returns it in the order of the most repeated characters

#     '''
#     dicto = Counter(s)
#     sorted_dict = dict(sorted(dicto.items(),key=lambda item: item[1],reverse=True))
#     ans=''
#     for key,value in sorted_dict.items():
#         ans += key*value
#     return ans


# test  = frequencySort('tree')
# print(test)
# _________________________________________________________________________________________________________________________________

# __________________________________________________________________________________________________________________________________

# import math
# def addRungs(rungs:list, dist: int) -> int:
#     count = 0
#     rungs.insert(0,0)
#     for i in range(len(rungs)-1):
#         gap= rungs[i+1] -rungs[i]
#         if gap > dist:
#             gap =math.ceil(gap/dist)-1
#             count +=gap

#     return count

# test  = addRungs([1,3,5,10],2)
# print(test)


# ___________________________________________________________________________________________________________________________________


# def int_to_Roman( num):
#     lookup = [
#         (1000, 'M'),
#         (900, 'CM'),
#         (500, 'D'),
#         (400, 'CD'),
#         (100, 'C'),
#         (90, 'XC'),
#         (50, 'L'),
#         (40, 'XL'),
#         (10, 'X'),
#         (9, 'IX'),
#         (5, 'V'),
#         (4, 'IV'),
#         (1, 'I'),
#     ]
#     res = ''
#     for (n, roman) in lookup:
#         (d, num) = divmod(num, n)
#         res += roman * d
#     return res

# test = int_to_Roman(645)
# print(test)
# from typing import Generator

# def fib6(n):
#     yield 0
#     if n >0 : yield 1
#     last = 0
#     next=1

#     for _ in range(1,n):
#         last,next = next, last +next
#         yield  next

# if __name__ == '__main__':
#     for i in fib6(50):

#         print(i)


# class Iter:
#     def __init__(self,n):
#         self.n = n

#     def __iter__(self):
#         self.current = -1
#         return self

#     def __next__(self):
#         self.current += 1

#         if self.current >= self.n:
#             raise StopIteration

#         return self.current


# print(hash(Iter))

# reply = input("Enter x and y separated by numbers :")
# x_y = reply.split( )

# x = float(x_y[0])
# y = float(x_y[1])

# print (x,y)

# ___________________________________________________________________________________________________________________________________
# def count_words(word):
#     """A function that takes in a string of letters and returns true if the count of all the letters is equal

#     Args:
#         word (string): the input that is used to check the count 

#     Returns:
#         Boolean : returns true or False if depending on the count of the characters
#     """
#     dicto = {}

#     lowercase = word.lower()
   
#     for char in lowercase:
#         dicto[char] = lowercase.count(char)
#     print(dicto)
#     result = len(list(set(list(dicto.values())))) == 1
#     return result

#     return dicto


# test = count_words("abcabcabc")
# print(test)

# from collections import Counter

# def validate_word(word):
#     return len(set(Counter(word.lower()).itervalues())) == 1

#_______________________________________________________________________________________________________________________________________________________

# def split_in_parts(s, part_length): 
#     """[summary]

#     Args:
#         s ([type]): [description]
#         part_length ([type]): [description]

#     Returns:
#         [type]: [description]
#     """
#     empty =[]
#     for i in range(0 ,len(s), part_length):
#         x=s[i:i+part_length]
#         empty.append(x)
#     return " ".join(empty)






#_________________________________________________________________________________________________________________________________________________________
# from collections import Counter
# # x= Counter ("abcabcabcabc")
# # print(x)
# x = Counter({"i":5,"s":4,"p":2,"m":1})

# print(x.most_common(1))

# def count_letters(filename):
#     f=[]
#     letter_counter  = Counter()
#     with open(filename ) as file :
#         for line in file :
#             for char in line.lower():
#                 if char .isalpha():
#                     f.append(char)
#             letter_counter.update(Counter(f))
            
#     return letter_counter

#______________________________________________________________________________________________
# def fib(n):
#     if n==0: return n 
#     last= 0
#     first=1
#     second = 1
#     for _ in range(1,n):
#         last,first ,second = first,second,second+first+last
#     return second




# if __name__ == "__main__":
#     print(fib(10))


#_____________________________________________________________________________________________

# def findDisappearedNumbers( nums: list )  -> list:
#     list =[]
#     for number in range(1,len(nums)+1):
#         if number not in nums:
#             list.append(number)
#     return list


# test = findDisappearedNumbers([1,1])
# print (test)

#_______________________________________________________________________________________________________


#Type Hinting

# def headline(text: str, align: bool = True) -> str :
#     if align:
#         return f"{text.title()}\n{'-'* len(text)}"

#     else:
#         return f"{text.title()} ".center(50, "0")

# test  = headline("python type checking ",align = False)
# print (test)


#________________________________________________________________________________________________

# def sum_of_two(numbers):
#     numbers.sort()
#     return numbers[0]+numbers[1]


# test=sum_of_two([1,5,7,8,2,9])
# print (test)

#_____________________________________________________________________________________________________

# Finding the perfect square given a number , return true if its perfect return false if its not 
# import math

# def is_square(n): 
#     if n < 0 :
#         return False

#     x=math.sqrt(n)
#     return x.is_integer()
  
  

 
# test = is_square(-1)
# print(test)

#________________________________________________________________________________________________

# Replace characters in strings 

# def  replace_string(s:str)->str:
#     return s.replace("()","o").replace("(al)","al")


# test = replace_string("G()(al)")
# print(test)

# ____________________________________________________________________________________________

# Given a sentence find the shortest's word length 

# def find_shortes_string(sent:str ) ->int :
#     lst=sent.split()
#     return len(min(lst, key=len))

# test = find_shortes_string("bitcoin take over the world maybe who knows perhaps")
# print(test)

# ____________________________________________________________________________________________

# ___________________________________________________________________________________________


# def powers_of_two(n:int)->list:
#     return [ pow(2, x) for x in range(0,n+1)]

# test = powers_of_two(4)
# print(test)

#___________________________________________________________________________________


# def get_vowel_count(s:str)->int:
#     return len([ letter for letter in s if letter in 'aeiou'])

# test= get_vowel_count("abracadabra")
# print(test)
    
#_________________________________________________________________________________________

# def to_underscore(string:str)-> str:
#     string =str(string)
#     final=string[0].lower()
#     for letter in  string[1:]:
#         if letter.isupper():
#             final+="_"+ letter.lower()
#         else:
#             final +=letter

#     return final

  

    
    
# test = to_underscore(1)
# print(test)

#_____________________________________________________________________________________________
# from math import floor
# def get_average(marks:list)->int:
#     return floor(sum(marks)/len(marks))


# test=get_average([2,5,13,20,16,16,10])
# print(test)
#____________________________________________________________________________________________________


# def remove_duplicate_words(s):
#     empty =[]
#     for word in s.split():
#         if word not in empty:
#             empty.append(word) 
#     return " ".join(empty)
# test = remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
# print(test)


#_____________________________________________________________________________________________________________________________

# def odd_ones_out(numbers:list)->list():
#     final =list ([ number for number in numbers if numbers.count(number)%2 ==0])
#     return final



# test = odd_ones_out([75, 68, 75, 47, 68])
# print(test)

#______________________________________________________________________________________


# def reverse_words(text:str)->str:
#     empty=[]
#     text = text.split()
#     for word in text:
#         x=word[::-1]
#         empty.append(x)
#     return " ".join(empty)

#_________________________________________________________________________________________________

# def reverse_words(text:str)->str:
#     ans=[ word[::-1]  for word in text.split()]
#     return " ".join(ans)

# test=reverse_words("This is an example!")
# print(test)

# ____________________________________________________________________________

#     def DNA_strand(dna:str)->str:
#         x=[]
#         for letter in dna:
#             if letter == "A":
#                 x.append("T")
#             elif letter == "T":
#                 x.append("A")
#             elif letter == "C":
#                 x.append("G")
#             elif letter == "G":
#                 x.append("C")  

#         return "".join(x)  



# test= DNA_strand("AAAA")
# print(test)

#_______________________________________________________________________________________

# def to_camel_case(text:str)-> str:
#     """
#     """
#     text=list(text)
#     final =""
#     for index,char in enumerate(text):
#         if char == "-" or char == "_":
#             final = 
#             text[index+1].upper()
#             text.remove(char) 
#     return "".join(text)




# test = to_camel_case("the_steal_th_warrior")
# print(test)


#_______________________________________________________________________________________

# def duplicate_encode(word:str)->str:
#     arr=[]

#     for letter in word :
#         if word.count(letter) != 1:
#             arr.append(")")
#         else:
#             arr.append("(")

#     return "".join(arr)



# test= duplicate_encode("D(@iZ@XVNOu@qHcBwXhfNW@DXz(PP")
# print (test)



#___________________________________________________________________________________

# def unique_in_order(iterable):
#     lst=[]
#     for x in iterable:
#         if x not in lst:
#             lst.append(x)
#     return lst

#___________________________________________________________________________________


# def open_or_senior(data:list)->list:
#     empty = []
#     for values  in data :
#         if values[0] < 55:
#             empty.append("Open")
#         elif values[1] < 7:
#             empty.append("Open")
#         else:
#             empty.append("Senior")
#     return empty

# test = open_or_senior([(26, 17), (19, 9), (78, 26), (16, 0), (72, 5)])
# print(test)


# empty = []

# __________________________________________________________________________________

# def printer_error(s):
#     x="abcdefghijklm"
#     count=0
#     for char in s:
#         if char not in x:
#             count +=1
#     return f"{count} / { len(s)}"


# test = printer_error("aaabbbbhaijjjm")
# print(test)

    


#____________________________________________________________________________


# def binary_array_to_number(arr):

#     s = [  str(i) for i in arr ]
#     x="".join(s)
#     return int(x,2)




# test = binary_array_to_number([0, 0, 0, 1])
# print(test)
    
  
#________________________________________________________________________________________

# def high(x):
    
#     alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
#     'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
#     'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#     count = 0
#     result = {}
#     x=x.split(" ")
#     print(x)
#     for word in x:
#         for letter in word:
                
         
#                 count += alpha.get(letter)
            
               
#         result[word]=count

#     return result






# test = high('man i need a taxi up to ubud')
# print (test)

# _________________________________________________________________________________

# def to_jaden_case(string):
#     return " ".join([  word.capitalize()  for word in string.split()])


# test = to_jaden_case("am so hype'd")
# print(test)

#_________________________________________________________________________________________

# def alphabet_position(text:str) ->str:
#     alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
#     'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
#     'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

#     arr = []
#     text = text.split()
#     for word in text:
#         for letter in word.lower():
#             if letter.isalpha():
#                 if letter in alpha:
#                     arr.append(alpha.get(letter))
#     return " ".join([str(int) for int in arr])



# test = alphabet_position("The sunset sets at twelve o' clock.")
# print(test)

# ___________________________________________________________________________________________________

# def solution(s):
#     if len(s) % 2 !=0:
#         s += "_"
#     lst= [s[i:i+2] for i in range(0,len(s),2)]
#     return lst




# test = solution("asdfads")
# print(test)
#____________________________________________________________________________________________________

# def tower_builder(n_floors:int )-> list:
#     lst=[]
#     x=(2 *n_floors)+1
#     for num in range(1,x, 2):
#         lst.append('*'*num)
#     return lst




# test = tower_builder(6)
# print(test)

# ___________________________________________________________________________________________________



# def sort_array(source_array:list) -> list:

#     b= sorted([item for item in source_array if item%2 != 0])
#     odd_int = 0
#     for i in range(len(source_array)):
#         if source_array[i] % 2 !=0:
#             source_array[i]=b[odd_int]
#             odd_int +=1
#     return source_array    

# test = sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
# print(test)

#______________________________________________________________________________________________________

# def rake_garden(garden):
#     return " ".join(w if w == "rock" else "gravel" for w in garden.split())


# test = rake_garden('slug spider rock gravel slug slug gravel gravel gravel gravel')
# print(test)



#_______________________________________________________________________________________________

# def count_bits(n):
#     x= bin(n).replace("0b", "")
#     m=0
#     for num in str(x):
#         m+= int(num)
        
#     return  m

# test = count_bits(5)
# print(test)


#__________________________________________________________________________________________________
# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.


# #* Solution 1
#import numpy as np
# def dig_pow(n, p):
#     x=np.array([int(i) for i in str(n)])
#     y=np.array([ i for i in range(p,len(x)+p)])
#     m = sum(x ** y)
#     if m%n == 0 :
#         return m//n
#     else:
#         return -1

# test = dig_pow(695, 2)
# print(test)

#* Solution 2
# def dig_pow(n, p):
#     sum = 0
#     for c in str(n):
#         sum += int(c) ** p
#         p += 1
#     if sum % n == 0:
#         return sum / n
#     else:
#         return -1

#______________________________________________________________________________________________________________________________________________________________

# def solution(s):
#     text= list(s)
#     final =""
#     for index, char in enumerate(text):
#         if char.isupper():
#             final += " "
#         final +=char 
#     return final 
 

# test = solution("camelCasing")
# print (test)