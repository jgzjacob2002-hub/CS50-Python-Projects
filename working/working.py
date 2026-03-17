import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"([0-9][0-2]?):?([0-5][0-9])? ([A|P]M) (to) ([0-9][0-2]?):?([0-5][0-9])? ([A|P]M)", s)
    if match:
        uno = match.group(3)
        dos = match.group(7)

        if match.group(2) == None:
            nada_ida = ":00"
        else:
            nada_ida = ":" + match.group(2)

        if match.group(6) == None:
            nada_back = ":00"
        else:
            nada_back = ":" + match.group(6)

        if uno == "PM":
            if (int(match.group(1)) + 12) == 24:
                tarde_ida = "12"
            else:
                tarde_ida = int(match.group(1)) + 12
        else:
            if int(match.group(1)) == 12:
                tarde_ida = "00"
            elif int(match.group(1)) < 10:
                tarde_ida = "0" + match.group(1)
            else:
                tarde_ida = int(match.group(1))

        if dos == "PM":
            if (int(match.group(5)) + 12) == 24:
                tarde_back = "12"
            else:
                tarde_back = int(match.group(5)) + 12
        else:
            if int(match.group(5)) == 12:
                tarde_back = "00"
            elif int(match.group(5)) < 10:
                tarde_back = "0" + match.group(5)
            else:
                tarde_back = int(match.group(5))

        return f"{tarde_ida}{nada_ida} to {tarde_back}{nada_back}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
