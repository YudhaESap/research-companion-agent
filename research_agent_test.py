from openai import OpenAI

# Initialize client (using environment variable)
client = OpenAI()

# Example research abstract
abstract = """
A prospective cohort study of 150 patients with colorectal cancer was conducted 
to examine the association between depression and cancer outcomes. 
Patients were aged 45–75, 60% male and 40% female.
"""

# Ask GPT to extract structured info
prompt = f"""
Extract the following from the abstract:
1. Study design
2. Sample size
3. Population (age, sex)
4. Key outcomes

Return as JSON only.

Abstract:
{abstract}
"""

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

# Print structured output
print(response.output_text)
