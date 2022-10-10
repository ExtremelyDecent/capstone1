from secretkey import API_SECRET_KEY, SECRET_KEY
from flask import Flask, render_template,request, redirect, flash, session
# from forms import GetDataForm
from models import db, connect_db, Champion, Tier, Region, Challenge, Map
import requests

KEY = API_SECRET_KEY
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///riotchallenges'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = f"{SECRET_KEY}"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['FLASK_DEBUG'] = True
API_BASE_URL = "americas.api.riotgames.com"
JSON_LEAGUE_VERSION = '12.19.1'
API_CHALLENGE_BASE_URL = "https://na1.api.riotgames.com/lol/challenges/v1/challenges/config"
champion_list = []
challenge_list = []

connect_db(app)
@app.route('/create')
def create():
    db.create_all()
    db.session.add_tier("IRON")
    db.session.add_tier("BRONZE")
    db.session.add_tier("SILVER")
    db.session.add_tier("GOLD")
    db.session.add_tier("PLATINUM")
    db.session.add_tier("DIAMOND")
    db.session.add_tier("MASTER")
    db.session.add_tier("GRANDMASTER")
    db.session.add_tier("CHALLENGER")
    db.session.commit()
    return 'tables created'


@app.route('/')
def show_homepage():
    
    return render_template("index.html")


@app.route('/champions')
def show_champions():
    champions = Champion.query.all()
    
    return render_template("champions/show.html", champions = champions)

@app.route('/champions/populate')
def get_champions():
    res = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{JSON_LEAGUE_VERSION}/data/en_US/champion.json")
    
    champions = res.json()
    print(champions['data'])
    for champion in champions['data']:
        
        champion_name = champions['data'][f"{champion}"]['name']
        print(champion_name)
        Champion.add_champion(champion_name, f"/static/img/tiles/{champion}_0.jpg")
    db.session.commit()
    return redirect('/champions')
@app.route('/champions/<champion_id>')
def show_champion_details(challenge_id):
    champion = Champion.query.get(champion_id)

    return render_template("champions/details.html")


@app.route('/challenges')
def show_challenges():
    challenges = Challenge.query.all()
    
    return render_template("challenges.html", challenges = challenges)
@app.route('/challenges/<challenge_id>')
def show_challenge_details(challenge_id):
    challenge = Challenge.query.get(challenge_id)

    return render_template("challenges/details.html")
    
@app.route('/challenges/populate')
def get_challenges():
    res = requests.get(f"{API_CHALLENGE_BASE_URL}?api_key={API_SECRET_KEY}")
    challenges = res.json()
    for challenge in challenges:
        challenge_id = challenge['id']
        challenge_name = challenge['localizedNames']['en_US']['name']
        challenge_description = challenge['localizedNames']['en_US']['description']
        # challenge_image = f"/static/img/challenge_tiles/{challenge_id}-BRONZE"
        print(f"{challenge_id} - {challenge_name} - {challenge_description}")
        # Challenge.add_challenge(parseInt(challenge_id), challenge_name, challenge_description)

    # add_challenge(challenge.)
    
    return redirect('/challenges')
    