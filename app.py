from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['user_query']
    bot_response = generate_random_response()
    return jsonify({'bot_response': bot_response})

def generate_random_response():
    responses = ["Hello!", "How can I help you?", "Nice to meet you!"]
    return random.choice(responses)

if __name__ == '__main__':
    app.run(debug=True)

# Import necessary libraries for openAI integration
import openai
import os

# Set up your OpenAI API key
openai.api_key = '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'

# Existing code remains the same...

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['user_query']
    
    # Call OpenAI API to get bot response
    bot_response = generate_openai_response(user_query)
    
    return jsonify({'bot_response': bot_response})

def generate_openai_response(user_query):
    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_query,
        max_tokens=100
    )
    return response['choices'][0]['text']

# Import additional libraries for PDF processing and embedding
import PyPDF2
import numpy as np

# Existing code remains the same...

# Function to generate embeddings from PDF
def generate_embedding_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text_content = ''
        for page_num in range(pdf_reader.numPages):
            text_content += pdf_reader.getPage(page_num).extractText()
    
    # Use OpenAI API to get embedding
    embedding_response = openai.Embed.create(
        model="text-davinci-003",
        documents=[text_content]
    )
    
    return np.array(embedding_response['data'][0]['embedding'])

# Existing code remains the same...

if __name__ == '__main__':
    # Example usage: Generate and print embedding from a sample PDF
    pdf_embedding = generate_embedding_from_pdf('sample.pdf')
    print(pdf_embedding)
    
    app.run(debug=True)

