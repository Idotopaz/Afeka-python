def count_letter(words, ch):

    total = 0
    if words == []:
        return total
    total = words[0].count(ch)

    if words != []:
        words.pop(0)
        return count_letter(words,ch)+total

def main():
    print(count_letter(["gogo", "momo","yoyo","dodo"],"o"))

if __name__=="__main__":
    main()
