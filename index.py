from flask import Flask, request, render_template
from flask_cors import CORS
from static.dataPrepare import PrepareData

app = Flask(__name__)
cors = CORS(app)


@app.route('/receiver', methods=['POST'])
def RecievingData():
    data = request.get_json()
    mydocument = PrepareData(data)
    mydocument.myfunction()
    return data

@app.route('/')
def RenderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


