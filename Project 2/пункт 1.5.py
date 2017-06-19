file = open('resultZS.csv', 'r', encoding = 'utf-8')
file1 = open('Result 1.csv', 'w', encoding = 'utf-8')

tags = file.read()
res = tags.replace('P-3fsn', 'SPRO 3p,nom,sg')
file1.write(res)

file.close()
