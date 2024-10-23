from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')  # Ensure this model is installed

def generate_response(question):
    doc = nlp(question)
    # Extract named entities and their labels from the user's question
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    if entities:
        # Construct a response mentioning the entities found
        entity_list = ', '.join([f"'{text}' ({label})" for text, label in entities])
        response = f"I noticed you mentioned {entity_list}."
    else:
        response = "Tell me more about that."

    return response

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if data is None or 'message' not in data:
            return jsonify({"response": "Please provide a 'message' in your JSON request."}), 400
        question = data['message']
        response = generate_response(question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
