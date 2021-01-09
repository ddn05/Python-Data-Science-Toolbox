avengers = ['iron man','thor','spiderman','dr tron']

e = enumerate(avengers)

print(type(e))

e_list = list(e)
print(e_list)

for i,v in enumerate(avengers):
    print(i,v)
    
print("------------------------")

for i,v in enumerate(avengers, start=10):
    print(i,v)
    
print("------------------------")

names = ['wawan','bambang','eren','mikasa']
for z1,z2 in zip(avengers,names):
    print(z1,z2)
    
print("------------------------")

z = zip(avengers,names)
z_list = list(z)

print(z_list)