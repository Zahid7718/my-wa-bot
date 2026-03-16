import os
from flask import Flask

app = Flask(__name__)

# آپ کے بوٹ کی پہچان
AGENT_NAME = "IQLEEM"

@app.route('/')
def home():
    return f"Welcome! I am {AGENT_NAME}, your AI Agent. I am running and ready."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"{AGENT_NAME} is starting on port {port}...")
    app.run(host='0.0.0.0', port=port)
