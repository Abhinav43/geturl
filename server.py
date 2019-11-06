from flask import Flask,request,jsonify
from flask_cors import CORS
# from chatter import chat
from get_ur import get_url

# app = Flask(__name__)



app = Flask(__name__)


@app.route('/urls',methods=['POST'])
def _predict():
    query = request.json["reply"]
    try:
        result = chat(query)
        return jsonify({"prediction" : result})
    except Exception as e:
        print(e)
        return jsonify({"result" : "model failed"})

    
if __name__ == '__main__':
    app.run(port= 8073 ,debug=True)
