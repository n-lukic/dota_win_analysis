from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
