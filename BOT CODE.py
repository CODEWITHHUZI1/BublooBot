import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure Gemini with your key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# Temporary storage for PDF text
pdf_context = {}

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    
    # Using a simple library like pypdf to extract text for the context
    import pypdf
    import io
    
    reader = pypdf.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return jsonify({"text": text, "filename": file.name})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get('query')
    context = data.get('context') # This is the text from all uploaded PDFs

    prompt = f"""
    You are a Lab Assistant. Use the following PDF context to answer the user.
    If the answer isn't in the context, say you don't know based on the documents.
    
    Context:
    {context}
    
    User Question: {user_query}
    """
    
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
