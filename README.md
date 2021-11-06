# README

Backend-conductor is the proxy between frontend and solvers.

## Install
```shell
pip install -r requirements.txt
```

## Run server
```shell
flask run
```

## Send request
```shell
python examples/request_dummy.py
# output will be:
# {'info': None, 'result': 24, 'status': 'success'}

```

## (Pre-)commit
1. Install:
```sh
pip install pre-commit && pre-commit install
```
2. Run:
```sh
git add <FILES>
pre-commit run
git add <FIXED FILES>  # if necessary
git commit -m "MESSAGE"
```
