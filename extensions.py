Input = input("File name: ")
lowerInput = Input.lower()

if '.gif' in lowerInput:
    print("image/gif", end =" ")
elif '.jpeg' or 'jpg' in lowerInput:
    print("image/jpeg", end =" ")
elif '.png' in lowerInput:
    print("image/png", end =" ")
elif '.pdf' in lowerInput:
    print("application/pdf", end =" ")
elif '.txt' in lowerInput:
    print("text/plain", end =" ")
elif '.zip' in lowerInput:
    print("application/zip", end =" ")
elif '.bin' in lowerInput:
    print("application/octet-stream", end =" ")
