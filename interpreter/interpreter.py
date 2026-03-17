expression = input ("Expression: ").strip()
x, y, z = expression.split(" ")
x = int(x)
z = int(z)


match y:
    case "+":
        j = float(x + z)
        print(f"{j:.1f}")
    case "-":
        j = float(x - z)
        print(f"{j:.1f}")
    case "*":
        j = float(x * z)
        print(f"{j:.1f}")
    case "/":
        j = float(x / z)
        print(f"{j:.1f}")

