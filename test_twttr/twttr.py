def main():
    x = shorten(input("Input: ").strip())
    print (f"Output: {x}")


def shorten(word):
    for vocales in ("aeiouAEIOU"):
        word = word.replace(vocales, "")
    return word



if __name__ == "__main__":
    main()
