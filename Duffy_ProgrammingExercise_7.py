# Import the regular expressions module.
import re


def acceptor():
    """
    Collects a paragraph from the user and displays the matched sentences.

    Parameters:
        None

    Variables:
        paragraph (str): The paragraph entered by the user.
        sentence_count (int): The number of matched sentences returned by enumerator().
        sentence_list (list): The list of matched sentence strings returned by enumerator().
        index (int): The numbered position of each sentence in the displayed output.
        sentence (str): The current sentence being displayed from sentence_list.

    Logic:
        1. Print a welcome message and brief program instructions.
        2. Prompt the user to enter a paragraph.
        3. Pass the paragraph to enumerator() for sentence matching.
        4. Print the total number of matched sentences.
        5. Print each matched sentence with its numbered position.

    Return:
        None
    """

    # Introduce the program and the instructions.
    print()
    print("Welcome To The Sentence Enumeration Utility!")
    print("Please enter a paragraph so its sentences can be enumerated.\n")

    # Read the paragraph entered by the user.
    paragraph = input(">>> ")

    # Store the sentence count and matched sentence list returned by enumerator().
    sentence_count, sentence_list = enumerator(paragraph)

    # Print the sentence count heading.
    print(f"\nThere are {sentence_count} sentences:")

    # Print each matched sentence with its numbered position.
    for index, sentence in enumerate(sentence_list, start=1):
        print(f"{index}: {sentence}")


def enumerator(paragraph):
    """
    Matches complete sentences in a paragraph and counts how many are found.

    Parameters:
        paragraph (str): The paragraph entered by the user for sentence matching.

    Variables:
        pattern (str): The regular expression pattern used to match sentences that
            begin with a capital letter or number and end with sentence punctuation.
        sentence_list (list): The list of sentence strings matched in the paragraph.
        sentence_count (int): The total number of matched sentences in sentence_list.

    Logic:
        1. Store the regular expression pattern for sentence matching.
        2. Use re.findall() to collect every matching sentence in the paragraph.
        3. Count the number of matched sentences.
        4. Return the sentence count and the list of matched sentences.

    Return:
        int: The total number of matched sentences.
        list: The list of matched sentence strings.
    """

    # Store the regular expression pattern used to match complete sentences.
    # Match a capital letter or number followed by any number of characters.
    # End with valid punctuation but only if it is followed by a space and then
    # another capital letter or number, or the end of the paragraph.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Match all valid sentences in the paragraph using the regular expression flags.
    # Let DOTALL match across line breaks and let MULTILINE recognize line endings.
    sentence_list = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Count the total number of matched sentences.
    sentence_count = len(sentence_list)

    # Return the sentence count and the list of matched sentences.
    return sentence_count, sentence_list


def main():
    """
    Runs the sentence enumeration program.

    Parameters:
        None

    Variables:
        None

    Logic:
        1. Call acceptor() to collect input and display the results.

    Return:
        None
    """
    # Call acceptor() to run the program.
    acceptor()


# Call main() only when the file runs directly.
if __name__ == "__main__":
    main()