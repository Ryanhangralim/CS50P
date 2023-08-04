vowel = ["a", "i", "u", "e", "o"]


def main():
    output = shorten(input("Input: "))
    print(f"Output: {output}")


def shorten(word):
    twttr = ""
    for i in range(len(word)):
        char = word[i]
        if char.lower() in vowel:
            continue
        else:
            twttr += char
    return twttr


if __name__ == "__main__":
    main()
