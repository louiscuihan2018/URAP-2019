import csv
name = []
cap = []
radius = []
new_r = []
new_n = []
with open('Presas_datos2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    for row in reader:
        name.append(row[0])
        cap.append(row[3])
        if row[3] != 'null':
            radius.append(float(row[3])/100)
        else:
            radius.append(0)
csvfile.close()
#x = input('Enter your input:')
#index = name.index(x)
#print(name[index], cap[index], radius[index])
new_n = sorted(name, key=str.lower)
print(new_n)

for x in new_n:
    new_r.append(radius[name.index(x)])

print(new_r)
#print(radius)