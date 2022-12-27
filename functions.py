

def add_mult(a,b):
    c = a + b
    d = a * b
    return c , d

addition,mult=add_mult(10,12)

print(addition)
print(mult)

def fun(a):
    a = 10
    print(a)

a = 12

fun(a)
print(a)

def fun(lst):
    lst[2] = 10
    print(lst)

lst = [12, 14, 16, 18, 20]

fun(lst)
print(lst)


def fun(name, age=18):  # default value in argument in age
    print(name,age)

fun(age=20,name="Anas Siddiqui")   # Keyword Arguments

def sum(*b):
    c = 0
    for i in b:
        c = c + i
        #print(c)
    print(c)

sum(10,20,30,40,50)
