# Function to recieve input and give output
def prompter():
    """
    Prompts the user to enter an email message, normalizes the message,
    scans it for spam trigger phrases, and prints the results.

    Parameters:
        None

    Variables:
        message (str): Raw message input entered by the user.
        clean_message (str): Normalized message after removing punctuation,
                             collapsing whitespace, and converting to lower case.
        score (int): Total spam score based on trigger phrase occurrences.
        hits (list): List of (phrase, occurrences) tuples for matched phrases.
        rating (str): Spam likelihood message based on score.

    Logic:
        1. Prompt the user to enter an email message.
        2. Normalize the message (lowercase, remove punctuation, collapse spaces).
        3. Pass the cleaned message to the scanner function to calculate score/hits.
        4. Pass the score to the auditor function to determine the spam rating.
        5. Display the spam score, rating, and matched phrases.

    Return:
        None
    """
    # Read input from the user
    message = input("Enter your message: ")
    # Clean the input before scanning
    clean_message = normalizer(message)

    # Pass message to the scanner function for scoring and return a tuple
    score, hits = scanner(clean_message)

    # Print rating
    rating = auditor(score)
    print("\nSpam score:", score)
    print("The results are in: ", rating)

    # Display the words/phrases which caused it to be spam
    if len(hits) > 0:
        print("Matched phrases:")
        for phrase, occurrences in hits:
            print(f"- {phrase} ({occurrences})")
    else:
        print("Matched phrases: None")


# Function that prefers the inspection
def scanner(message):
    """
    Scans a normalized email message for spam trigger phrases and calculates
    a spam score based on the number of occurrences of each trigger phrase.

    Parameters:
        message (str): A normalized email message (lower case, punctuation removed,
                       and whitespace collapsed).

    Variables:
        scam_score (int): Accumulates one point per occurrence of trigger phrases.
        hits (list): Collects matched phrases and their occurrence counts.
        phrase (str): A trigger phrase from the triggers list.
        clean_phrase (str): Normalized version of the trigger phrase.
        occurrences (int): Number of times clean_phrase occurs in message.

    Logic:
        1. Initialize scam_score to 0 and hits to an empty list.
        2. Loop through each phrase in the triggers list.
        3. Normalize the phrase to match the same format as the message.
        4. Count the number of occurrences of the phrase in the message.
        5. Add occurrences to scam_score.
        6. If occurrences > 0, store (phrase, occurrences) in hits.
        7. Return the final scam_score and hits list.

    Return:
        tuple: (int, list) The scam score and a list of matched phrases with counts.
    """
    # Initialize counter
    scam_score = 0
    # Create a list of phrases that were matched
    hits = []
    # Loop through the 30 phrases
    for phrase in triggers:
        # Clean the phrase before attempting to match
        clean_phrase = normalizer(phrase)
        # Count each instance of the phrase found
        occurrences = message.count(clean_phrase)
        # Add a point for each hit detected
        scam_score += occurrences
        # If matches occurred, record phrase + count
        if occurrences > 0:
            hits.append((phrase, occurrences))

    # Return score and hits after scanning all phrases
    return scam_score, hits


# Function to clean messages before scanning
def normalizer(message):
    """
    Normalizes text by converting to lower case, replacing punctuation with spaces,
    and collapsing extra whitespace into single spaces. This creates a consistent
    format for comparing trigger phrases against user input.

    Parameters:
        message (str): The input text to be normalized.

    Variables:
        punctuation (list): Characters to replace with whitespace.
        ch (str): A single punctuation character from the punctuation list.

    Logic:
        1. Convert the message to lower case.
        2. Replace each punctuation symbol in the list with a space.
        3. Collapse all extra whitespace into single spaces.
        4. Return the cleaned message.

    Return:
        str: The normalized version of the input message.
    """
    # Convert to lower case
    message = message.lower()

    # Establish a list of punctuation symbols
    punctuation = [".", ",", "!", "?", ":", ";", "'", "\"", "(", ")", "[", "]",
                   "{", "}", "-", "_", "/", "\\", "@", "#", "$", "%", "&", "*",
                   "+", "=", "<", ">", "|", "~", "`", "’", "“", "”"]
    # Replace symbols with whitespace
    for ch in punctuation:
        message = message.replace(ch, " ")

    # Collapse white space
    message = " ".join(message.split())
    # Send cleaned message back to call point
    return message


def auditor(score):
    """
    Rates the likelihood that a message is spam based on its spam score.

    Parameters:
        score (int): Total spam score returned by the scanner function.

    Logic:
        1. If score is 0, message is likely safe.
        2. If score is 1, message might be spam.
        3. If score is 2, message is probably spam.
        4. If score is 3 or higher, message is very likely spam.

    Return:
        str: A spam likelihood rating message.
    """
    if score == 0:
        return "This message looks safe."
    elif score == 1:
        return "This message might be spam."
    elif score == 2:
        return "This message is probably spam."
    else:
        return "Call up the Prince of Nigeria, because this is spam."


# List of spammy phrases to monitor for
triggers = [
    "Act Now",
    "Urgent",
    "Immediate Action Required",
    "Limited Time",
    "Last Chance",
    "Final Notice",
    "Account Suspended",
    "Unusual Activity Detected",
    "Today Only",
    "Winner",
    "You Are A Winner",
    "You Have Been Selected",
    "Congratulations",
    "Claim Your Prize",
    "Free",
    "100% Free",
    "Risk-Free",
    "Guaranteed",
    "Financial Freedom",
    "Earn $$$ Fast",
    "Double Your Income",
    "Work From Home",
    "Be Your Own Boss",
    "No Credit Check",
    "Cash Bonus",
    "Pure Profit",
    "This Isn’t A Scam",
    "Dear Friend",
    "Verify Your Account",
    "Once In A Lifetime"
]


if __name__ == "__main__":
    prompter()
