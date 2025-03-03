import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ✅ API Key setup
API_KEY = "AIzaSyCm-PFCD1FPyt1cVcWLQEFgKuyIm3mwv68"

# ✅ Configure the API key
genai.configure(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        # ✅ First API call - Get detailed interests
        model1 = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")
        response1 = model1.generate_content(
            f"Can you analyze the public posts of this public Facebook profile with this exact username: {user_input}. "
            f"Search Google for this Facebook profile and its publicly available posts. "
            f"Analyze and give me five of their areas of interest."
        )   

        if not response1 or not hasattr(response1, "text") or not response1.text.strip():
            return jsonify({"error": "Gemini API returned an empty response."}), 500

        detailed_interests = response1.text.strip()

        # ✅ Second API call - Extract only the key interest names
        model2 = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")
        response2 = model2.generate_content(
            f"Suggest me actions to impress them on meeting them for the first time. Extract and list only the five key interest areas (as bullet points) from the following text:\n\n{detailed_interests}."
        )

        if response2 and hasattr(response2, "text") and response2.text.strip():
            refined_interests = response2.text.strip()
            return jsonify({"response": refined_interests})
        else:
            return jsonify({"error": "Refinement step failed."}), 500

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT",4000))
    app.run(host="0.0.0.0", port=port)
