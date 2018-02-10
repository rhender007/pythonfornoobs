print("********App1********")
lst= ["easy", "simple", "cheap", "free"]
# first print
print(lst[-1])
 
lst = [3,5,7]
lst.append(42)
# second print
print(lst)
 
lst2 = [3,5,7]
lst2=lst2.append(42) #dont do this!!
# third print
print(lst2)
 
cities = ["Hamburg", "Linx", "Salzburg", "Vienna"]
cities.pop(1)
# fourth print
print(cities)