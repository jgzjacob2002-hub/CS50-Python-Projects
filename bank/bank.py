saludo = input("Greeting: ").strip().lower()
x = saludo.split(",")


if  x[0] == "hello":
    print("$0")

elif (saludo != "hello") and (saludo.startswith("h") == True):
    print("$20")

else:
    print("$100")
