import difflib
import json

# Function to load data from a JSON file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Define the path to the JSON file
json_file_path = 'universal_bot.json'

# Load the predefined questions and answers from the JSON file
qa_list = load_data(json_file_path)

# Function to get the most suitable answer
def get_most_suitable_answer(user_input):
    # Use difflib to find the most similar question in the predefined list
    similarity_scores = [(difflib.SequenceMatcher(None, user_input, qa["user"]).ratio(), qa["bot"]) for qa in qa_list]
    most_suitable_answer = max(similarity_scores, key=lambda x: x[0])

    # Check if the similarity score is below a certain threshold (adjust as needed)
    if most_suitable_answer[0] < 0.6:
        return "I didn't understand that"
    
    return most_suitable_answer[1]

# Interaction loop
while True:
    # Get user input
    user_prompt = input("\nYou: ")

    # Check for exit condition
    if user_prompt.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    # Get the most suitable answer
    bot_response = get_most_suitable_answer(user_prompt)

    # Print the bot's response
    print("Bot:", bot_response)
