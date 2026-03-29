from flask import Flask, request, jsonify
from rag import RAGChatbot
from config import API_KEY, DOCUMENT_PATH

app = Flask(__name__)

# Initialize the RAG chatbot
chatbot = RAGChatbot(api_key=API_KEY, document_path=DOCUMENT_PATH)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    response = chatbot.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)