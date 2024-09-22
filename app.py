from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/get-data',methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request"})
@app.route('/post-data',methods=['POST'])
def post_data():
    data=request.json
    return jsonify({"message": "This is a POST request","data_received":data})
if __name__=="__main__":
    app.run(debug=True)
