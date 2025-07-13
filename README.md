                   🎙️ GROQ AI CHATBOT with LLaMA3 – Powered by Streamlit

📌 Project Overview

Welcome to my AI Chatbot Web App, where conversations meet blazing-fast inference speeds using Groq’s LLaMA3 model!

Built using Streamlit, this app lets users interact with a helpful AI assistant in real-time — perfect for showcasing conversational AI with a minimal, beautiful UI.

🚀 How I Built & Ran the App (Step-by-Step):

Here’s the exact process I followed to bring this project to life 👇

1️⃣ Create a fresh project folder for the chatbot.

2️⃣ Inside that folder, create a file named app.py

🧠 This is the heart of the Streamlit app where all logic goes.

3️⃣ Add a .env file

🔐 Use this file to securely store your API key:GROQ_API_KEY=your_actual_key_here

4️⃣ Then, create a requirements.txt file and include: 

1) streamlit

2) python-dotenv

3) groq

5️⃣ Open the terminal in your project directory.

6️⃣ Install all the required packages:
pip install -r requirements.txt

7️⃣ Run the application using Streamlit:
streamlit run app.py

8️⃣ Visit the chatbot in your browser:
🌍 http://localhost:8501

🔁 GitHub Upload Steps
(How I published my project to GitHub 💻)

1️⃣ Created a new repository on GitHub.

2️⃣ Opened terminal inside my local project folder.

3️⃣ Initialized Git locally:
git init

4️⃣ Added all project files:
git add .

5️⃣ Committed changes with a message:
git commit -m "Add Groq Chatbot Streamlit app"

6️⃣ Linked the folder to GitHub:
git remote add origin https://github.com/your-username/your-repo-name.git

7️⃣ Pushed everything to GitHub:
git push -u origin main

📝 Replace your-username and your-repo-name with your actual GitHub URL.

📁 Project Folder Structure

📦 groq-chatbot-project

┣ 📄 app.py             → Main chatbot interface

┣ 📄 .env               → Securely stores Groq API key

┣ 📄 requirements.txt   → List of required Python packages

┣ 📄 README.md          → Full setup guide and documentation

💡 What the Chatbot Can Do

✔ Accepts real-time questions from users

✔ Uses Groq’s lightning-fast LLaMA3 to generate replies

✔ Streams assistant responses smoothly on screen

✔ Maintains the full conversation context

✔ Delivers a sleek and friendly UI via Streamlit

✨ Tech Stack Used

Streamlit for frontend and interactivity

Groq API with LLaMA3 model for responses

Python-dotenv to manage API key securely

👩‍💻 Created By

Ushmitha Annapaneni

Feel free to ⭐ star or fork the project if you found it interesting!

📄 License

MIT License – Free to use, modify, and share