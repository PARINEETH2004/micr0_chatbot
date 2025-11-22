# Lena — Neo-Tokyo Microplastics Chatbot 🌊🤖

![Neo-Tokyo Aesthetic](https://img.shields.io/badge/Style-Neo--Tokyo%20Cyberpunk-ff00ff?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green?style=for-the-badge&logo=flask)
![Gemini AI](https://img.shields.io/badge/Gemini-AI%20Powered-orange?style=for-the-badge)

## 🎯 Project Overview

**Lena** is a conversational AI chatbot designed to educate users about microplastic pollution in an engaging, entertaining, and scientifically accurate way. With her sarcastic yet loyal personality and stunning Neo-Tokyo cyberpunk aesthetic, Lena transforms complex environmental data into memorable, character-driven conversations.

### 🌟 Key Features

- **🎭 Character-Driven AI**: Lena's sarcastic but loyal personality makes environmental education engaging
- **🔬 Scientific Accuracy**: Provides factual information about microplastics, pollution, and environmental impact
- **🎨 Neo-Tokyo Aesthetic**: Stunning cyberpunk-inspired UI with neon colors and animations
- **📱 Responsive Design**: Works seamlessly across desktop, tablet, and mobile devices
- **🛡️ Topic Filtering**: Intelligent conversation steering to keep discussions on environmental topics
- **⚡ Real-time Chat**: Instant responses powered by Google's Gemini AI

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Modern web browser

### Installation

1. **Clone or download the project**
   ```bash
   cd lena_microplastics_chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Open `app.py`
   - Replace `"YOUR_API_KEY_HERE"` with your actual Google Gemini API key
   - **Important**: Keep your API key secure and never commit it to version control

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   - Navigate to `http://127.0.0.1:5000`
   - Start chatting with Lena!

## 🏗️ Project Structure

```
lena_microplastics_chatbot/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML template
├── static/
│   └── style.css          # Neo-Tokyo cyberpunk styling
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎮 How to Use

### Starting a Conversation

1. **Launch the app** and you'll see Lena's welcome message
2. **Ask questions** about microplastics, pollution, or environmental topics
3. **Use quick action buttons** for common queries
4. **Enjoy the experience** - Lena's personality makes learning fun!

### Example Conversations

**User**: "What are microplastics?"
**Lena**: "Oh, you want to know about microplastics? *adjusts cyber-goggles* Well, buckle up buttercup, because this is where things get interesting..."

**User**: "How do microplastics affect marine life?"
**Lena**: "Marine life and microplastics? Now we're talking my language! *cracks digital knuckles* Let me break down this environmental nightmare for you..."

### Quick Action Buttons

- **"What are microplastics?"** - Get a comprehensive introduction
- **"Ocean pollution effects"** - Learn about marine ecosystem impact
- **"Reduce plastic waste"** - Discover actionable solutions
- **"Health impacts"** - Understand effects on human health

## 🛠️ Technical Details

### Architecture

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3.0
- **Backend**: Flask (Python web framework)
- **AI Integration**: Google Gemini 1.5 Flash model
- **Styling**: Custom cyberpunk CSS with animations and responsive design

### Key Components

#### Flask Routes
- `/` - Serves the main chat interface
- `/chat` - Handles POST requests for chat messages

#### AI Integration
- **Model**: `gemini-1.5-flash`
- **Persona System**: Maintains Lena's consistent character
- **Topic Filtering**: Ensures conversations stay on environmental topics
- **Error Handling**: Graceful fallbacks for API issues

#### Frontend Features
- **Animated Background**: Cyber-grid and floating particles
- **Responsive Layout**: Mobile-first design approach
- **Loading Indicators**: Visual feedback during AI processing
- **Message Timestamps**: Track conversation history
- **Error Handling**: User-friendly error messages

## 🎨 Design Philosophy

### Neo-Tokyo Cyberpunk Aesthetic

The visual design draws inspiration from:
- **Blade Runner** and **Ghost in the Shell** aesthetics
- **Neon color palettes**: Cyan, magenta, orange highlights
- **Futuristic typography**: Orbitron and Rajdhani fonts
- **Animated elements**: Glowing effects and smooth transitions
- **Glass morphism**: Translucent elements with backdrop blur

### Color Scheme

```css
--primary-cyan: #00ffff      /* Main accent color */
--primary-magenta: #ff00ff   /* Secondary accent */
--primary-orange: #ff8c00    /* Highlight color */
--neon-blue: #0080ff         /* Interactive elements */
--neon-green: #00ff80        /* Success states */
--neon-pink: #ff0080         /* Warning states */
--dark-bg: #0a0a0f           /* Primary background */
```

## 🔧 Configuration

### Environment Variables (Optional)

You can set these environment variables instead of hardcoding values:

```bash
export GEMINI_API_KEY="your_api_key_here"
export FLASK_ENV="development"
export FLASK_DEBUG="True"
```

### Customization Options

#### Modify Lena's Personality
Edit the `LENA_PROFILE` in `app.py` to adjust her responses and expertise areas.

#### Add New Quick Actions
Update the quick action buttons in `index.html` and add corresponding logic in the JavaScript.

#### Customize Styling
Modify `static/style.css` to change colors, animations, or layout elements.

## 🚨 Important Notes

### Security
- **Never commit API keys** to version control
- **Use environment variables** in production
- **Implement rate limiting** for production deployments

### Performance
- Responses typically load within 2-3 seconds
- Application supports multiple concurrent users
- Mobile-optimized for various screen sizes

### Browser Compatibility
- **Recommended**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile**: iOS Safari, Chrome Mobile, Samsung Internet
- **Features**: CSS Grid, Flexbox, ES6+ JavaScript required

## 🔮 Future Enhancements

### Planned Features
- **🎤 Voice Interaction**: Speech-to-text and text-to-speech capabilities
- **📊 Real-time Data**: Integration with environmental data APIs
- **🌍 Multi-language Support**: Localization for global accessibility
- **🎮 Gamification**: Daily eco-challenges and environmental quizzes
- **📈 Analytics Dashboard**: Track user engagement and learning progress

### Technical Improvements
- **Database Integration**: Store conversation history
- **User Authentication**: Personalized experiences
- **API Rate Limiting**: Enhanced production readiness
- **Docker Containerization**: Simplified deployment
- **Progressive Web App**: Offline functionality

## 🤝 Contributing

This project was created as an educational demonstration of AI integration in environmental education. Feel free to:

- **Fork the repository** for your own experiments
- **Suggest improvements** to Lena's personality or knowledge base
- **Report bugs** or usability issues
- **Share feedback** on the user experience

## 📚 Educational Value

### Learning Objectives
- **Environmental Awareness**: Understanding microplastic pollution
- **AI Integration**: Practical application of generative AI
- **Web Development**: Full-stack development with Flask
- **UX Design**: Creating engaging, character-driven interfaces
- **Prompt Engineering**: Maintaining consistent AI personas

### Academic Applications
- **Environmental Science Courses**: Interactive learning tool
- **Computer Science Projects**: AI and web development showcase
- **Design Studies**: Cyberpunk aesthetic implementation
- **Sustainability Education**: Engaging awareness campaigns

## 📄 License

This project is created for educational purposes. Please ensure you comply with Google's Gemini API terms of service when using this application.

## 🆘 Troubleshooting

### Common Issues

**Application won't start**
- Check Python version (3.7+ required)
- Verify all dependencies are installed
- Ensure API key is properly set

**Chat not responding**
- Verify internet connection
- Check API key validity
- Look for error messages in browser console

**Styling issues**
- Clear browser cache
- Check if CSS file is loading properly
- Verify browser compatibility

**Mobile display problems**
- Test on different devices
- Check viewport meta tag
- Verify responsive CSS rules

### Getting Help

If you encounter issues:
1. Check the browser console for JavaScript errors
2. Review the Flask terminal output for backend errors
3. Verify your API key is valid and has sufficient quota
4. Ensure all dependencies are correctly installed

---

**Built with 💚 for environmental education and 🤖 AI innovation**

*"The future is now, and it's time we start taking care of our planet. Let Lena show you how."* 🌊✨