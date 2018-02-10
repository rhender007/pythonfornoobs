a=0
b=1
count = 0
max_count =5
arrayList = []
while count < max_count:
    count = count+1
    # 0 , 1
    # 1 , 2
    # 3 , 5
    # 8 , 13
    # 21 , 34
    print(a, b, end=" ") # This keeps from printing a new line
    # 0, 1, 1, 2, 3, 5, 8, 13
    a = a + b
    b = a + b