import re
import random
import sys

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm a bot, but I'm functioning well!", "Doing great, how about you?"],
    "what did you eat today": ["I don't eat, but I did consume some data!", "Bots don't eat, but thanks for asking!"]
}

def unknown():
    responses_unknown = [
        "I didn't understand that.",
        "Can you rephrase that?",
        "I'm not sure how to respond to that."
    ]
    return random.choice(responses_unknown)

def get_response(user_input):
    user_input = user_input.lower()
    highest_match = 0
    best_response = None
    
    for prompt, replies in responses.items():
        pattern_words = prompt.split()
        matches = 0
        for word in pattern_words:
            if re.search(r'\\b' + re.escape(word) + r'\\b', user_input):
                matches += 1
        match_percentage = matches / len(pattern_words)
        
        if match_percentage > highest_match:
            highest_match = match_percentage
            best_response = random.choice(replies)
    
    if highest_match == 0:
        return unknown()
    else:
        return best_response

def main():
    print("Chatbot: Hello! Type something to begin, or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            sys.exit()
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
