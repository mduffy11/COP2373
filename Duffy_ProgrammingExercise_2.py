# Function to recieve input and give output
def prompter():
    # Read input from the user
    message = input("Enter your message: ")
    # Clean the input before scanning
    clean_message = normalizer(message)

    # Pass message to the scanner function for scoring
    # (Change) scanner now returns a tuple: (score, hits)
    score, hits = scanner(clean_message)

    # Print rating
    rating = auditor(score)
    print("The results are in: ", rating)

    # (Added) Display the words/phrases which caused it to be spam
    if len(hits) > 0:
        print("Matched phrases:")
        for phrase, occurrences in hits:
            print(f"- {phrase} ({occurrences})")
    else:
        print("Matched phrases: None")


# Function that prefers the inspection
def scanner(message):
    # Initialize counter
    scam_score = 0
    # (Added) Create a list of phrases that were matched
    hits = []
    # Loop through the 30 phrases
    for phrase in triggers:
        # Clean the phrase before attempting to match
        clean_phrase = normalizer(phrase)
        # Count each instance of the phrase found
        occurrences = message.count(clean_phrase)
        # Add a point for each hit detected
        scam_score += occurrences
        # (Fixed) If matches occurred, record phrase + count
        if occurrences > 0:
            hits.append((phrase, occurrences))

    # (Fixed) Return score and hits AFTER scanning all phrases
    return scam_score, hits


# Function to clean messages before scanning
def normalizer(message):
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
    if score == 0:
        return "This message looks safe"
    elif score == 1:
        return "This message might be spam"
    elif score == 2:
        return "This message is probably spam"
    elif score == 3:
        return "This message is almost certainly spam"
    else:
        return "Call up the Prince of Nigeria, because this is spam"


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

prompter()
