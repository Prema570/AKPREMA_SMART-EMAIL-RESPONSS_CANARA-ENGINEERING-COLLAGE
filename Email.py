import openai
import os

# Load the OpenAI API key from the environment variable
openai.api_key = ("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")


# Function to generate email response using OpenAI's API
def generate_email_response(client_input):
    # Define the prompt to guide OpenAI's API
    prompt = f"""
    A client has contacted you with the following details:

    {client_input}

    Your task is to generate a professional, friendly, and human-like email response to the client.
    The response should:
    - Acknowledge the client's message and show appreciation for their input.
    - Address specific details such as the number of pages, filters, and functionality requirements.
    - Mention the client's budget in a polite way and offer further discussion if necessary.
    - Avoid generic phrases like "I hope this email finds you well."
    - The tone should be professional, yet approachable and natural.

    Please generate a polished, human-sounding email response.
    """

    # Call OpenAI API to generate the response
    response = openai.Completion.create(
        model="text-davinci-003",  # You can use a different model if preferred
        prompt=prompt,
        max_tokens=250,  # Limit the response length
        temperature=0.7  # Adjust creativity (higher = more creative)
    )

    # Extract and return the response from the API
    return response.choices[0].text.strip()


# Example client input
client_input = """
From Name: Jesna 
Client First Name: Geminas 
Client Last Name: Ket 
Client Email: GeminasKet@gmail.com 
Client Country: Romania 
Client Location (if provided): Romania 
Client Language: English 
Project Type: Content with Databases 
Service Category: Web Development 
Client Website (if any): No 
Additional Information (if any):
"I need 4 dynamic pages for a real estate Web-application: one each for apartments, 
houses, business centres, and land. I need 2 filters for 'for sale' and 'for rent,' 
and they should be connected. Don't bother with the design; I'll handle that. I just 
need the functionality. The budget should be $100000. Thank you!"
"""

# Generate the email response
email_response = generate_email_response(client_input)

# Print the generated response
print(email_response)
