def penzvaltas(price: int, arfolyam: float) -> float:
    # Az új ár dollárban vagy euróban
    new_price = round(price * arfolyam, 2)
    return new_price

textContent = []
with open("cipok.txt", "r", encoding="utf8") as text:
    firstLine = text.readline().strip().split()
    shoes = dict()
    shoes["A"] = firstLine[0]
    shoes["B"] = firstLine[1]
    shoes["C"] = firstLine[2]
    for line in text:
        tempLine = line.strip().split()
        row = dict()
        row["Shoes"] = tempLine[0]
        row["Prices"] = int(tempLine[1])  # Konvertáljuk az árat int típusúra
        row["OnStock"] = int(tempLine[2])  # Konvertáljuk az OnStock értéket int típusúra
        textContent.append(row)

arfolyamok = {
    "ft": 1,  # forint
    "usd": 0.0031,  # dollár
    "eur": 0.0027  # euró
}

penznem = input("Válassz valutát (ft/usd/eur): ").lower()
while penznem not in arfolyamok:
    print("Nem megfelelő valuta! Kérlek válassz ft/usd/eur közül.")
    penznem = input("Válassz valutát (ft/usd/eur): ").lower()

name = input("Shoes name: ")
while name != "":
    found = False
    for shoe in textContent:
        if name == shoe["Shoes"]:
            print(f"The {shoe['Shoes']} price: {shoe['Prices']} HUF")
            print(f"The price in {penznem.upper()}: {penzvaltas(shoe['Prices'], arfolyamok[penznem]):.2f} {penznem.upper()}")
            if shoe["OnStock"] > 0:
                print("The shoes are in stock.")
            else:
                print("The shoes are out of stock.")
            found = True
            break
    if not found:
        print("Shoes not found.")
    name = input("Shoes name: ")
