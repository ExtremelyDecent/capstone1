
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)


class Champion(db.Model):
    """All champions currently available for play"""
    __tablename__ = "champions"

    champion_id = db.Column(
        db.Integer,
        primary_key = True
    )
    champion_name = db.Column(
        db.Text,
        nullable = False,
        unique = True  
    )
    # region_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('regions.regions_id', ondelete = 'cascade')
    # )
    champion_image_url = db.Column(
        db.Text,
        nullable = False,
    )
    # champion_role_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('role.role_id', ondelete= 'cascade')
    # )
    @classmethod
    def add_champion(cls, champion_name, champion_image_url):
        champion = Champion(
            champion_name = champion_name,
            champion_image_url = champion_image_url
        )
        db.session.add(champion)




class Challenge(db.Model):
    """Challenges curretly available in game"""
    __tablename__ = "challenges"

    challenge_id = db.Column(
        db.Integer,
        primary_key = True
    )
    challenge_name = db.Column(
        db.Text,
        nullable = False,
        unique = True  
    )
    # challenge_region_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('regions.region_id', ondelete = 'cascade')
    # )
    challenge_image_url = db.Column(
        db.Text,
        nullable = False,
    )
    # challenge_role_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('role.role_id', ondelete= 'cascade')
    # )
    # challenge_map_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('map.map_id', ondelete = 'cascade')
    # )
    # challenge_tier_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('tier.tier_id', ondelete = 'cascade')
    # )

    @classmethod
    def add_challenge(cls, challenge_name, challenge_image_url):
        challenge = Challenge(
            challenge_name = challenge_name,
            challenge_image_url = challenge_image_url
        )
        db.session.add(challenge)



class Region(db.Model):
    """Champion regions"""
    __tablename__ = "regions"

    region_id = db.Column(
        db.Integer,
        primary_key = True
    )
    region_name = db.Column(
        db.String(20),
        nullable=False,
        unique = True
    )
    region_image_url = db.Column(
        db.Text,
        nullable = False,
    )

class Map(db.Model):
    """Maps"""
    __tablename__ = "maps"

    map_id = db.Column(
        db.Integer,
        primary_key = True
    )
    map_name = db.Column(
        db.String(20),
        nullable=False,
        unique = True
    )

class Tier(db.Model):
    """Challenge tiers"""
    __tablename__ = "tier"

    tier_id = db.Column(
        db.Integer,
        primary_key = True
    )
    tier_name = db.Column(
        db.String(20),
        nullable=False,
        unique = True
    )
    tier_image_url = db.Column(
        db.Text,
        nullable = False,
    )
    tier_xp_max = db.Column(
        db.Integer,
        nullable = False
    )
class Role(db.Model):
    """Challenge tiers"""
    __tablename__ = "roles"

    role_id = db.Column(
        db.Integer,
        primary_key = True
    )
    role_name = db.Column(
        db.String(20),
        nullable=False,
        unique = True
    )
    role_image_url = db.Column(
        db.Text,
        nullable = False,
    )