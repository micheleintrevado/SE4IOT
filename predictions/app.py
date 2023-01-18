import json
from flask import Flask
from components.model import Model

app = Flask(__name__)

@app.route('/predictions/solar/<value>', methods=['GET'])
def index(value):
    value = int(value)
    value = 10 if value > 10 else value
    value = 0 if value < 0 else value
    model = Model()
    predicted_value = model.predict(value)
    return json.dumps(predicted_value)

app.run(debug=True, host='172.20.0.105', port=5000)
