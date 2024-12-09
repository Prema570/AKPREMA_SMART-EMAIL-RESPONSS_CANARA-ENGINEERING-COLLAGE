import requests
import json
import time

# Define the OpenAI API key (Replace with your actual API key)
OPENAI_API_KEY = "sk-proj-<JCFFOrLwpZ2P6BZZGVmneqYZ7srUGJYBBqU82nEgvczq_HU1hTjnsSiYVin6aFpnVkxm60_0zpT3BlbkFJQJ37znlhPlBnnKowdj4udw_1seetXeqxNgOC-FCuJQN_-xyfV5t2OtTVT1ScwnTEnkW3AwDQMA>"

# Method to interact with OpenAI's API for dynamic response generation
def generate_email_response_with_ml(client_info):
    # Compose the input for OpenAI's API based on the client's data
    prompt = f"""
    Generate a professional email response to a client named {client_info['first_name']} {client_info['last_name']}, 
    who is working on a {client_info['project_type']} project in the {client_info['service_category']} category. 
    The project is located in {client_info['location']}, {client_info['country']}. 
    The client speaks {client_info['language']} and provided the following details: 
    Website: {client_info['website']}, Additional Info: {client_info['additional_info']}. 
    Make sure the response is personalized, context-aware, and does not follow a rigid template. 
    It should encourage further conversation and show professionalism.
    """
    
    # Call OpenAI's API for dynamic response generation
    return call_openai_api(prompt)

# Method to call OpenAI's API with retry mechanism
def call_openai_api(prompt):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 150
    }

    retries = 3  # Set number of retries
    for i in range(retries):
        try:
            # Send the request to OpenAI
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise error for bad responses
            
            # Parse and return the response from OpenAI
            response_json = response.json()
            return response_json['choices'][0]['text'].strip()
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed, attempt {i+1}/{retries}: {e}")
            if i < retries - 1:
                time.sleep(2)  # Wait 2 seconds before retrying
            else:
                print("All retries failed.")
                raise

# Method to handle mistakes input and improve responses (separate from prompt)
def handle_mistakes(mistake_input):
    # Process mistake and feedback (print feedback for now)
    print(f"Mistake Feedback received: {mistake_input}")

# Main function to gather client information and generate email response
def main():
    try:
        # Gather client information
        client_info = {}

        print("Please provide the following client details to generate a response:")

        client_info['first_name'] = input("Client First Name: ").strip()
        client_info['last_name'] = input("Client Last Name: ").strip()
        client_info['email'] = input("Client Email: ").strip()
        client_info['country'] = input("Client Country: ").strip()
        client_info['location'] = input("Client Location (if provided): ").strip() or "Not provided"
        client_info['language'] = input("Client Language: ").strip()
        client_info['project_type'] = input("Project Type: ").strip()
        client_info['service_category'] = input("Service Category: ").strip()
        client_info['website'] = input("Client Website (if any): ").strip() or "None"
        client_info['additional_info'] = input("Additional Information (if any): ").strip() or "No additional information provided."

        # Generate the email response using OpenAI's API
        email_response = generate_email_response_with_ml(client_info)

        # Output the response
        print("\nGenerated Email Response:")
        print(email_response)

        # Handle mistakes feedback (optional)
        feedback_response = input("\nWould you like to provide any feedback for improvements? (Yes/No): ").strip()
        if feedback_response.lower() == "yes":
            mistake_input = input("Please provide your feedback: ").strip()
            handle_mistakes(mistake_input)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
