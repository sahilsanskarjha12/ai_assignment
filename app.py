from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'  # Replace with your OpenAI API key

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_query = data.get('query')

    # Print or log the user query for debugging
    print("User Query:", user_query)

    # Use OpenAI GPT to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can experiment with different engines
        prompt=user_query,
        max_tokens=150
    )

    # Print or log the OpenAI GPT response for debugging
    print("OpenAI Response:", response)

    return jsonify({'response': response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True)
