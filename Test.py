from flask import Flask, request
import sqlite3
import logging
import json

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    input_js = request.json
    cats = ["еда", "продукты"]
    input_text = input_js["request"]["command"]
    out = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    cat = ""
    summ = 0
    for string in input_text.split(" "):
        if string in cats:
            cat = string
        else:
            try:
                summ = int(string)

            except ValueError:
                pass

    if cat and summ:
        out["response"]["text"] =  f"Хорошо, записала в категорию: {cat}, {summ} рублей"
    else:
        out["response"][
            "text"] = f"Я не расслышала, можете повторить."

    return json.dumps(out)





@app.route('/post', methods=['GET'])
@app.route('/', methods=['GET'])
def inf():
    return "Тут должна быть информация"


if __name__ == '__main__':
    app.run(port=500, host='127.0.0.1')