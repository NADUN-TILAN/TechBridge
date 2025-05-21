from flask import Flask, request, jsonify
from search_engine import search_documents

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query', '')
    if not user_input:
        return jsonify({"error": "Query is required"}), 400

    # Search for the query in documents
    results = search_documents(user_input)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
