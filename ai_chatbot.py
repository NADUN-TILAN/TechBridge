def load_document(filepath):
    """Load the document from the given file path."""
    with open(filepath, 'r') as file:
        return file.readlines()

def search_document(document_lines, query):
    """Search for the query in the document and return matching lines."""
    results = []
    for line_number, line in enumerate(document_lines, start=1):
        if query.lower() in line.lower():
            results.append(f"Line {line_number}: {line.strip()}")
    return results

def chatbot():
    """AI chatbot to search for words or phrases in the document."""
    document_path = r"https://drive.google.com/drive/folders/14GKiHPeVCEic8WRgwybbbVLN90LmLkUw"
    document_lines = load_document(document_path)
    
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        query = input("Enter a word or phrase to search: ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        results = search_document(document_lines, query)
        if results:
            print("Found the following matches:")
            for result in results:
                print(result)
        else:
            print("No matches found.")

if __name__ == "__main__":
    chatbot()
