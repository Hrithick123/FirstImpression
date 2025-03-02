# First Impression - Decode Interests, Build Connections

## 📌 Overview
**First Impression** is a web application that analyzes the publicly available information of a Facebook profile and identifies key areas of interest. Using Google's **Gemini AI**, it suggests actions to impress the person when meeting them for the first time.

## 🚀 Features
- 🔍 **Public Profile Analysis**: Extracts interests from publicly available Facebook posts.
- 🤖 **AI-Powered Insights**: Uses **Gemini AI** to analyze and refine key interests.
- 🎯 **Actionable Suggestions**: Provides tailored advice on how to engage based on interests.
- 🖥️ **User-Friendly Interface**: Simple and clean UI for easy interaction.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **AI Model:** Google Generative AI (Gemini)

## 📥 Installation & Setup
### 🔹 Clone the Repository
```bash
git clone https://github.com/yourusername/InstaConnect.git
cd InstaConnect
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Set Up API Key
1. Get your **Google AI API Key** from [Google AI Studio](https://ai.google.dev/).
2. Replace the `API_KEY` in `app.py` with your own.

### 🔹 Run the Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## 📸 Screenshots
🚧 *Coming Soon...*

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Renders the homepage |
| POST   | `/chat`  | Sends input to Gemini AI and returns analyzed interests |

## 🎯 Usage
1. Enter a **Facebook profile name** in the input box.
2. Click **Analyze**.
3. The AI will fetch, analyze, and display key interests and engagement tips.

## 🌍 Deployment
You can deploy this on:
- **Heroku**
- **Render**
- **Vercel (with Flask adapter)**

## 📜 License
MIT License. Feel free to use and contribute!

## ✨ Contributions
We welcome contributions! Feel free to:
- Open an **issue** for bug reports.
- Submit a **pull request** with improvements.

## 👨‍💻 Developed By
**Hrithick**  
🔗 [Portfolio](https://hrithick123.github.io/Hrithickfolio/)

