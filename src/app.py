from flask import Flask, request, jsonify
from rag import RAGChatbot
from config import API_KEY, DOCUMENT_PATH
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Global variable to hold the chatbot instance
chatbot = None

def get_chatbot():
    """Lazy initialization to ensure the bot is only created once."""
    global chatbot
    if chatbot is None:
        try:
            logger.info(f"Initializing RAG engine using documents at: {DOCUMENT_PATH}")
            # Ensure the path exists before trying to load
            if not os.path.exists(DOCUMENT_PATH):
                raise FileNotFoundError(f"The path {DOCUMENT_PATH} does not exist.")
                
            chatbot = RAGChatbot(api_key=API_KEY, document_path=DOCUMENT_PATH)
            logger.info("RAG Engine successfully initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize chatbot: {e}")
            return None
    return chatbot

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint to check if the bot is actually ready."""
    bot = get_chatbot()
    if bot:
        return jsonify({'status': 'ready', 'path': DOCUMENT_PATH}), 200
    return jsonify({'status': 'error', 'message': 'Chatbot failed to initialize'}), 500

@app.route('/chat', methods=['POST'])
def chat():
    bot = get_chatbot()
    if not bot:
        return jsonify({'error': 'Chatbot not initialized. Check server logs.'}), 503
        
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided in JSON body'}), 400

    user_message = data.get('message')
    logger.info(f"Received query: {user_message}")
    
    try:
        response = bot.get_response(user_message)
        return jsonify({
            'status': 'success',
            'response': response
        })
    except Exception as e:
        logger.error(f"Error during RAG generation: {e}")
        return jsonify({'error': 'Failed to process message'}), 500

if __name__ == '__main__':
    # We remove the global initialize_bot() call here and let get_chatbot() 
    # handle it on the first request, or simply call it once:
    with app.app_context():
        get_chatbot()
        
    # debug=True is fine for development, but it will restart the bot on code changes
    app.run(debug=True, port=5000)