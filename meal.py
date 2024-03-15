def main():
    # Get time from user
    Input = input("What time is it? ")
    #call convert
    time = convert(Input)
    #breakfast between 7 - 8
    if time >= 7 and time <= 8:
        print("breakfast time")
    # lunch between 12 - 13
    elif time >= 12 and time <= 13:
        print("lunch time")
    # dinner 18 - 19
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # get hour and minute
    hours, minutes = time.split(":")
    # convert time intro a float number
    newMinutes = float(minutes) / 60
    return float(hours) + newMinutes


if __name__ == "__main__":
    main()

