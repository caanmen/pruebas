from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/news', methods=['GET'])
def get_news():
    news = [
        {
            "title": "¿Por qué hay crisis en las manifestaciones?",
            "content": "El pasado jueves 25 de julio la policía disparó contra estudiantes de la universidad Nacional que se encontraban manifestándose.",
            "date_posted": "2024-07-25",
            "image_url": "https://example.com/image1.jpg"
        }
    ]
    return jsonify(news)

@app.route('/events', methods=['GET'])
def get_events():
    events = [
        {
            "title": "Pachanga Solidaria",
            "description": "Un evento de recaudación para apoyar proyectos sociales.",
            "event_date": "2024-08-01",
            "image_url": "https://example.com/event1.jpg"
        },
        {
            "title": "Gran Re-inauguración",
            "description": "Celebración especial con actividades para toda la familia.",
            "event_date": "2024-08-15",
            "image_url": "https://example.com/event2.jpg"
        }
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
