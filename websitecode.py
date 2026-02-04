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

# --- NEW: AUTO-LOAD PDF FOLDER ---
KNOWLEDGE_BASE_DIR = "knowledge_base"
global_pdf_context = ""

def load_static_pdfs():
    global global_pdf_context
    if not os.path.exists(KNOWLEDGE_BASE_DIR):
        os.makedirs(KNOWLEDGE_BASE_DIR)
        print(f"Created folder: {KNOWLEDGE_BASE_DIR}. Add your PDFs there!")
        return

    combined_text = ""
    for filename in os.listdir(KNOWLEDGE_BASE_DIR):
        if filename.endswith(".pdf"):
            print(f"📖 Pre-loading: {filename}")
            path = os.path.join(KNOWLEDGE_BASE_DIR, filename)
            reader = pypdf.PdfReader(path)
            for page in reader.pages:
                combined_text += page.extract_text() + "\n"
    
    global_pdf_context = combined_text
    print("✅ All PDFs loaded into memory.")

# Load the PDFs right when the script starts
load_static_pdfs()
# --------------------------------

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get('query')
    
    # We combine the pre-loaded PDFs with any text sent from the browser
    browser_context = data.get('context', "")
    full_context = global_pdf_context + "\n" + browser_context

    prompt = f"Use this knowledge to answer: {full_context}\n\nUser: {user_query}"
    
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
