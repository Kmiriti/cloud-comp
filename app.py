from flask import Flask, request, jsonify
import pickle
import os
import time

app = Flask(__name__)

MODEL_PATH = os.getenv("MODEL_PATH", "/mnt/pvc/model.pkl")
app.model = pickle.load(open(MODEL_PATH, "rb"))
app.config['VERSION'] = "1.0"
app.config['MODEL_DATE'] = time.ctime(os.path.getmtime(MODEL_PATH))

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_songs = data['songs']

    # reccommendation logic
    recommendations = []  # Replace with actual logic to generate recommendations
    for rule in app.model:
        #do user's song match any rule?
        if set(user_songs).issubset(set(rule[0])):
            recommendations.extend(rule[1])


    return jsonify({
        "songs": recommendations,
        "version": app.config['VERSION'],
        "model_date": app.config['MODEL_DATE']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52003)