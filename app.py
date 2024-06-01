from flask import Flask, request, jsonify
from transformers import pipeline, BartForConditionalGeneration, BartTokenizer
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import torch

# Creating the pipeline with the loaded model and tokenizer
summarizer = pipeline("summarization", model ="facebook/bart-large-cnn")


@app.route('/summarise', methods=['POST'])
def summarise():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    word_limit = data.get('word_limit', None)
    if word_limit:
        total_words = len(text.split())
        if word_limit > total_words:
            return jsonify({'error': 'Word limit exceeds the total number of words in the summary'}), 400
        
    if word_limit is None:
        word_limit = 130

    summary = summarizer(text, max_length=word_limit, min_length=30, do_sample=False)
    summarised_text = summary[0]['summary_text']
    return jsonify({'summary': summarised_text})

if __name__ == '__main__':
    app.run(debug=True)
