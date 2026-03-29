def load_documents(document_path):
    # Function to load documents from the specified path
    documents = []
    try:
        with open(document_path, 'r') as file:
            documents = file.readlines()
    except Exception as e:
        print(f"Error loading documents: {e}")
    return documents

def preprocess_text(text):
    # Function to preprocess text for the model
    return text.strip().lower()

def format_response(response):
    # Function to format the response from the model
    return response.strip()