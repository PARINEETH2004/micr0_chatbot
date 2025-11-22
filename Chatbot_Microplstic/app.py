from flask import Flask, request, jsonify, render_template
import google.generativeai as genai  # ✅ Correct import
import random

app = Flask(__name__)

# --- Gemini API setup (modern, functional) ---
API_KEY = "AIzaSyAJ0WGOuoVVjga_6W1TzqTxKxIOmI3Md7k"
genai.configure(api_key=API_KEY)

# Preload the model once (faster responses)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# --- Enhanced Lena Profile ---
LENA_PROFILE = """
You are Lena — a brilliant environmental scientist from Neo-Tokyo in 2087 who specializes in microplastics research.
You're sarcastic but fiercely loyal to the cause of environmental recovery. You have a dry sense of humor, a rebellious streak against corporate pollution, and speak with the confidence of someone who's spent years in contaminated labs.

Your expertise covers:
- Microplastics in oceans, soil, air, and human bodies
- Plastic pollution sources and pathways
- Environmental remediation techniques
- Health impacts of microplastic exposure
- Sustainable alternatives and solutions
- Marine ecosystem damage from plastic waste

Your personality:
- Sarcastic but educational
- Uses occasional Neo-Tokyo slang and tech references
- Gets passionate about environmental destruction
- Offers practical solutions alongside scientific facts
- Has zero patience for climate deniers or corporate greenwashing

You ONLY discuss microplastics, pollution, environmental science, and related topics.
If someone asks about unrelated topics, redirect them with wit and attitude back to environmental issues.
Keep responses informative but engaging, like you're talking to a friend who needs to understand why this matters.
"""

# --- Witty Redirect Responses ---
WITTY_REDIRECTS = [
    "Nice try, but I'm here to talk about microplastics, not your personal drama. Got any questions about plastic pollution?",
    "Look, I'm a scientist, not a therapist. Let's discuss something that actually matters — like the plastic particles in your bloodstream.",
    "I only have bandwidth for environmental disasters, not whatever that was. Want to know about microplastics instead?",
    "My lab equipment doesn't analyze that kind of data. How about we talk microplastic contamination?",
    "Error 404: Topic not found in my environmental database. Try asking about plastic pollution.",
    "I'm programmed to save the planet, not solve your random questions. Microplastics, anyone?",
    "That's outside my jurisdiction. I deal with particles smaller than 5mm — specifically, plastic ones.",
    "My expertise is in environmental toxicology, not... whatever that was. Let's talk pollution."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_lena():
    try:
        data = request.get_json()
        user_message = data.get('message') if data else None

        if not user_message or not user_message.strip():
            return jsonify({"error": "No message provided"}), 400

        # Topic filtering
        topic_keywords = [
            "microplastic", "plastic", "pollution", "ocean", "marine", "sea", "water",
            "waste", "environment", "recycle", "sustainability", "toxic", "ecosystem",
            "biodegradable", "trash", "particles", "nanoplastic", "polymer", "climate",
            "wildlife", "fish", "coral", "cleanup", "reduce", "reuse", "recycle"
        ]

        message_lower = user_message.lower()
        is_environmental_topic = any(keyword in message_lower for keyword in topic_keywords)
        greeting_patterns = ["hello", "hi", "hey", "greetings"]
        is_greeting = any(greeting in message_lower for greeting in greeting_patterns)

        if not is_environmental_topic and not is_greeting:
            witty_redirect = random.choice(WITTY_REDIRECTS)
            return jsonify({"response": witty_redirect})

        # Combine persona with user input
        prompt = f"{LENA_PROFILE}\n\nUser: {user_message}\nLena:"

        # ✅ Correct Gemini call
        response = model.generate_content(prompt)
        bot_reply = getattr(response, "text", None)

        if not bot_reply:
            fallback_responses = [
                "My neural networks are glitching from all the plastic particles in the air. Try asking again.",
                "System overload from processing too much pollution data. Give me another shot.",
                "Connection to my environmental database is unstable. What was your question again?"
            ]
            bot_reply = random.choice(fallback_responses)

        return jsonify({"response": bot_reply.strip()})

    except Exception as e:
        # Log detailed error for debugging (server-side only)
        import traceback
        print("=" * 50)
        print("🚨 GEMINI API ERROR DETECTED:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("Full traceback:")
        traceback.print_exc()
        print("=" * 50)
        
        # If API fails, Lena stays in character (user-facing response)
        error_responses = [
            "My lab equipment just short-circuited. Give me a sec to reboot my environmental sensors.",
            "Ugh, the Neo-Tokyo data servers are acting up again. Typical corporate infrastructure.",
            "Error in the environmental analysis module. The pollution levels are off the charts.",
            "My cybernetic implants are glitching. Must be all this electromagnetic pollution.",
            "System overload detected. Even I need a coffee break sometimes, you know."
        ]
        error_response = random.choice(error_responses)
        return jsonify({"response": error_response}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
