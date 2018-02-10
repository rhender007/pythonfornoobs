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