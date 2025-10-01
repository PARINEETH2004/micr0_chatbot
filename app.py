from flask import Flask, request, jsonify, render_template
from google import genai

app = Flask(__name__, template_folder='.')

# Replace with your Gemini API key
API_KEY = "AIzaSyCAER21snzjfb9szPKcy_rG5Fn5PyBpJwg"
client = genai.Client(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_gemini():
    data = request.get_json()
    user_message = data.get('message') if data else None

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response using Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
