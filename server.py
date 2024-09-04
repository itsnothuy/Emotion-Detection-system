from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text_to_analyse = request.json.get("text", "")
    if not text_to_analyse:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    result = emotion_detector(text_to_analyse)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
