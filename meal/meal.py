def main():
    meal = convert(input("What time is it? ").strip().replace("a.m.", "").replace("p.m.", ""))
    if 7 <= meal <= 8:
        print("breakfast time")

    elif 12 <= meal <= 13:
        print("lunch time")

    elif 18 <= meal <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    time = ((float(hours) * 60) + float(minutes)) / 60
    return time


if __name__ == "__main__":
    main()
