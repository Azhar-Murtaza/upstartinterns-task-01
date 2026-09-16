def word_count(sentence):
    """Return the number of words in a sentence."""
    words = sentence.split()
    return len(words)


def longest_word(sentence):
    """Return the longest word in a sentence."""
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)


def reverse_sentence(sentence):
    """Return the sentence with its characters reversed."""
    return sentence[::-1]


def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    print("=== Text and Number Tools ===")

    sentence = input("Enter a sentence: ")
    number = int(input("Enter a number: "))

    print("\n--- Results ---")
    print("Word count:", word_count(sentence))
    print("Longest word:", longest_word(sentence))
    print("Reversed sentence:", reverse_sentence(sentence))

    if is_prime(number):
        print("Prime check:", number, "is a prime number.")
    else:
        print("Prime check:", number, "is not a prime number.")


if __name__ == "__main__":
    main()
