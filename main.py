from flask import*
app=Flask(__name__)

@app.route("/iris-get")
def get_iris():
    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    return jsonify({
        "message":"Iris Dataset",
        "data": iris.to_dict()
    })

if __name__ == "__main__":
    app.run(debug=True,port="8000")