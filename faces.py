def main():
    sentence = input("Input a Sentence: ")
    convert(sentence)
    sentence = convert(sentence)
    print(sentence)

def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

main()
