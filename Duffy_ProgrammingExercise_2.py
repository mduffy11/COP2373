# Function to recieve input and give output
def prompter():
    # Read input from the user
    message = input("Enter your message: ")
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