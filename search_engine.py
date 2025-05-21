import os

DOCUMENTS_DIR = "c:\\github\\TechBridge\\documents"

def search_documents(query):
    results = []
    for filename in os.listdir(DOCUMENTS_DIR):
        filepath = os.path.join(DOCUMENTS_DIR, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                if query.lower() in content.lower():
                    results.append({"file": filename, "snippet": get_snippet(content, query)})
    return results

def get_snippet(content, query, snippet_length=100):
    index = content.lower().find(query.lower())
    if index == -1:
        return ""
    start = max(index - snippet_length // 2, 0)
    end = min(index + snippet_length // 2, len(content))
    return content[start:end].replace('\n', ' ')
