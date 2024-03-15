Input = input("File name: ")
lowerInput = Input.lower()

if '.' not in lowerInput:
    print("application/octet-stream", end="")
elif '.gif' in lowerInput:
    print("image/gif", end ="")
elif '.png' in lowerInput:
    print("image/png", end ="")
elif '.pdf' in lowerInput:
    print("application/pdf", end ="")
elif '.txt' in lowerInput:
    print("text/plain", end ="")
elif '.zip' in lowerInput:
    print("application/zip", end ="")
elif '.bin' in lowerInput:
    print("application/octet-stream", end ="")
elif '.jpeg' or 'jpg' in lowerInput:
    print("image/jpeg", end ="")

