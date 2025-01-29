"""
https://software-engineering.masterschool.com/production-pages/the-almighty-oracle-classwork
"""
from flask import Flask, render_template, request
import chat_GPT_request

app = Flask(__name__)

question = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        content = chat_GPT_request.make_request(question)
        return render_template('index.html', answer=content)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)