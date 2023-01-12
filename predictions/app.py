import json
from flask import Flask

from components.model import Model

app = Flask(__name__)


@app.route('/predictions/solar/<value>', methods=['GET'])
def index(value):
    model = Model()
    predicted_value = model.predict(int(value))
    return json.dumps(predicted_value)


app.run()
