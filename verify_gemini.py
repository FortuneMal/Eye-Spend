import os
import toml
import google.generativeai as genai
from PIL import Image
import json

# Load API Key
api_key = os.environ.get("API_KEY")
if not api_key:
    try:
        secrets = toml.load(".streamlit/secrets.toml")
        api_key = secrets.get("GEMINI_API_KEY")
    except Exception as e:
        print(f"Error loading secrets: {e}")

if not api_key:
    print("API Key not found!")
    exit(1)

print(f"API Key found: {api_key[:5]}...")

genai.configure(api_key=api_key)
model_name = 'gemini-1.5-flash'
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods and 'flash' in m.name:
            model_name = m.name
            break
except:
    pass
print(f"Using model: {model_name}")
model = genai.GenerativeModel(model_name)

image_path = "C:/Users/keepk/.gemini/antigravity/brain/4646e856-fcb1-4a3f-a91f-85aad337e683/uploaded_image_1764317935307.png"

if not os.path.exists(image_path):
    print(f"Image not found at {image_path}")
    # Try to find it in the current directory or artifacts
    # For now, just exit if not found
    exit(1)

print(f"Analyzing image: {image_path}")
image = Image.open(image_path)

prompt = """
Analyze this receipt image and extract the following details into a JSON object:
- vendor: The name of the merchant.
- date: The date of the transaction in YYYY-MM-DD format. If not found, use today's date.
- amount: The total amount of the transaction as a number (float).
- category: The expense category (e.g., Meals, Travel, Office Supplies, Entertainment, Software, Groceries).
- risk_score: A score from 0 to 100 indicating the risk level of this expense (0 is safe, 100 is high risk).
- risk_reason: A brief explanation for the assigned risk score.

Return ONLY the raw JSON string, no markdown formatting.
"""

try:
    response = model.generate_content([prompt, image])
    print("Raw Response:")
    print(response.text)
    
    response_text = response.text.strip()
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
        
    data = json.loads(response_text)
    print("\nParsed Data:")
    print(json.dumps(data, indent=2))
    
except Exception as e:
    print(f"Error: {e}")
    print("Listing available models:")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods and 'flash' in m.name:
                print(m.name)
    except Exception as list_e:
        print(f"Could not list models: {list_e}")
