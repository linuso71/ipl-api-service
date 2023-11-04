from flask import Flask,jsonify,request
import ipl
import jugaad

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/api/teams')
def teams():
    teams = ipl.teams()
    return jsonify(teams)

@app.route('/api/teamvteam')
def temvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteam(team1,team2)

    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')

    response = jugaad.teamAPI(team_name)
    return response

@app.route('/api/batsman-record')
def batsman_record():
    batsman = request.args.get('batsman')
    response = jugaad.batsmanAPI(batsman)
    return response

@app.route('/api/bowler-record')
def bowler_record():
    bowler = request.args.get('bowler')
    response = jugaad.bowlerAPI(bowler)
    return response


app.run(debug=True)

