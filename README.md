# RAG Chatbot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot using LangChain and the Google Gemini language model. The chatbot is designed to retrieve relevant documents and generate contextually appropriate responses based on user input.

## Project Structure
```
rag-chatbot
├── src
│   ├── app.py          # Main entry point for the chatbot application
│   ├── rag.py          # Implementation of the RAG architecture
│   ├── config.py       # Configuration settings for the application
│   └── utils.py        # Utility functions for various tasks
├── data
│   └── documents       # Directory to store documents for retrieval
├── requirements.txt    # List of dependencies for the project
└── README.md           # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd rag-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application:
   - Update the `src/config.py` file with your Google Gemini API key and document path.

## Usage
To run the chatbot, execute the following command:
```
python src/app.py
```
Follow the prompts to interact with the chatbot.

## RAG Architecture
The RAG architecture combines retrieval and generation capabilities. The `RAGChatbot` class in `src/rag.py` retrieves relevant documents from the `data/documents` directory and uses the Google Gemini model to generate responses based on the retrieved information.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.