from app import db
from models import Champion, Tier, Region, Challenge, Map
db.drop_all()
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

