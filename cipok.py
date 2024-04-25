


textContent = []
with open("cipok.txt","r" ,encoding="utf8" ) as text:

    firstLine = text.readline().strip().split()
    shoes = dict()
    shoes["A"] = firstLine[0]
    shoes["B"] = firstLine[1]
    shoes["C"] = firstLine[2]
    for line in text:
        tempLine = line.strip().split()
        row = dict()
        row["Shoes"] = tempLine[0]
        row["Prices"] = tempLine[1]
        row["OnStock"] = tempLine[2]
        textContent.append(row)

print(textContent)
#mennyibe kerül keresés
name =input("Shoes name: ")
while name != "":
    name =input("Shoes name: ")