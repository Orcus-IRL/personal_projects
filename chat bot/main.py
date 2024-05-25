import openai

openai.api_key = "your api key"


def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{
            "role": "user", "content": prompt
        }]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("Hello sir, How may I help you today?: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break

        response = chat(user_input)
        print("ChatTPG: ", response)
