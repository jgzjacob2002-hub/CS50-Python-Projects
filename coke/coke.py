i = 50

while True:
    print(f"Amount Due: {i}")
    x = int(input("Insert Coin: ").strip())

    if x == 25 or x == 10 or x == 5:
        i -=x
    if i <= 0:
        print(f"Change Owed: {i*-1}")
        break
    else:
        continue



