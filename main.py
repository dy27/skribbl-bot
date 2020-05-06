def load_wordbank():
    wordbank = []
    with open('wordbank.txt', 'r') as f:
        for line in f:
            wordbank.append(line.strip())
    return wordbank


def length_filter(wordbank, length):
    return filter(lambda word: len(word) == length, wordbank)


def char_filter(wordbank, char, index):
    return filter(lambda word: word[index] == char, wordbank)


if __name__ == "__main__":
    wordbank = load_wordbank()
    wordbank = list(length_filter(wordbank, 7))
    wordbank = list(char_filter(wordbank, 'a', 2))
    print(wordbank)
