from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

def insert_match(match_id):
    """
    Takes Match json object and inserts the data into the database
    """
    engine = create_engine('sqlite:///data\\dota_analysis.db', echo=True)
    Session = sessionmaker(bind=engine)
    session= Session()

    match = Matches(
        match_id = r['match_id'],
        barracks_status_dire = r['barracks_status_dire'],
        barracks_status_radiant = r['barracks_status_radiant'],
        cluster = r['cluster'],
        dire_score = r['dire_score'],
        dire_team_id = r['dire_team_id'],
        duration = r['duration'],
        engine = r['engine'],
        first_blood_time = r['first_blood_time'],
        game_mode = r['game_mode'],
        human_players = r['human_players'],
        leagueid = r['leagueid'],
        lobby_type = r['lobby_type'],
        match_seq_num = r['match_seq_num'],
        negative_votes = r['negative_votes'],
        positive_votes = r['positive_votes'],
        radiant_score = r['radiant_score'],
        radiant_team_id = r['radiant_team_id'],
        radiant_win = r['radiant_win'],
        skill = r['skill'],
        start_time = r['start_time'],
        tower_status_dire = r['tower_status_dire'],
        tower_status_radiant = r['tower_status_radiant'],
        version = r['version'],
        replay_salt = r['replay_salt'],
        series_id = r['series_id'],
        series_type = r['series_type'],
        patch = r['patch'],
        region = r['region'],
        throw = r['throw'],
        comeback = r['comeback'],
        loss = r['loss'],
        win = r['win'],
        replay_url = r['replay_url']

    )

    session.add(match)
    session.commit()
    session.close()

def create_db():
    """
    Create DB for storing match data.
    """
    engine = create_engine('sqlite:///data\\dota_analysis.db', echo=True)
    Base = declarative_base()

    class Matches(Base):

        __tablename__ = 'matches'

        match_id = Column(Integer, primary_key=True)
        barracks_status_dire = Column(Integer)
        barracks_status_radiant = Column(Integer)
        cluster = Column(Integer)
        dire_score = Column(Integer)
        dire_team_id = Column(Integer)
        duration = Column(Integer)
        engine = Column(Integer)
        first_blood_time = Column(Integer)
        game_mode = Column(Integer)
        human_players = Column(Integer)
        leagueid = Column(Integer)
        lobby_type = Column(Integer)
        match_seq_num = Column(Integer)
        negative_votes = Column(Integer)
        positive_votes = Column(Integer)
        radiant_score = Column(Integer)
        radiant_team_id = Column(Integer)
        radiant_win = Column(Integer)
        skill = Column(Integer)
        start_time = Column(Integer)
        tower_status_dire = Column(Integer)
        tower_status_radiant = Column(Integer)
        version = Column(Integer)
        replay_salt = Column(Integer)
        series_id = Column(Integer)
        series_type = Column(Integer)
        patch = Column(Integer)
        region = Column(Integer)
        throw = Column(Integer)
        comeback = Column(Integer)
        loss = Column(Integer)
        win = Column(Integer)
        replay_url = Column(String(50))
        radiant_heroes = Column(String(50))
        dire_heroes = Column(String(50))

    # class Chat(Base):
    #
    #     __tablename__ = 'chat'
    #
    # class Cosmetics(Base):
    #
    #     __tablename__ = 'cosmetics'
    #
    # class Draft(Base):
    #
    #     __tablename__ = 'draft'
    #
    # class Objectives(Base):
    #
    #     __tablename__ = 'objectives'
    #
    # class PicksBans(Base):
    #
    #     __tablename__ = 'picks_bans'
    #
    # class RadiantGoldAdv(Base):
    #
    #     __tablename__ = 'radiant_gold_adv'
    #
    # class RadiantXPAdv(Base):
    #
    #     __tablename__ = 'radiant_xp_adv'
    #
    # class Teamfights(Base):
    #
    #     __tablename__ = 'teamfights'
    #
    # class RadiantTeam(Base):
    #
    #     __tablename__ = 'radiant_team'
    #
    # class DireTeam(Base):
    #
    #     __tablename__ = 'dire_team'
    #
    # class WordCounts(Base):
    #
    #     __tablename__ = 'all_word_counts'


    Base.metadata.create_all(engine)
