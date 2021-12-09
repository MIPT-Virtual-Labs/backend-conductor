import solver_dummy
import solver_gas_dynamics_1d
from flask import Flask, request
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

    request_json = request.get_json()
    print(request_json)

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

    return response
