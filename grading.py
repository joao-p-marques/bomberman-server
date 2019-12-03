from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_url_path='')
basedir = os.path.abspath(os.path.dirname(__file__))

SUM = 0
COUNT = 0

# endpoint to create new game
@app.route("/game", methods=["POST"])
def add_game():
    global SUM
    global COUNT
    player = request.json['player']
    level = request.json['level']
    score = request.json['score']

    s = f'Player {player} reached level {level} with {score} points'
    with open('level.log', 'a') as f:
        f.write(s + '\n')

    print(s)

    SUM += level
    COUNT += 1

    return jsonify({'type' : 'OK'})

# return average
@app.route("/avg", methods=['GET'])
def avg():
    global SUM
    global COUNT
    average = SUM/COUNT
    SUM = 0
    COUNT = 0
    s = f'Average: {average}'
    print(s)
    with open('level.log', 'a') as f:
        f.write(s + '\n')
    return jsonify({'average': average})

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8080)
