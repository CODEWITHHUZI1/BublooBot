<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bubloo Scientist - Lab Assistant</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Roboto for a clean, scientific look -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f4f8; /* Light gray-blue background */
        }
        
        /* Custom Scrollbar for the chat window */
        .scrollbar-hide::-webkit-scrollbar {
            display: none;
        }
        .chat-scroll::-webkit-scrollbar {
            width: 6px;
        }
        .chat-scroll::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        .chat-scroll::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }
        .chat-scroll::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        /* Message Bubble Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .message-anim {
            animation: fadeIn 0.3s ease-out forwards;
        }

        /* Typing Indicator dots */
        .typing-dot {
            animation: typing 1.4s infinite ease-in-out both;
        }
        .typing-dot:nth-child(1) { animation-delay: -0.32s; }
        .typing-dot:nth-child(2) { animation-delay: -0.16s; }
        
        @keyframes typing {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    </style>
</head>
<body class="h-screen flex items-center justify-center p-4">

    <!-- Main Chat Widget Container -->
    <div class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden flex flex-col h-[600px] border border-gray-200">
        
        <!-- Header -->
        <div class="bg-blue-700 p-4 flex items-center justify-between text-white shadow-md z-10">
            <div class="flex items-center space-x-3">
                <!-- Logo Container (Replace generic icon with actual logo URL if needed) -->
                <div class="bg-white text-blue-700 p-2 rounded-full w-10 h-10 flex items-center justify-center">
                    <i class="fa-solid fa-flask text-lg"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight">Lab Assistant</h1>
                    <p class="text-xs text-blue-200 flex items-center">
                        <span class="w-2 h-2 bg-green-400 rounded-full mr-1 animate-pulse"></span> Online
                    </p>
                </div>
            </div>
            <!-- Header Actions -->
            <button class="hover:bg-blue-600 p-2 rounded-full transition-colors" title="About Bubloo Scientist">
                <i class="fa-solid fa-info-circle"></i>
            </button>
        </div>

        <!-- Chat Area -->
        <div id="chat-messages" class="flex-1 bg-gray-50 p-4 overflow-y-auto chat-scroll flex flex-col space-y-4">
            <!-- Time Timestamp -->
            <div class="text-center text-xs text-gray-400 my-2">Today</div>
            
            <!-- Initial Bot Message -->
            <!-- Will be populated by JS on load -->
        </div>

        <!-- Input Area -->
        <div class="bg-white p-3 border-t border-gray-100">
            <div class="relative flex items-center bg-gray-100 rounded-full px-4 py-2 border border-gray-200 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-100 transition-all">
                <input id="user-input" type="text" placeholder="Ask about Science, Team, or Contact..." 
                    class="flex-1 bg-transparent outline-none text-gray-700 text-sm placeholder-gray-400"
                    autocomplete="off">
                <button id="send-btn" class="ml-2 text-blue-600 hover:text-blue-800 transition-transform hover:scale-110">
                    <i class="fa-solid fa-paper-plane text-lg"></i>
                </button>
            </div>
            <div class="text-center mt-2">
                <p class="text-[10px] text-gray-400">Powered by Bubloo Scientist AI</p>
            </div>
        </div>

    </div>

    <script>
        // --- Data & Logic ---

        // The Knowledge Base derived from your documents
        const knowledgeBase = {
            greetings: [
                "Hello! I am the Lab Assistant for Bubloo Scientist. How can I help you discover the wonders of science today?",
                "Welcome to Bubloo Scientist! I'm here to answer your questions about Physics, Chemistry, our Team, or our projects."
            ],
            
            // Keywords and their associated responses
            responses: [
                {
                    keywords: ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
                    answer: "Hello there! I'm ready to explore science with you. What's on your mind?"
                },
                {
                    keywords: ["bye", "goodbye", "see you", "later", "exit"],
                    answer: "Goodbye! Keep exploring and stay curious. Come back anytime you have more questions!"
                },
                {
                    keywords: ["purpose", "what do you do", "mission", "goal", "help me"],
                    answer: "My purpose is to be your personal guide to the Bubloo Scientist website. I'm here to help you discover the wonders of science, introduce you to our team, and help you find resources on Physics, Chemistry, and more!"
                },
                {
                    keywords: ["popular", "posts", "articles", "read", "top", "trending", "best"],
                    answer: "Our readers love these popular topics:<br><br>• <b>Quantum Physics:</b> Dive into the fascinating world of quantum mechanics.<br>• <b>Python Coding:</b> Learn how to build things with code in our 'Coding and Languages' section.<br>• <b>Motorsports:</b> Check out our dedicated project on racing technology.<br>• <b>Entrepreneurship:</b> Read our guide on starting your own business."
                },
                {
                    keywords: ["team", "who are you", "founder", "ceo", "staff", "members", "creator"],
                    answer: "Meet the team behind Bubloo Scientist:<br><br>• <b>Abdur Rehman Siddiqui:</b> CEO<br>• <b>Muhammad Mustafa Khan:</b> Lead Designer<br>• <b>Ayaan Hassan Khan:</b> Web Developer<br>• <b>Sadaat Furqan:</b> Marketer<br>• <b>Saim Ahmed:</b> Social Media Manager<br>• <b>Muhammad Huzaifa Khan:</b> Web Designer"
                },
                {
                    keywords: ["chemistry", "what is chemistry"],
                    answer: "<b>Chemistry</b> is the study of matter and its properties. According to our lead contributors (who have 5+ years of experience!), it's a fascinating field that explores how substances interact, even if it seems complex at first!"
                },
                {
                    keywords: ["living", "characteristics", "mrs gren", "life"],
                    answer: "All living things share seven basic characteristics, remembered by the acronym <b>MRS GREN</b>:<br>1. Movement<br>2. Respiration<br>3. Sensitivity<br>4. Growth<br>5. Reproduction<br>6. Excretion<br>7. Nutrition"
                },
                {
                    keywords: ["mutation", "liger", "evolve"],
                    answer: "<b>Mutations</b> occur when living things change or evolve into different forms. A rare example mentioned on our site is the <b>Liger</b> (a cross between a lion and a tiger)."
                },
                {
                    keywords: ["digestion", "absorption", "food"],
                    answer: "Here is the difference:<br>• <b>Digestion:</b> The process where large, complex, insoluble food molecules are converted into smaller, simpler, soluble ones.<br>• <b>Absorption:</b> The stage where these simplified nutrients are taken into the body's cells for energy and growth."
                },
                {
                    keywords: ["contact", "email", "phone", "number", "whatsapp", "reach"],
                    answer: "You can reach us via:<br>📞 <b>Phone:</b> 03378324258 (PK)<br>📧 <b>Email:</b> bublooscientist@gmail.com, abisbah2011@gmail.com<br>💬 You can also use the WhatsApp button on our website!"
                },
                {
                    keywords: ["website", "offer", "bubloo", "about"],
                    answer: "<b>Bubloo Scientist</b> is a hub for knowledge! We offer content on Physics, Chemistry, Biology, and Computer Languages. We also do Book Reviews and have a section for our latest Projects."
                },
                {
                    keywords: ["code", "coding", "python", "programming", "language"],
                    answer: "Yes! We have a dedicated section for 'Coding and Languages'. Currently, we share updates on learning <b>Python</b> and creating new things through programming."
                },
                {
                    keywords: ["project", "work", "motorsport", "business", "entrepreneurship"],
                    answer: "Our latest projects include a <b>Motorsports website</b> and a guide on <b>Entrepreneurship</b>. Check out the 'Creative' and 'My Projects' sections for more."
                },
                {
                    keywords: ["physics", "quantum"],
                    answer: "Our team loves Physics! We regularly post updates, including fascinating topics like <b>Quantum Physics</b>. Stay tuned to the website for the latest articles."
                }
            ],

            fallback: "I'm not sure about that specific detail yet. However, I can tell you about our Team, Chemistry, Living Things, or how to Contact us. What would you like to know?"
        };

        // --- DOM Elements ---
        const chatMessages = document.getElementById('chat-messages');
        const userInput = document.getElementById('user-input');
        const sendBtn = document.getElementById('send-btn');

        // --- Functions ---

        function addMessage(text, sender) {
            const div = document.createElement('div');
            const isBot = sender === 'bot';
            
            div.className = `flex w-full ${isBot ? 'justify-start' : 'justify-end'} message-anim`;
            
            const bubbleHtml = `
                <div class="flex max-w-[80%] ${isBot ? 'flex-row' : 'flex-row-reverse'} items-end gap-2">
                    ${isBot ? 
                        `<div class="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 flex-shrink-0 border border-blue-200">
                            <i class="fa-solid fa-robot text-xs"></i>
                         </div>` : 
                        `<div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center text-gray-600 flex-shrink-0">
                            <i class="fa-solid fa-user text-xs"></i>
                         </div>`
                    }
                    
                    <div class="${isBot ? 'bg-white text-gray-800 border-l-4 border-blue-600' : 'bg-blue-600 text-white'} px-4 py-2 rounded-lg shadow-sm text-sm leading-relaxed">
                        ${text}
                    </div>
                </div>
            `;
            
            div.innerHTML = bubbleHtml;
            chatMessages.appendChild(div);
            scrollToBottom();
        }

        function showTypingIndicator() {
            const div = document.createElement('div');
            div.id = 'typing-indicator';
            div.className = 'flex w-full justify-start message-anim';
            div.innerHTML = `
                <div class="flex max-w-[80%] flex-row items-end gap-2">
                    <div class="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 flex-shrink-0 border border-blue-200">
                        <i class="fa-solid fa-robot text-xs"></i>
                    </div>
                    <div class="bg-white border-l-4 border-blue-600 px-4 py-3 rounded-lg shadow-sm">
                        <div class="flex space-x-1">
                            <div class="w-2 h-2 bg-gray-400 rounded-full typing-dot"></div>
                            <div class="w-2 h-2 bg-gray-400 rounded-full typing-dot"></div>
                            <div class="w-2 h-2 bg-gray-400 rounded-full typing-dot"></div>
                        </div>
                    </div>
                </div>
            `;
            chatMessages.appendChild(div);
            scrollToBottom();
        }

        function removeTypingIndicator() {
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();
        }

        function scrollToBottom() {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function getBotResponse(input) {
            const lowerInput = input.toLowerCase();
            
            // Check for matches in knowledge base
            for (const item of knowledgeBase.responses) {
                if (item.keywords.some(keyword => lowerInput.includes(keyword))) {
                    return item.answer;
                }
            }
            
            return knowledgeBase.fallback;
        }

        function handleUserMessage() {
            const text = userInput.value.trim();
            if (!text) return;

            // 1. Add User Message
            addMessage(text, 'user');
            userInput.value = '';
            
            // 2. Show Typing Indicator
            showTypingIndicator();

            // 3. Simulate Network Delay & Respond
            setTimeout(() => {
                removeTypingIndicator();
                const response = getBotResponse(text);
                addMessage(response, 'bot');
            }, 800 + Math.random() * 500); // Random delay between 800ms and 1300ms
        }

        // --- Event Listeners ---
        sendBtn.addEventListener('click', handleUserMessage);
        
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') handleUserMessage();
        });

        // --- Initialization ---
        window.addEventListener('load', () => {
            setTimeout(() => {
                addMessage(knowledgeBase.greetings[0], 'bot');
            }, 500);
        });

    </script>
</body>
</html>