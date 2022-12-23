import openai

# Set the API key for your OpenAI account
openai.api_key_path = "/path/to/openai/key"

prompt = input("User: ")

# Loop indefinitely to continue the conversation
while True:
    # Use the openai library to generate a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=3800,
        temperature=0.7
    )

    # Print the response
    response_text = response["choices"][0]["text"]
    print(f"Bot: {response_text.strip()}\n")

    # Get the user's input
    user_input = input("User: ")

    # Check if the user's input is "exit" and exit the script if it is
    if user_input.lower() == "exit":
        break

    # Update the prompt with the user's input
    prompt = f"{response_text.strip()}\nUser: {user_input}"
