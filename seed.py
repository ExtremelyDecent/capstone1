from app import db
from models import Champion, Tier, Region, Challenge, Map
db.drop_all()
db.create_all()

res = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{JSON_LEAGUE_VERSION}/data/en_US/champion.json")

champions = res.json()
print(champions['data'])
for champion in champions['data']:
    
    champion_name = champions['data'][f"{champion}"]['name']
    print(champion_name)
    Champion.add_champion(champion_name, f"/static/img/tiles/{champion}_0.jpg")

db.session.commit()

