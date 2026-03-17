def main():
    saludo = value(input("Greeting: ").strip())
    print(f"${saludo}")


def value(greeting):
    x = greeting.lower().split(",")
    greeting = greeting.lower()

    if  x[0] == "hello":
        return 0

    elif (greeting != "hello") and (greeting.startswith("h") == True):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
