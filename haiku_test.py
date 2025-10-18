from openai import OpenAI

client = OpenAI()  # Uses OPENAI_API_KEY from your environment variable

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a haiku about a calm morning."
)

print(response.output_text)
