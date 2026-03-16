print("WhatsApp Bot is starting...")
import os

# ہم یہاں آپ کی اوپن راؤٹر کی چابی استعمال کریں گے
api_key = os.getenv("OPENROUTER_API_KEY")

if api_key:
    print("AI Brain is connected!")
else:
    print("API Key missing!")
  
