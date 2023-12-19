import difflib
import pandas as pd

# Function to load data from an Excel file
def load_data(file_path):
    df = pd.read_excel(file_path, header=None)
    qa_list = [{"user": row[0], "bot": row[1]} for index, row in df.iterrows()]
    return qa_list

# Define the path to the Excel file
excel_file_path = 'chatbot_data.xlsx'

# Load the predefined questions and answers from the Excel file
qa_list = load_data(excel_file_path)

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

