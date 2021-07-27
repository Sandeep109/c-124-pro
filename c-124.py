from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    {
        "id":1,
        "Contact": "8194674464",
        "name": "Rahul",
        "done": False
    },
    {
        "id":2,
        "Contact": "9865327845",
        "name": "Tina",
        "done": False
    }
]
@app.route('/add-data',methods=['POST'])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please Provide data"
        },400)
    task = {
        "id": tasks[-1]["id"]+1,
        "Contact": request.json["Contact"],
        "name": request.json.get("name",""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added Successfully"
    })

@app.route("/get-data")
def getTask():
    return jsonify({
        "data": tasks
    })

if(__name__ == '__main__'):
    app.run(debug = True)