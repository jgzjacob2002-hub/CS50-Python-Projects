import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        dividido = ip.split(".")
        for valido in dividido:
            if int(valido) >= 256 or int(valido) < 0:
                return False
            if valido != "0" and valido.startswith("0"):
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
