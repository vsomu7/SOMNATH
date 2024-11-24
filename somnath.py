import streamlit as st
import requests
import json

# Azure OpenAI resource details
RESOURCE_ENDPOINT = "https://w2403-m3uiakgy-swedencentral.cognitiveservices.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01"
API_KEY = "2uMq4tqafnMsNMo3nez8n8kKR0eRR5N9Fipr1BkTmBUathRJxw7jJQQJ99AKACfhMk5XJ3w3AAAAACOGUvYl"  # Keep this secure

def generate_image(prompt):
    """
    Generate an image from a text prompt using Azure OpenAI's DALL·E 3.

    Args:
        prompt (str): The text description for the image.

    Returns:
        str: URL or path to the generated image.
    """
    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    # Payload with prompt and settings
    payload = {
        "prompt": prompt,
        "n": 1,  # Number of images to generate
        "size": "1024x1024"  # Supported sizes: "256x256", "512x512", "1024x1024"
    }

    try:
        # Make a POST request to the Azure OpenAI API
        response = requests.post(RESOURCE_ENDPOINT, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            # Extract image URL from the response
            data = response.json()
            image_url = data["data"][0]["url"]  # Get the first image URL
            return image_url
        else:
            st.error(f"Failed to generate image. Status Code: {response.status_code}")
            st.error(f"Response: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit App UI
st.title("AI-Driven Augmented Reality Image Composer: Real-Time Scene Augmentation Based on Text Prompts")

# Input for the prompt
prompt_text = st.text_input("Enter a prompt for image generation", "")

# Button to generate image
if st.button("Generate Image"):
    if prompt_text:
        # Generate image when a prompt is provided
        st.write("Generating your image, please wait...")
        image_url = generate_image(prompt_text)

        if image_url:
            # Display the generated image
            st.image(image_url, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt before clicking the 'Generate Image' button.")
