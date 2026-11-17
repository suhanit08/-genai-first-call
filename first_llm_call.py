
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain Generative AI in simple terms in three bullet points."
)

# Display AI response
print(response.output_text)
