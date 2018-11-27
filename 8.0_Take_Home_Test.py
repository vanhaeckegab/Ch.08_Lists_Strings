'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________

For every section of code predict what you think it will do and record it. Next, test it
and record what it actually did. It's not a problem if you were wrong.
Make sure you understand WHY it prints what it does.
You don't have to explain it, but if you don't understand why, make sure to ask.
Otherwise you are wasting your time doing these.
'''

'''
1.)
my_list = [5, 2, 6, 8, 101]
print(my_list[1])
print(my_list[4])
print(my_list[5])
'''



'''
2.)
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
'''






'''
3.)
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
my_list2[2] = 10
print(my_list2)
'''







'''
4.)
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)
'''





'''
5.)
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)
'''





'''
6.)
print(len("Force"))
print(len("Force Sensitivity"))
print(len("Force") + len("Sensitivity"))
print(len("2"))
print(len(2))
'''




'''
7.)
print("Death" + "Star")
print("Death" + "Star"[1])
print( ("Death" + "Star")[1] )
'''





'''
8.)
word = "Skywalker"
for letter in word:
    print(letter)
'''






'''
9.)
word = "Han"
for i in range(3):
    word += "Solo"
print(word)
'''






'''
10.)
word = "Jedi" * 3
print(word)
'''






'''
11.)
my_text = "May the force be with you!"
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])
'''






'''
12.)
s = "0123456789"
print(s[1])
print(s[:3])
print(s[3:])
'''



'''
13.)
Write a program that takes a list like the following, and prints the average. 
Use the len function, don't just use 15, because that won't work if the list size changes.
(There is a sum function I haven't told you about. 
Don't use that. Sum the numbers individually as shown in the chapter.) 
(Also, a common mistake is to calculate the average each time through the loop 
to add the numbers. Finish adding the numbers before you divide.)

my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
'''





'''
TEXT FORMATTING:
14.) Take the following program:
     
     score = 41237
     highscore = 1023407
     print("Score:      " + str(score) )
     print("High score: " + str(highscore) )
     
     Which right now outputs:
     
     Score:      41237
     High score: 1023407
     
     Use print formatting so that the output instead looks like:
     
     Score:          41,237
     High score:  1,023,407
     
     Make sure the print formatting works for any integer from zero to nine million.
     Do not use any plus sign (+) in your code.
     You should only have two double quotes in each print statement.
     '''




'''
15.) Create a program that loops from 1 to 20 and lists the decimal
     equivalent of their inverse. Use print formatting to exactly match the following
     output:
     
     1/1  = 1.0
     1/2  = 0.5
     1/3  = 0.333
     1/4  = 0.25
     1/5  = 0.2
     1/6  = 0.167
     1/7  = 0.143
     1/8  = 0.125
     1/9  = 0.111
     1/10 = 0.1
     1/11 = 0.0909
     1/12 = 0.0833
     1/13 = 0.0769
     1/14 = 0.0714
     1/15 = 0.0667
     1/16 = 0.0625
     1/17 = 0.0588
     1/18 = 0.0556
     1/19 = 0.0526
     1/20 = 0.05
'''
