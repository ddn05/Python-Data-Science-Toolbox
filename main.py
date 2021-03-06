print(">> User defined example")

def kotak():
    nilai=2**2
    print(nilai)

kotak()

print("----------------------------------")
print(">> Multiple User defined Example")

nilai = (1,2,3)
print(type(nilai))

a,b,c = nilai
print(c)
print(nilai[1])

print("----------------------------------")
print(">> Nested Function")

def nesmod(x1,x2,x3):
    def inner(x):
        return x % 2 + 5
    return(inner(x1), inner(x2), inner(x3))

print(nesmod(1,2,3))

print("----------------------------------")
print(">> Default and flexible argument")

def power(nilai1, pow=1):
    nilai_baru = nilai1 ** pow
    print(nilai_baru)
    
power(2,2)

def tambah(*args):
    n = 0
    for y in args:
        n += y
    print(n)

tambah(10,20,30,5)

print("----------------------------------")
print(">> Lambda Function")

nilai = lambda x,y : x ** 2
print(nilai(4,2))

nomor = [23,33,65,77]
nilai = map(lambda num : num ** 2, nomor)
print(list(nilai))

print("----------------------------------")
print(">> Error Handling")

def eh(x):
    try:
        return x ** 2
    except:
        print("x harus INTEGER atau FLOAT")
        
print(eh("HAI"))