This project provides a Flask-based API for text summarization using a pre-trained BART model from the Hugging Face Transformers library. The API allows you to submit text for summarization and optionally specify a word limit for the summary.

**Features**
Asynchronous request handling for improved performance.
Utilizes GPU if available for faster inference.
CORS enabled for cross-origin requests.

**Prerequisites**
Python 3.7+

**Install Dependencies**
pip install -r requirements.txt

**API Endpoints**

POST /summarise
Description: Summarizes the provided text.
Request Body:
text (string, required): The text to be summarized.
word_limit (integer, optional): The maximum number of words in the summary.

**Request Example**
{
    "text": "Your long text here...",
    "word_limit": 50  // Optional
}


