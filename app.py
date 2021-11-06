import solver_dummy
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/solver/<solvername>", methods=["POST"])
def solver(solvername):

    request_json = request.get_json()

    if solvername == "dummy":
        response = solver_dummy.handle_request(request_json)

    # elif solvername == "some_other_solver"
    #     response = some_other_solver.handle_request(request_json)

    else:
        response = {"status": "failed", "info": f"Unknown solver: {solvername}"}

    return response
