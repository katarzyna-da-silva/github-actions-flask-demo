# multi_language.py
from flask import Flask, request
#import logging
#import pdb
import time 
app = Flask(__name__)  # instance de l'application Flask

@app.route('/') # Définit une route pour l'adresse '/'
def hello_world():
    return """
    <h1>Hello, World!</h1>
    <p>Bonjour, le Monde!</p>
    <p>Hola, Mundo!</p>
    <p>Ciao, Mondo!</p>
    <p>你好，世界！</p>
    <p>Привет, мир!</p>
    """

@app.route('/greet/<lang>')
def greet_in_language(lang):
    greeting = get_greeting_in_language(lang)
    return f"<h2>{greeting}</h2>"

def get_greeting_in_language(lang):
    # Prosty przykład - dodaj więcej języków w razie potrzeby
    greetings = {
        'fr': 'Bonjour!',
        'es': '¡Hola!',
        'it': 'Ciao!',
        'zh': '你好!',
        'ru': 'Привет!',
    }
    return greetings.get(lang, 'Hello!')

if __name__ == '__main__':
    time.sleep(5)
    app.run(host='0.0.0.0', port=8083, debug=False)

#logging.basicConfig(level=logging.DEBUG)
#if __name__ == '__main__':
#    pdb.set_trace()
#    app.run(host='0.0.0.0', port=8080, debug=False)