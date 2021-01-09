import pandas as pd

result = []

for chunk in pd.read_csv('E:/PROGRAMMING/GITHUB REPO/Python-Data-Science-Toolbox/data.csv', chunksize = 1000):
    result.append(sum(chunk['x']))

total = sum(result)
print(total)

print("------------------------")

tot = 0
for chunk in pd.read_csv('E:/PROGRAMMING/GITHUB REPO/Python-Data-Science-Toolbox/data.csv', chunksize=1000):
    tot += sum(chunk['x'])
    
print(tot)