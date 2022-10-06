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
API_CHALLENGE_BASE_URL = "https://na1.api.riotgames.com/lol/challenges/v1/challenges/"
champion_list = []
challenge_list = []

connect_db(app)
@app.route('/create')
def create():
    db.create_all()
    return 'tables created'


@app.route('/')
def show_homepage():
    
    return render_template("index.html")


@app.route('/champions')
def show_champions():
    champions = Champion.query.all()
    
    return render_template("champions.html", champions = champions)

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

@app.route('/challenges')
def show_challenges():
    
    return render_template("challenges.html", challenges = challenge_list)

@app.route('/challenges/get')
def get_challenges():
    res = requests.get(f"{API_CHALLENGE_BASE_URL}/config", params={ "X-Riot-Token": f"{API_SECRET_KEY}"})
    challenge = res.data
    # add_challenge(challenge.)
    
    return redirect('/challenges')
    