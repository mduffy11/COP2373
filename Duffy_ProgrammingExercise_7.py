import re

def acceptor():
    print()
    print('Welcome to the Sentence Enumeration Utility')
    print('Please input a paragraph for which you would')
    print('like to enumerate its sentences below.')

    paragraph = input('> ')

    sentence_count, sentence_list = enumerator(paragraph)

def enumerator(paragraph):

    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Match all valid sentences in the paragraph.
    sentence_list = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Count the total number of matched sentences.
    sentence_count = len(sentence_list)

    # Return the sentence count and the list of matched sentences.
    return sentence_count, sentence_list


acceptor()