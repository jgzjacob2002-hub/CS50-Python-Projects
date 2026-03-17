import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe.+><\/iframe>",s):
        if number := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(?P<numeros>[^"]+)"',s):
            return f'https://youtu.be/{number.group("numeros")}'
    else:
        None


...


if __name__ == "__main__":
    main()
