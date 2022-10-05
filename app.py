from secrets import API_SECRET_KEY
from flask import Flask, render_template,request, redirect, flash
from forms import GetDataForm
from models import db, connect_db, Champion, Tier, Region, Challenge, Map
import requests

key = API_SECRET_KEY
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql:///riotchallenges')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
API_BASE_URL = "americas.api.riotgames.com"
API_CHALLENGE_BASE_URL = "https://na1.api.riotgames.com/lol/challenges/v1/challenges/"
champion_list = []
challenge_list = []

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template("index.html")
    form = GetDataForm()

@app.route('/champions')
def show_champions():

    return render_template("champions.html", champions = champion_list)

@app.route('/champions/get')
def get_champions():
    res = requests.get("http://ddragon.leagueoflegends.com/cdn/12.18.1/data/en_US/champion", 
        params={ "X-Riot-Token": f"{API_SECRET_KEY}"})
    for champion in res.data:
        champion_list.push(champion)
        add_champion(champion.name, f"/static/img/tiles/{champion.id}_0.jpg")
    
    return redirect('/champions')

@app.route('/challenges')
def show_challenges():
    
    return render_template("challenges.html", challenges = challenge_list)

@app.route('/challenges/get')
def get_challenges():
    res = requests.get(f"{API_CHALLENGE_BASE_URL}/config", params={ "X-Riot-Token": f"{API_SECRET_KEY}"})
    challenge = res.data
    add_challenge(challenge.)
    
    return redirect('/challenges')
    