'''Testing SQLAlchemy Helper Functions'''
import pytest
from datetime import date

import crud
from database import SessionLocal

# use a test date of 4/1/2024 to test the min_last_changed_date.
test_date = date(2024,4,1)

@pytest.fixture(scope = "function")
def db_session():
    """This starts a database session and closes it when done"""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player (db_session):
    """Tests you can get the first player"""
    player = crud.get_player(db_session, player_id = 101)
    assert player.player_id==101

def test_get_players_by_name (db_session):
    """Tests that the count of players in the database is what is expectedr"""
    players = crud.get_players (db_session, first_name = "Bryce", last_name = "Young")
    assert len (players) == 1
    assert players[0].player.id == 102

def test_get_all_perfromances(db_session):
    """Test that the count of performances in the database is what is expected - all the performances"""
    performances = crud.get_performances (db_session, skip = 0, limit = 10000)
    assert len(performances) == 1100

def test_get_half_performances(db_session):
    """Tests that the count of performances in the database is what is expected - half the performances"""
    performances = crud.get_performances(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(performances) == 550

#test the count functions
def test_get_player_count(db_session):
    player_count = crud.get_player_count(db_session)
    assert player_count == 550