import os
import io
import pypdf
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- FOLDER CONFIGURATION ---
KNOWLEDGE_BASE_DIR = "knowledge_base"
# This variable will hold all the text from your PDFs
static_pdf_context = ""

def load_all_pdfs():
    global static_pdf_context
    if not os.path.exists(KNOWLEDGE_BASE_DIR):
        os.makedirs(KNOWLEDGE_BASE_DIR)
        print(f"⚠️ Created '{KNOWLEDGE_BASE_DIR}' folder. Put your PDFs there!")
        return

    combined_text = ""
    for filename in os.listdir(KNOWLEDGE_BASE_DIR):
        if filename.endswith(".pdf"):
            print(f"📖 Reading: {filename}...")
            path = os.path.join(KNOWLEDGE_BASE_DIR, filename)
            try:
                reader = pypdf.PdfReader(path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        combined_text += text + "\n"
            except Exception as e:
                print(f"❌ Could not read {filename}: {e}")
    
    static_pdf_context = combined_text
    print("✅ Knowledge Base Loaded.")

# Run the loader once when the server starts
load_all_pdfs()

# --- GEMINI SETUP ---
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get('query')
    
    # We combine the folder text with any new text from the browser
    browser_context = data.get('context', "")
    full_context = static_pdf_context + "\n" + browser_context

    prompt = f"""
    You are Bubloo Scientist. Answer the question using ONLY the provided context.
    Context: {full_context}
    Question: {user_query}
    """
    
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
