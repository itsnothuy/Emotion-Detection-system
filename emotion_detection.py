import json
import requests 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document" : { "text" : text_to_analyse}}

    header = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Print the full response for debugging purposes
    print("Full API response:", formatted_response)

    # Extract emotions and their scores
    emotions = formatted_response.get('emotion_predictions', [{}])[0]  # Check for a key that holds emotions data

    # Correctly initialize emotion scores
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }
    
    # Check if all scores are zero, handle the case
    if all(score == 0 for score in emotion_scores.values()):
        emotion_scores['dominant_emotion'] = 'none'
    else:
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
    
    # Return the formatted output
    return emotion_scores

