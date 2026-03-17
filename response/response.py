from validator_collection import checkers

#En la libreria indica que y como utilizarlos en este caso utilice checkers, pero
#puede ser otro validators o onclusive errors

def main():
    print(email(input("What's your email address? ")))


def email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
