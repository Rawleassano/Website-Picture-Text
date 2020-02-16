#  program that collects the range as any input number from the user

n = int(input('Enter Range Number:'))   # Made a variable in n that can collect a number and place it as the range for the loop
for num in range(n):                    #the input range number will be put in the place of n
  number = int(input('Enter a number:'))# parameter for number inputed by keyboard
  print('The number is ' + str(number))

  
#CODE FOR QUESTION 3
#program that stores each value input in a list called vals

n = int(input('Enter Range Number:'))  
vals = []  				#Create an empty list called numeric which will consist of numeric values
count = 0   				# set starting count to save numbers

for num in range(n):                    # all numbers not exceeding in input
  number = int(input('Enter a number:'))
  vals.insert(num, number)		# this inserts all the input numbers in the list vals
  num = count + 1# this uses the count variable, keeps each number has it is added from input
  print('The number is ' + str(number))
# uncomment below to print the list
#print('The Listed values are '  + str(vals)) # displays all the numbers as a list


#CODE FOR QUESTION 4
#program that prints the first and last element of the list

n = int(input('Enter Range Number:'))  
vals = []  				
count = 0   				

for num in range(n):                   
    number = int(input('Enter a number:'))
    vals.insert(num, number)		
    num = count + 1
print('The number is ' + str(number))
# uncomment below to print the list
#print('The Listed values are '  + str(vals)) # displays all the numbers as a list

first_element = int(vals[0])            # every first element in a list iis always at 0 for any list
vals2 = vals.reverse()                  # this line of code reverses the enter list putting the last element in the list at the front
last_element = vals[0]                  # aftering reversing the list the index of the last element which is now the frist can be specified by index 0
print('The first element in the list is ' + str(first_element)) #displays the first element in the lis
print('The last element in the list is ' + str(last_element))   #displays the last element in the list



#CODE FOR QUESTION 5:
#program that prints the enire list using from program 3 for loop 

n = int(input('Enter Range Number:'))  
vals = []  				#Create an empty list called numeric which will consist of numeric values
count = 0   				# set starting count to save numbers

for num in range(n):                    # all numbers not exceeding in input
  number = int(input('Enter a number:'))
  vals.insert(num, number)		# this inserts all the input numbers in the list vals
  num = count + 1                       # this uses the count variable keeps each number has it is added from input
  print('The Listed values are '  + str(vals))	 # displays all the numbers as a list



#CODE FOR QUESTION 6
#program that generates random numbers between 1 and 10 and saves them to list called ran_list, gives the count of numbers less than 5 within the list and prints the largest and the smallest number in the list.

import random               #call in the random module

ran_list= []                #  create a list that stores all random numbers
lengt_num = []              # create a list that stores numbers less than  5
count = 0                   # starting count set to 0


for num in range(10):       # the amount of numbers needed which is up to 10
    number = random.randrange(1, 10) # the range in which the numbers need to be in 
    ran_list.insert(num, number)    # add numbers to the list called ran_list= []  
    num = count + 1    
print('Some random numbers are ' +  str(ran_list))  #random numbers generated will be printed
for i in ran_list:          
    if i < 5:
        lengt_num.append(i)             
        i = count + 1 
print('The amount of numbers less than 5 is ' + str(len(lengt_num)))  #the amount of numbers less than 5 will be counted and print
print('The smallest number is ' + str(min(ran_list))) #the largest number in the list wil be printed
print('The smallest number is ' + str(max(ran_list))) #the smallest number in the list wil be printed



