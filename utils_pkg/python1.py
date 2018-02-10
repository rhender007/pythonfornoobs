'''
# Created on Feb 3, 2018
 
#@author: Robert Henderson
'''

print("********App1********")
lst= ["easy", "simple", "cheap", "free"]
print(lst[-1])
 
lst = [3,5,7]
lst.append(42)
print(lst)
 
lst2 = [3,5,7]
lst2.append(42)
print(lst2)
 
cities = ["Hamburg", "Linx", "Salzburg", "Vienna"]
cities.pop(1)
print(cities)

print("********App2********")
languages = ["C", "C++", "Perl", "Python"]
 
for x in languages:
    print(x)

print("********App3********")     
edibles = ["Ham","Spam", "Eggs", "Nuts"]
for food in edibles:
    if food =="Spam":
        print("No more Spam, Please!")
        break
    print("Great, delicious " +food)
else:
    print("I am so glad, No Spam")
print("Finally, I finished stuffing myself")

print("********App4********")   
#my_list = ["one","two","three","four","five"]
fibonacci = [0,1,1,2,3,5,8,13,21]
my_list = fibonacci
my_list_len = len(my_list)
for i in range(0,my_list_len):
    print(my_list[i])
    #print(i)

print("********App5********")       
count = 0
sum =0
number = 1
print("Enter 0 to exit the loop")
while(number!=0):
    number=float(input("Enter a number: "))
    if number!=0:
        count = count+1
        sum = sum+number
    if number ==0:
        print("The average was ", sum/count)
         
#from pip._vendor.distlib.locators import Page

#App2     
print("********App6********") 
sum = 0.0
print('This program will take several numbers then average them')
count = int(input("How many numbers would you like to average: "))
start_count = 0;
while start_count < count:
    start_count = start_count +1
    number = float(input("Enter a number: "))
    sum = sum+number

print("Average: ", sum/count)
print("Average using start count", sum/start_count)

a=0
b=1
count = 0
max_count =5
arrayList = []
while count < max_count:
    count = count+1
    print(a, b, end=" ") # This keeps from printing a new line
    a = a + b
    b = a + b
'''
def function_name(parameter_list): #defines a function
    statements -> This is the function body'''

def fahrenheit(t_in_celcius):
    return t_in_celcius *9/5 +32

a=fahrenheit(0)
print(a)

for t in (23,6,25,8,27,3,29.8):
    print(t, ":", fahrenheit(t))
 
def avg(intFirst, *intRest):
    return (intFirst+ sum(intRest))/(len(intRest)+1)
 
print(avg(1,2,3,4,5))


def average(*interest):
    return(sum(interest)/len(interest))

xList = [3,5,9]
print(average(*xList))
print(average(3,5,9))

    
def has_permission(page):
    def inner(username):
        if username =="Admin":
            return "'{0}' does have access to {1}".format(username,page)
        else:
            return "'{0}' does not have access to {1}".format(username, page)
    return inner

current_user = has_permission('Admin Area')
print(current_user)
print(current_user('Admin'))