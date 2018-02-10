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