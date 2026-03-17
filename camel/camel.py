camel = input("camelCase: ").strip()
came2 = ""

for camels in camel:
    if (camels.isupper()):
        came2 = came2 + "_" + camels.lower()

    else:
        came2 = came2 + camels

print(came2)
