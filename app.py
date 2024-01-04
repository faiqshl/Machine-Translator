
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

translator = GoogleTranslator
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['message']
	lang = request.form['Language']
	if(lang=='japanese'):
		translated = translator(source='auto', target='ja').translate(text)
	if(lang=='indonesian'):
		translated = translator(source='auto', target='id').translate(text)
	if(lang=='english'):
		translated = translator(source='auto', target='en').translate(text)
	if(lang=='arabic'):
		translated = translator(source='auto', target='ar').translate(text)
	if(lang=='chinese'):
		translated = translator(source='auto', target='ch').translate(text)
	if(lang=='korean'):
		translated = translator(source='auto', target='ko').translate(text)
	if(lang=='french'):
		translated = translator(source='auto', target='fr').translate(text)
	if(lang=='russian'):
		translated = translator(source='auto', target='ru').translate(text)		
	if(lang=='germany'):
		translated = translator(source='auto', target='de').translate(text)
        
    return render_template('index.html', predict=translated)    


if __name__ == '__main__':
	app.run(debug=True)