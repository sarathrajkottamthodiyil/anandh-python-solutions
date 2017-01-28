def my_sum(a,b):
    c = a+b
    return c

result =  my_sum(5,8)

print result


def my_string(a):
    d = len(a)
    return d
print my_string("sarath")   


def length(b):
    c = len(b)
    if c >= 6:
        return True
    else:
        return False


s = ["nml","lk", "nmlop", "sxxj", "sarath"]


a = []
for i in s:
    if length(i)== True:
        a.append(i)
print a     



def foo(f):



    k = []
    for i in f:
        if i.startswith("nm"):
            k.append(i)
    return k
print foo(s) 



def bin(m):
    j = []
    for i in m:
        if i.startswith("s"):
            t=i[1:]
            j.append(t)


    return j
print bin(s)            

         

def count_digits(a)
    b = len(a)
    return b
print count_digits(41516261)    



