Input = input("File name: ")
lowerInput = Input.lower()

if '.jpeg' or 'jpg' in lowerInput:
    print("image/jpeg")
elif '.png' in lowerInput:
    print("image/png")
elif '.gif' in lowerInput:
    print("image/gif")
elif '.pdf' in lowerInput:
    print("application/pdf")
elif '.txt' in lowerInput:
    print("text/plain")
elif '.zip' in lowerInput:
    print("application/zip")
elif '.bin' in lowerInput:
    print("application/octet-stream")

