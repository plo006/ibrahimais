from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder="templates", static_folder="static")

# Configure Gemini API Key
genai.configure(api_key="AIzaSyAMnZphx2hskOhb8fkzQVWovpemdBl2jtA")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Generate response using Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_message)
    bot_reply = response.text if response.text else "Sorry, I couldn't understand that."
    
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
