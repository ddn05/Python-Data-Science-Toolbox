print("Introduction to interatior")

employess = ["Ahmad","Sakura","Baban","Mamat"]
for employe in employess:
    print(employe)
    
print("--------------------------------------")

for ex in "Dadan":
    print(ex)
    
print("--------------------------------------")
    
for i in range(5):
    print(i)
    
print("--------------------------------------")

word = "Abcd"
word2 = "Dadan"

it = iter(word)
it2 = iter(word2)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

print(*it2)

print("-------------------------------------- Dictionary")

dict = {"Country" : "Indonesia", "Capitals" : "DKI Jakarta"}
for k,v in dict.items():
    print(k,v)
    
print("--------------------------------------")

file = open('E:/PROGRAMMING/GITHUB REPO/Python-Data-Science-Toolbox/file.txt')

it2 = iter(file)

print(*it2)