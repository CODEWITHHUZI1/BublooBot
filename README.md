# 🧪 Bubloo Scientist AI Lab Assistant - Enhanced Edition

A **legendary, cyber-futuristic AI chatbot** with Quiz Mode, powered by Google's Gemini AI. Features a stunning glassmorphic UI with neon effects, holographic elements, and smooth animations.

![Version](https://img.shields.io/badge/version-2.0-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-red)
![Gemini](https://img.shields.io/badge/Gemini-AI-purple)

## ✨ Features

### 🎨 **Legendary UI/UX**
- **Cyber-Futuristic Design** with neon glow effects
- **Glassmorphism** with advanced backdrop blur
- **Holographic Elements** and animated particles
- **Smooth Animations** with custom easing functions
- **Scanline Effects** for that authentic cyber feel
- **Custom Orbitron & Rajdhani** fonts for a tech-forward look
- **Maximize/Minimize** - Full-screen or compact mode
- **Delete Messages** - Remove bot responses with hover delete button

### 🤖 **AI Capabilities**
- **Intelligent Chatbot** powered by Gemini 2.0 Flash
- **PDF Knowledge Base** - Upload PDFs and the AI learns from them
- **Context-Aware** responses with conversation history
- **Multi-Subject Expertise** - Science, Geography, History, Sports, and more

### 🎓 **Enhanced Quiz Mode**
- **5 Questions Per Session** - Complete quiz sets with scoring
- **Three Difficulty Levels**: Easy, Medium, Hard
- **15+ Topic Categories**:
  - 🔬 Science: Physics, Chemistry, Biology, Astronomy, Modern Science
  - 🌍 Geography & History: World Geography, World History, Modern History, Discoveries
  - ⚽ Sports: General Sports, Olympics, Football, Cricket
  - 💻 Technology: Tech Innovations, Space Exploration, Inventions
- **Topic Selection** - Choose specific categories before starting
- **Progress Tracking** - See your score as you progress (e.g., "Score: 3/5")
- **Auto-Generated Questions** on various topics
- **Multiple Choice Format** with explanations
- **Interactive UI** with correct/incorrect animations
- **Instant Feedback** with educational explanations
- **Final Score Display** with personalized messages

### 🔥 **Enhanced Features**
- **Dual Mode Toggle** - Switch between Chat and Quiz modes
- **Real-time Status** indicators
- **Message Timestamps**
- **Typing Indicators** with animated dots
- **Sample Questions** for quick starts
- **Clear Chat** functionality
- **Responsive Design** - Works on all devices

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- Modern web browser

## 🚀 Quick Start

### 1. Clone or Download

```bash
# Create project directory
mkdir bubloo-scientist-ai
cd bubloo-scientist-ai
```

### 2. Install Dependencies

```bash
pip install flask flask-cors python-dotenv google-generativeai
```

### 3. Setup Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=3000
```

**Get your Gemini API Key:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy and paste it into your `.env` file

### 4. Create Knowledge Base Directory

```bash
mkdir knowledge_base
```

(Optional) Add PDF files to this directory for the AI to learn from.

### 5. Add Project Files

Place these files in your project directory:
- `server-enhanced.py` - Backend server
- `chatbot-gemini-enhanced.html` - Frontend UI

### 6. Run the Server

```bash
python server-enhanced.py
```

You should see:
```
╔═══════════════════════════════════════════════════════════╗
║       🤖 BUBLOO SCIENTIST AI LAB ASSISTANT v2.0          ║
║              with QUIZ MODE enabled                       ║
╚═══════════════════════════════════════════════════════════╝

🚀 Server running on http://localhost:3000
🔐 Gemini API Key: ✓ Configured
📄 PDFs loaded: 0
```

### 7. Open in Browser

Navigate to: `http://localhost:3000`

## 📖 Usage Guide

### Chat Mode

1. **Click the floating bot button** (bottom-right)
2. **Type your question** about any topic
3. **Press Enter** or click send
4. **Delete bot messages** by hovering over them and clicking the trash icon
5. **Maximize** the chat window for full-screen experience
6. Get instant AI-powered responses!

**Sample Questions:**
- "What is quantum physics?"
- "Tell me about the French Revolution"
- "Who won the last FIFA World Cup?"
- "What are the tallest mountains?"

### Quiz Mode

1. **Click the graduation cap icon** in the header
2. **Select a topic category** from the dropdown:
   - 🔬 Science subjects
   - 🌍 Geography & History
   - ⚽ Sports categories
   - 💻 Technology topics
3. **Choose difficulty level**:
   - 🟢 **Easy** - Basic concepts (5 questions)
   - 🟡 **Medium** - Intermediate knowledge (5 questions)
   - 🔴 **Hard** - Advanced topics (5 questions)
4. **Answer each question** by clicking an option
5. **View explanations** after each answer
6. **Track your progress** - See your current score
7. **Get final results** with personalized feedback
8. **Start new quiz** or **Exit** to chat mode

**Quiz Features:**
- Random topic selection available
- 15+ specialized categories
- Progress tracking (Question 1/5, 2/5, etc.)
- Score display throughout quiz
- Motivational messages based on performance

### Window Controls

- **Maximize** - Click expand icon for full-screen mode
- **Restore** - Click compress icon to return to normal size
- **Minimize** - Close the chat window
- **Clear Chat** - Delete all conversation history

### PDF Knowledge Base

1. Add PDF files to the `knowledge_base/` directory
2. Restart the server
3. The AI will now reference these PDFs in answers
4. Ask questions about the PDF content

## 🎨 UI Features Breakdown

### Color Scheme
- **Primary**: Cyan (#38bdf8) - Neon glow effects
- **Secondary**: Purple (#a855f7) - Accents
- **Background**: Deep dark blues (#0a0e27 → #1a1f3a)
- **Text**: White with subtle shadows

### Typography
- **Titles**: Orbitron (Bold, futuristic)
- **Body**: Rajdhani (Clean, readable)
- **Tracking**: Wide letter spacing for cyber feel

### Animations
- **Float Effect**: Holographic button hover
- **Pulse Cyber**: Status indicators
- **Slide In**: Message animations
- **Glitch**: Title effect
- **Scanline**: Moving scan effect
- **Particles**: Ambient background motion

### Glassmorphism
- **Backdrop Blur**: 20-30px
- **Border**: Subtle cyan glow
- **Shadow**: Layered neon shadows
- **Transparency**: 70-95%

## 🛠️ Configuration

### Change Port

Edit `.env`:
```env
PORT=8080
```

### Adjust AI Settings

Edit `server-enhanced.py`:
```python
generation_config = {
    "temperature": 0.7,      # Creativity (0.0 - 1.0)
    "top_p": 0.9,           # Diversity
    "top_k": 40,            # Sampling
    "max_output_tokens": 2048,  # Response length
}
```

### Modify Quiz Topics

Edit `server-enhanced.py` - `QUIZ_TOPICS` dictionary:
```python
QUIZ_TOPICS = {
    'easy': ['Your topics here'],
    'medium': ['Your topics here'],
    'hard': ['Your topics here']
}
```

## 📁 Project Structure

```
bubloo-scientist-ai/
├── server-enhanced.py              # Flask backend
├── chatbot-gemini-enhanced.html    # Enhanced UI
├── .env                            # Environment variables
├── knowledge_base/                 # PDF storage
│   └── (your PDFs here)
└── README.md                       # This file
```

## 🔧 API Endpoints

### Chat
```
POST /api/chat
{
  "message": "Your question",
  "history": []
}
```

### Quiz Generation
```
POST /api/quiz
{
  "difficulty": "medium",
  "topic": "optional"
}
```

### Custom Quiz
```
POST /api/quiz/custom
{
  "request": "Quiz about genetics",
  "difficulty": "hard"
}
```

### Health Check
```
GET /health
```

### List PDFs
```
GET /api/pdfs
```

## 🎯 Quiz Mode Tips

1. **Choose Your Topic**: Select from 15+ categories before starting
2. **Start with Easy**: Build confidence with basic concepts
3. **Learn from Explanations**: Read why answers are correct
4. **Track Your Progress**: Monitor your score throughout (e.g., 3/5)
5. **Complete All 5**: Finish the full quiz to see your final score
6. **Try Different Topics**: Explore Science, History, Geography, and Sports
7. **Challenge Yourself**: Progress from Easy to Hard difficulty
8. **Review Mistakes**: Use explanations to understand concepts
9. **Aim for Perfect**: Try to achieve 5/5 scores!
10. **Delete & Retry**: Remove incorrect answers and learn from them

### Available Quiz Categories

**Science** (🔬)
- Physics, Chemistry, Biology, Astronomy, Modern Science & Discoveries

**Geography & History** (🌍)
- World Geography, World History, Modern History, Recent Discoveries

**Sports** (⚽)
- General Sports, Olympics, Football/Soccer, Cricket

**Technology** (💻)
- Technology Innovations, Space Exploration, Inventions & Innovations

## 🐛 Troubleshooting

### Server Won't Start
- ✅ Check Python version: `python --version` (need 3.8+)
- ✅ Verify all dependencies installed
- ✅ Check `.env` file exists with valid API key

### API Key Error
- ✅ Get new key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- ✅ Ensure no spaces in `.env` file
- ✅ Restart server after updating

### Chat Not Working
- ✅ Check browser console (F12) for errors
- ✅ Verify server is running on correct port
- ✅ Check CORS is enabled

### PDFs Not Loading
- ✅ Ensure PDFs are in `knowledge_base/` folder
- ✅ Check file permissions
- ✅ Restart server after adding PDFs
- ✅ Look for error messages in server console

### Quiz Mode Issues
- ✅ Wait for full response before clicking options
- ✅ Check internet connection
- ✅ Try different difficulty levels
- ✅ Clear chat and try again

## 🚀 Advanced Customization

### Change Color Theme

Edit `chatbot-gemini-enhanced.html` CSS variables:
```css
/* Primary neon color */
--neon-primary: #38bdf8;  /* Change this */

/* Background gradient */
background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1624 100%);
```

### Add More Fonts

Add Google Fonts link in `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@400;700&display=swap" rel="stylesheet">
```

### Modify Animations

Adjust animation duration and easing:
```css
animation: slideUpCyber 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
```

## 📊 Performance Tips

1. **Optimize PDFs**: Keep PDF sizes under 10MB each
2. **Limit History**: Chat history is limited to prevent memory issues
3. **Clear Regularly**: Use Clear Chat button for long sessions
4. **Browser Cache**: Hard refresh (Ctrl+Shift+R) if UI seems outdated

## 🤝 Contributing

Feel free to enhance this project! Ideas:
- Add more quiz categories
- Implement scoring system
- Add voice chat
- Create study progress tracker
- Add more animation effects

## 📜 License

MIT License - Feel free to use and modify!

## 🙏 Credits

- **UI Design**: Custom cyber-futuristic design
- **AI**: Google Gemini 2.0 Flash
- **Backend**: Flask + Python
- **Frontend**: Vanilla HTML/CSS/JS
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Orbitron, Rajdhani)

## 📞 Support

For issues or questions:
1. Check this README
2. Review console errors (F12)
3. Verify API key is valid
4. Try restarting the server

---

**Made with 💙 and ⚡ by the Bubloo Scientist Team**

# 🎉 NEW FEATURES SHOWCASE

## What's New in Version 2.5?

### 🖥️ Window Controls

#### **Maximize/Minimize Chat Window**
- **Maximize Button** (⛶) - Expand chat to full screen for immersive experience
- **Restore Button** (⬜) - Return to compact mode
- **Smooth Transitions** - Animated resize with 0.3s duration
- **Responsive** - Works perfectly on all screen sizes
- **Keyboard Friendly** - Easy to toggle while working

**How to Use:**
1. Click the expand icon (⛶) in the header
2. Chat fills your entire screen
3. Click compress icon (⬜) to restore

**Perfect For:**
- Reading long AI responses
- Taking quizzes without distractions
- Deep learning sessions
- Mobile users wanting more space

---

### 🗑️ Delete Bot Messages

#### **Hover-to-Delete Functionality**
- **Clean Interface** - Delete button appears on hover
- **Smooth Animation** - Fade out effect (0.3s)
- **Smart History** - Removes from conversation context
- **User-Friendly** - Only bot messages can be deleted
- **Instant Feedback** - Message disappears immediately

**How to Use:**
1. Hover over any bot message
2. Red trash icon appears in top-right corner
3. Click to delete that specific response
4. Message fades out and is removed

**Use Cases:**
- Remove incorrect AI responses
- Clean up test conversations
- Focus on important messages
- Manage chat history better

---

### 🎓 Enhanced Quiz System

#### **5-Question Quiz Sessions**
- **Complete Sessions** - Each quiz has exactly 5 questions
- **Progress Tracking** - See "Question 3/5" as you go
- **Live Scoring** - Current score updates after each answer
- **Final Summary** - Beautiful results screen at the end
- **Motivational Messages** - Personalized feedback based on score

**Scoring System:**
- 5/5 (100%) - 🏆 "Perfect Score! Absolutely Outstanding!"
- 4/5 (80%) - 🌟 "Excellent! Great knowledge!"
- 3/5 (60%) - 👍 "Good job! Keep learning!"
- 2/5 (40%) - 📚 "Not bad! Room for improvement!"
- 0-1/5 - 💪 "Keep practicing! You'll improve!"

#### **Topic Selection System**
- **Pre-Quiz Selection** - Choose topic before starting
- **15+ Categories** organized by subject
- **Random Option** - Let AI surprise you
- **Visual Categories** - Icons for easy identification
- **Dropdown Menu** - Clean, organized interface

**Categories Available:**

**🔬 SCIENCE**
- ⚛️ Physics
- 🧪 Chemistry
- 🧬 Biology
- 🌌 Astronomy
- 🚀 Modern Science & Discoveries

**🌍 GEOGRAPHY & HISTORY**
- 🗺️ World Geography
- 📜 World History
- 📰 Modern History (20th-21st century)
- 🔍 Modern Discoveries

**⚽ SPORTS**
- 🏆 General Sports
- 🥇 Olympics
- ⚽ Football/Soccer
- 🏏 Cricket

**💻 TECHNOLOGY**
- 💻 Technology Innovations
- 🛸 Space Exploration
- 💡 Inventions & Innovations

#### **Smart Question Generation**
- **Context-Aware** - Questions match selected topic
- **Difficulty-Scaled** - Easy/Medium/Hard properly calibrated
- **Educational** - Each question teaches something new
- **Varied Content** - No repeated questions in same session
- **Quality Explanations** - Learn why answers are correct/incorrect

---

### 📊 Progress Tracking

#### **Real-Time Updates**
```
Question 1/5 - Medium difficulty - Physics
Score: 0/0

[Answer question]

Question 2/5 - Medium difficulty - Physics  
Score: 1/1  ✓ Correct!

[Answer question]

Question 3/5 - Medium difficulty - Physics
Score: 1/2  ✗ Keep going!
```

#### **Final Results Screen**
```
╔════════════════════════════╗
║     QUIZ COMPLETE!         ║
║         4/5                ║
║  🌟 Excellent! Great      ║
║     knowledge!             ║
╚════════════════════════════╝
```

---

## 🎨 UI/UX Improvements

### Visual Enhancements
- **Better Message Containers** - Delete button integration
- **Hover Effects** - Smooth opacity transitions
- **Maximize Animations** - Fluid full-screen expansion
- **Progress Indicators** - Clear quiz tracking
- **Score Displays** - Bold, colorful, easy to read

### Accessibility
- **Tooltips** - Every button has helpful hints
- **Clear Labels** - "Maximize", "Delete", "Next Question"
- **Visual Feedback** - Buttons change on hover
- **Keyboard Support** - Tab navigation works
- **Color Coding** - Green (correct), Red (wrong), Cyan (info)

---

## 💡 Usage Tips

### For Students
1. **Start quiz mode** for structured learning
2. **Select your subject** based on what you're studying
3. **Try Easy first** to build confidence
4. **Read all explanations** even when you get it right
5. **Delete wrong messages** to keep chat clean
6. **Maximize for focus** when taking serious quizzes

### For Quick Learning
1. Use **Random Topic** for varied knowledge
2. **Medium difficulty** gives best challenge/learning ratio
3. Complete **full 5-question sessions** for retention
4. **Exit and retry** topics you scored low on
5. Mix **chat mode questions** with **quiz mode** practice

### For Teachers
1. **Maximize mode** great for classroom displays
2. **Delete messages** to reset demonstrations
3. **Topic selection** lets you focus on curriculum
4. **Progress tracking** shows student comprehension
5. **Explanations** can supplement your teaching

---

## 🚀 Technical Details

### Performance
- **Instant Delete** - Messages removed in <300ms
- **Smooth Maximize** - Transition takes 300ms
- **Quiz Generation** - 2-3 seconds per question
- **No Lag** - Optimized for smooth interactions

### Browser Support
- ✅ Chrome/Edge (Best experience)
- ✅ Firefox (Fully supported)
- ✅ Safari (Works great)
- ✅ Mobile browsers (Responsive)

### Storage
- Quiz sessions stored in memory
- Conversation history maintained
- Message IDs for deletion tracking
- No server-side session storage

---

## 🎯 Coming Soon (Ideas)

- 🏅 Leaderboard system
- 📊 Statistics dashboard
- 🎵 Sound effects for correct/wrong answers
- ⏱️ Timed quiz mode
- 🎖️ Achievements and badges
- 📝 Quiz history review
- 🔄 Retry failed questions
- 👥 Multi-player quiz battles

---

## 📞 Feature Requests

Want more features? Here's how to suggest:
1. Use the chat to describe your idea
2. Think about: "What would make this better?"
3. Consider: "What do other quiz apps have?"
4. Imagine: "What would help me learn more?"

**Popular Requests We've Implemented:**
- ✅ Maximize window
- ✅ Delete messages  
- ✅ 5-question sessions
- ✅ Topic selection
- ✅ More subjects (History, Geography, Sports)
- ✅ Progress tracking
- ✅ Score display

---

**Made with 💙 by the Bubloo Scientist Team**

*"The beautiful thing about learning is that no one can take it away from you."* - B.B. King


# 🚀 QUICK START GUIDE

## Setup in 5 Minutes!

### Step 1: Install Python Packages
```bash
pip install flask flask-cors python-dotenv google-generativeai
```

### Step 2: Get Your API Key
1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

### Step 3: Create .env File
Create a file named `.env` in the same folder as your files:
```
GEMINI_API_KEY=paste_your_key_here
PORT=3000
```

### Step 4: Create knowledge_base Folder
```bash
mkdir knowledge_base
```

### Step 5: Run!
```bash
python server-enhanced.py
```

### Step 6: Open Browser
Go to: http://localhost:3000

## 🎮 How to Use

### Chat Mode (Default)
1. Click the floating bot button (bottom-right)
2. Type your science question
3. Get AI-powered answers!

### Quiz Mode
1. Click the graduation cap icon (📚) in the header
2. Choose difficulty: Easy, Medium, or Hard
3. Answer questions and learn!
4. View explanations for each answer

### Tips:
- Try sample questions to get started
- Add PDFs to knowledge_base/ folder for AI to learn from
- Clear chat anytime with the trash icon
- Switch between modes freely!

## 🎨 What Makes This Special?

✨ **Cyber-Futuristic UI** - Neon glows, glassmorphism, holographic effects
🧠 **Smart AI** - Powered by Google Gemini 2.0
📚 **Quiz System** - Three difficulty levels with instant feedback
📄 **PDF Learning** - Upload PDFs and AI learns from them
🎯 **Smooth Animations** - Every interaction is delightful
📱 **Responsive** - Works on phone, tablet, and desktop

## Need Help?

Check the full README.md for detailed documentation!

**Enjoy your AI Lab Assistant! 🧪⚗️🔬**

*"Science is not only a disciple of reason but, also, one of romance and passion."* - Stephen Hawking
