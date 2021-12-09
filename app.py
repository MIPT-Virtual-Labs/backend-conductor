import solver_dummy
import json
from time import sleep
import solver_gas_dynamics_1d
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
@cross_origin()
def hello_world():
    return {'result': 'ok'}


@app.route("/solver/<solvername>", methods=["POST"])
@cross_origin()
def solver(solvername):
    print(5, request)
    request_json = request.get_json(force=True)
    print(request_json)
    sleep(1)
    # return {'result': 'ok'}

    if solvername == "dummy":
        response = solver_dummy.handle_request(request_json)

    elif solvername == "gas_dynamics_1d":
        response = solver_gas_dynamics_1d.handle_request(request_json)

    else:
        response = {
            "status": "error",
            "errors": [
                {"error": f"unknown solver: {solvername}", "field": "solvername"}
            ],
        }
    # print("ANSWER:", jsonify(response))
    r1 = jsonify(response)
    r1.status_code = 200
    r1.headers = {"Content-Type": "application/json"}
    res = Response(response=json.dumps(response), status=200, mimetype='application/json')
    # print(res)
    return r1
