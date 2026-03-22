import re

def acceptor():

    # Introduce the program and the instructions.
    print()
    print("Welcome To The Sentence Enumeration Utility!")
    print("Please enter a paragraph so its sentences can be enumerated.\n")

    # Read the paragraph entered by the user.
    paragraph = input("> ")

    # Store the sentence count and matched sentence list returned by enumerator().
    sentence_count, sentence_list = enumerator(paragraph)

    # Print the sentence count heading.
    print(f"\nYou have {sentence_count} sentences:")

    # Print each matched sentence with its numbered position.
    for index, sentence in enumerate(sentence_list, start=1):
        print(f"{index}: {sentence}")

def enumerator(paragraph):

    # Store the regular expression pattern used to match complete sentences.
    # Match a capital letter or number followed by any number of characters.
    # End with valid punctuation only when it is followed by a space and then
    # another capital letter or number, or the end of the paragraph.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Match all valid sentences in the paragraph.
    sentence_list = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Count the total number of matched sentences.
    sentence_count = len(sentence_list)

    # Return the sentence count and the list of matched sentences.
    return sentence_count, sentence_list


def main():

    acceptor()

if __name__ == "__main__":
    main()