from flask import Flask,jsonify

app=Flask(__name__)
@app.get("/")
def hello():
    return jsonify(
        mmessage="Student api",
        tip="Build with falsk, shinnped by jenkins"
    )

@app.get("/hi")
def newEndpoint():
    return jsonify(
        mmessage="Student api",
        tip="new Endpoint"
    )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)