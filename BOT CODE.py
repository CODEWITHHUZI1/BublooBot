"""
server.py - Enhanced Python Flask Backend for Gemini AI Chatbot with Quiz Mode
This keeps your API key secure and manages PDF knowledge base + Quiz Generation
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
import os
from pathlib import Path
import base64
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
PDF_DIR = Path(__file__).parent / 'knowledge_base'
PORT = int(os.getenv('PORT', 3000))

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Model configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name='gemini-2.0-flash-exp',
    generation_config=generation_config
)

# Quiz topics by difficulty and category
QUIZ_TOPICS = {
    'easy': {
        'physics': ['States of matter', 'Simple machines', 'Basic forces', 'Light and sound'],
        'chemistry': ['Elements and compounds', 'States of water', 'Basic acids and bases'],
        'biology': ['Cell structure', 'Food chains', 'Plant parts', 'Animal groups'],
        'astronomy': ['Solar system basics', 'Moon phases', 'Day and night'],
        'geography': ['Continents', 'Oceans', 'Basic landforms', 'Cardinal directions'],
        'world-history': ['Ancient civilizations basics', 'Famous explorers', 'Medieval period'],
        'sports-general': ['Popular sports', 'Basic rules', 'Famous athletes'],
        'technology': ['Computer basics', 'Internet basics', 'Simple inventions']
    },
    'medium': {
        'physics': ['Newton\'s laws', 'Energy transfer', 'Electromagnetic spectrum', 'Waves'],
        'chemistry': ['Chemical bonds', 'Periodic table trends', 'Chemical reactions', 'pH scale'],
        'biology': ['Mitosis and meiosis', 'DNA and RNA', 'Cellular respiration', 'Evolution'],
        'astronomy': ['Star life cycles', 'Galaxy types', 'Space missions', 'Planets'],
        'geography': ['Climate zones', 'Mountain ranges', 'Rivers', 'Country capitals'],
        'world-history': ['World wars', 'Industrial revolution', 'Renaissance', 'Colonialism'],
        'modern-history': ['Cold War', 'Independence movements', 'Space race', 'Digital age'],
        'sports-general': ['Olympic history', 'Sports records', 'Tournament formats'],
        'football': ['FIFA World Cup', 'Famous players', 'League systems'],
        'cricket': ['Cricket formats', 'Famous players', 'World Cup history']
    },
    'hard': {
        'physics': ['Quantum mechanics', 'Relativity', 'Nuclear physics', 'Thermodynamics'],
        'chemistry': ['Organic reactions', 'Molecular geometry', 'Electrochemistry', 'Biochemistry'],
        'biology': ['Genetic engineering', 'Molecular biology', 'Evolutionary biology', 'Neuroscience'],
        'astronomy': ['Black holes', 'Dark matter', 'Cosmology', 'Exoplanets'],
        'modern-science': ['CRISPR', 'Quantum computing', 'AI breakthroughs', 'Climate science'],
        'geography': ['Plate tectonics', 'Geographic theories', 'Climate patterns', 'Geopolitics'],
        'modern-history': ['Globalization', 'Technological revolutions', 'Modern conflicts', '21st century politics'],
        'discoveries': ['Recent scientific breakthroughs', 'Space discoveries', 'Medical advances'],
        'space-exploration': ['Mars missions', 'James Webb telescope', 'ISS', 'SpaceX achievements'],
        'olympics': ['Olympic records', 'Memorable moments', 'Host cities history'],
        'technology': ['AI development', 'Blockchain', 'Quantum computing', 'Biotechnology']
    }
}


def ensure_pdf_dir():
    """Create PDF directory if it doesn't exist"""
    PDF_DIR.mkdir(exist_ok=True)
    print(f"📁 PDF directory: {PDF_DIR}")


def load_pdfs():
    """Load all PDFs from the pdfs directory"""
    try:
        pdf_files = list(PDF_DIR.glob('*.pdf'))
        pdfs = []

        for pdf_path in pdf_files:
            with open(pdf_path, 'rb') as f:
                pdf_data = base64.b64encode(f.read()).decode('utf-8')
                pdfs.append({
                    'name': pdf_path.name,
                    'data': pdf_data,
                    'mime_type': 'application/pdf'
                })

        return pdfs
    except Exception as e:
        print(f"❌ Error loading PDFs: {e}")
        return []


def build_pdf_context():
    """Build context from PDFs for Gemini"""
    pdfs = load_pdfs()

    if not pdfs:
        return None

    # Convert PDFs to Gemini format
    pdf_parts = []
    for pdf in pdfs:
        pdf_parts.append({
            'mime_type': pdf['mime_type'],
            'data': pdf['data']
        })

    return {
        'pdfs': pdf_parts,
        'count': len(pdfs),
        'names': [p['name'] for p in pdfs]
    }


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        message = data.get('message')
        history = data.get('history', [])

        if not message:
            return jsonify({'error': 'Message is required'}), 400

        # Load PDF context
        pdf_context = build_pdf_context()

        # Build conversation history for Gemini
        chat_history = []
        for msg in history:
            role = 'user' if msg.get('role') == 'user' else 'model'
            parts = msg.get('parts', [{'text': msg.get('content', '')}])
            chat_history.append({
                'role': role,
                'parts': parts
            })

        # Start chat with history
        chat_session = model.start_chat(history=chat_history)

        # Build prompt with PDF context
        if pdf_context and pdf_context['pdfs']:
            system_context = f"""You are a helpful AI assistant for Bubloo Scientist website. You have access to {pdf_context['count']} PDF document(s): {', '.join(pdf_context['names'])}. 

IMPORTANT INSTRUCTIONS:
1. Answer questions PRIMARILY based on the information in these PDFs
2. If the information is in the PDFs, cite it and use it
3. If the information is NOT in the PDFs, you can use your general knowledge but mention that you're using general knowledge
4. Be helpful, accurate, and conversational
5. Focus on science topics: Physics, Chemistry, Biology, and related subjects

User question: {message}"""

            # Build parts with PDFs
            parts = []
            for pdf in pdf_context['pdfs']:
                parts.append({
                    'inline_data': {
                        'mime_type': pdf['mime_type'],
                        'data': pdf['data']
                    }
                })
            parts.append({'text': system_context})

            # Send message
            response = chat_session.send_message(parts)

            return jsonify({
                'response': response.text,
                'pdfCount': pdf_context['count'],
                'pdfNames': pdf_context['names']
            })
        else:
            # No PDFs - general conversation
            system_prompt = f"""You are a helpful AI assistant for Bubloo Scientist website specializing in science topics (Physics, Chemistry, Biology, etc.). 

Note: No PDF documents are currently loaded. You can answer using your general knowledge about science.

User question: {message}"""

            response = chat_session.send_message(system_prompt)

            return jsonify({
                'response': response.text,
                'pdfCount': 0,
                'note': 'Using general knowledge (no PDFs loaded)'
            })

    except Exception as e:
        print(f"❌ Error in chat endpoint: {e}")

        if 'API_KEY' in str(e):
            return jsonify({
                'error': 'API key not configured. Please set GEMINI_API_KEY in .env file'
            }), 500

        return jsonify({
            'error': str(e) or 'Failed to generate response'
        }), 500


@app.route('/api/quiz', methods=['POST'])
def generate_quiz():
    """Generate quiz questions"""
    try:
        data = request.get_json()
        difficulty = data.get('difficulty', 'medium')
        topic = data.get('topic', None)
        
        # Validate difficulty
        if difficulty not in ['easy', 'medium', 'hard']:
            difficulty = 'medium'
        
        # Select topic
        if not topic:
            topic = random.choice(QUIZ_TOPICS[difficulty])
        
        # Generate quiz question
        prompt = f"""Generate a multiple-choice science quiz question about {topic} with {difficulty} difficulty.

STRICT FORMAT REQUIREMENT - Follow this EXACT format:
QUESTION: [Write a clear, specific question here]
A) [First option]
B) [Second option]
C) [Third option]
D) [Fourth option]
CORRECT: [Single letter: A, B, C, or D]
EXPLANATION: [Write a 2-3 sentence explanation of why the correct answer is right and what makes it important]

REQUIREMENTS:
- Question should be {difficulty} level in complexity
- All options should be plausible but only one correct
- Explanation should be educational and clear
- Topic: {topic}
- For EASY: Basic concepts, simple terminology
- For MEDIUM: Require understanding of concepts and relationships
- For HARD: Advanced knowledge, complex principles

Do NOT include any other text, markdown, or formatting. Follow the format exactly."""

        # Generate using Gemini
        response = model.generate_content(prompt)
        
        return jsonify({
            'quiz': response.text,
            'topic': topic,
            'difficulty': difficulty
        })
        
    except Exception as e:
        print(f"❌ Error in quiz endpoint: {e}")
        return jsonify({
            'error': str(e) or 'Failed to generate quiz'
        }), 500


@app.route('/api/quiz/custom', methods=['POST'])
def generate_custom_quiz():
    """Generate custom quiz based on user request"""
    try:
        data = request.get_json()
        user_request = data.get('request', '')
        difficulty = data.get('difficulty', 'medium')
        
        if not user_request:
            return jsonify({'error': 'Quiz request is required'}), 400
        
        # Generate quiz based on user's custom request
        prompt = f"""The user wants a quiz about: "{user_request}"
Difficulty: {difficulty}

Generate a multiple-choice science quiz question following this EXACT format:
QUESTION: [Write a clear, specific question here]
A) [First option]
B) [Second option]
C) [Third option]
D) [Fourth option]
CORRECT: [Single letter: A, B, C, or D]
EXPLANATION: [Write a 2-3 sentence explanation of why the correct answer is right]

REQUIREMENTS:
- Question should be {difficulty} level
- Must be related to science (Physics, Chemistry, Biology, etc.)
- All options should be plausible
- Include educational explanation

Do NOT include any other text or formatting."""

        response = model.generate_content(prompt)
        
        return jsonify({
            'quiz': response.text,
            'topic': user_request,
            'difficulty': difficulty
        })
        
    except Exception as e:
        print(f"❌ Error in custom quiz endpoint: {e}")
        return jsonify({
            'error': str(e) or 'Failed to generate custom quiz'
        }), 500


@app.route('/api/pdfs', methods=['GET'])
def list_pdfs():
    """List all loaded PDFs"""
    try:
        pdfs = load_pdfs()
        return jsonify({
            'count': len(pdfs),
            'files': [{'name': p['name']} for p in pdfs]
        })
    except Exception as e:
        return jsonify({'error': 'Failed to list PDFs'}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Gemini AI Server is running',
        'apiKeyConfigured': bool(GEMINI_API_KEY),
        'features': ['chat', 'quiz', 'pdf-knowledge-base']
    })


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files (HTML, CSS, JS)"""
    return send_from_directory('.', path)


@app.route('/')
def index():
    """Serve the main chatbot HTML"""
    # Try enhanced version first
    if os.path.exists('chatbot-gemini-enhanced.html'):
        return send_from_directory('.', 'chatbot-gemini-enhanced.html')
    return send_from_directory('.', 'chatbot-gemini.html')


if __name__ == '__main__':
    # Startup
    ensure_pdf_dir()
    pdf_context = build_pdf_context()

    print('╔═══════════════════════════════════════════════════════════╗')
    print('║       🤖 BUBLOO SCIENTIST AI LAB ASSISTANT v2.0          ║')
    print('║              with QUIZ MODE enabled                       ║')
    print('╚═══════════════════════════════════════════════════════════╝')
    print('')
    print(f'🚀 Server running on http://localhost:{PORT}')
    print(f'🔐 Gemini API Key: {"✓ Configured" if GEMINI_API_KEY else "✗ Missing"}')
    print(f'📄 PDFs loaded: {pdf_context["count"] if pdf_context else 0}')

    if pdf_context and pdf_context['count'] > 0:
        print(f'📚 Files: {", ".join(pdf_context["names"])}')
    else:
        print('💡 Add PDFs to ./knowledge_base/ directory to enable PDF-based responses')

    print('')
    print('🎮 FEATURES:')
    print('   ├─ AI Chat Assistant')
    print('   ├─ Quiz Mode (Easy/Medium/Hard)')
    print('   ├─ PDF Knowledge Base')
    print('   └─ Custom Quiz Generation')
    print('')
    print('───────────────────────────────────────────────────────────')

    # Run server
    app.run(host='0.0.0.0', port=PORT, debug=True)
