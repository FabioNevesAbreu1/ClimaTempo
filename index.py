from flask import Flask
from flask import request
import json
import os

app = Flask(__name__)

@app.route("/register", methods=['POST'])
# route for create user
def createUser():
    # open the txt file
    file = open("users.txt", 'a')
    # get the size of user txt file
    fileLenght = os.path.getsize('users.txt')
    if fileLenght == 0:
        file.write(json.dumps(request.get_json()))
    else:
        file.write("\n"+json.dumps(request.get_json()))
    # close file
    file.close()
    return "User registred"

@app.route("/routine", methods=['POST'])
# run routine
def routine(): 
    # get body data
    body = request.get_json()
    # open and read users data
    with open("users.txt") as file:
        for line in file:
            # parse user data
            userData = json.loads(line.rstrip())
            # verify if user neighborhood is the same as the message send
            if body['neighborhood'] == userData['neighborhood']:
                # TODO: effectively send the message in user mail
                print(f"Mensagem mandada para o email: {userData['mail']} contendo a mensagem: Atenção {userData['name']}, no dia {body['date']}, no bairro {userData['neighborhood']}, {body['message']}")

    return "Routine done!"
