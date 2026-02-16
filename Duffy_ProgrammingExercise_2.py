# Function to recieve input and give output
def prompter():
    # Read input from the user
    message = input("Enter your message: ")
    # Clean the input before scanning
    clean_message = normalizer(message)

    # Print the cleaned message for construction purposes
    print(clean_message)

    # Pass message to the scanner function
    scanner(message)

# Function that prefers the inspection
def scanner(message):
    # Initialize counter
    scam_score = 0
    # Loop through the 30 phrases
    for phrase in triggers:
        # Count each instance of the phrase found
        occurrences = message.count(phrase)
        # Check if phrase matches message
        if triggers in message:
            # If it does, add a point
            scam_score += 1

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