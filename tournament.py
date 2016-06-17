#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

#For deleteMatches(), it can be seen by looking at the schema
#    that none of the other 3 tables contain match data and therefore,
#    only the match table needs to be cleared (deleted):
def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect('dbname=tournament')
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()

# Player data is found in all three of the other tables, and therefore all 
#     three tables need their player data cleared. 
def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect('dbname = tournament')
    c = DB.cursor()
    c.execute("DELETE FROM tournament_players;")
    c.execute("DELETE FROM tournaments;")
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()

# For extra credit, as there is support for multiple tournaments, 
#   I have assumed that countPlayers() returns the number of registered 
#   players for ALL tournaments.
def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect('dbname = tournament')
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    no_players = c.fetchone()
    DB.close()
    return no_players[0]

# In case only the players from a certain tournament are required another function, 
#   countPlayersTournament() will return "the number of players 
#   who have entered in tournament #123"...
def countPlayersTournament(tourn_id):
    """Returns the number of players who have entered in tournament 'tourn_id'  """
    DB = psycopg2.connect('dbname = tournament')
    c = DB.cursor()
    c.execute("SELECT COUNT(player_id) FROM tournament_players WHERE tournament_id = (%s);", (tourn_id,))
    no_players = c.fetchone()
    DB.close()
    return no_players[0]

# The function below will add a player to the players table. 
#   Also added another function 'registerPlayerTourney' below,
#   that adds the player to the tournament_players table.
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO players(name) VALUES(%s);", (name,))
    DB.commit()
    DB.close()


# Now, for the extra credit component, the function 'registerPlayerTourney'
#   will allow (provided the players id, and the tournament's id are known) players to be 
#   added to the tournament_players table, which keeps track of which players are registered 
#   for each tournament.
def registerPlayerTourney(tournament_id, player_id):
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO players(tournament_id, player_id) VALUES(%s,%s);", (tournament_id, player_id,))
    DB.commit()
    DB.close()

# An additional requirement is the funcionality to include a tournament to the database:
def registerTourney(name):
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO tournaments(name) VALUES(%s);", (name,))
    DB.commit()
    DB.close()

# Also, each tournament requires a winner to be added, once the final playerStandings function has been run:
def winnerTourney(winner_id):
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO tournaments(winner_id) VALUES(%s);", (winner_id,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT id, name, wins, match FROM v_r_standings;")
    current_standings = c.fetchall()
    DB.close()
    #print current_standings
    return current_standings

'''playerStandings should take an argument specifying the tournament_id 
so that only players from that match are selected. This is shown here: 
def playerStandings_tourney(tournament_id):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT id, name, wins, match FROM v_r_standings WHERE tournament_id = %s;", (tournament_id,))
    current_standings = c.fetchall()
    DB.close()
    #print current_standings
    return current_standings
'''

def reportMatch(tournament_id, player1_id, player2_id, player1_result, player2_result):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname= tournament")
    c = DB.cursor()
    c.execute("INSERT INTO matches VALUES(%s,%s,%s,%s,%s);", (tournament_id, player1_id, player2_id, player1_result, player2_result,))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("SELECT id, name FROM v_r_standings ;")
    result = c.fetchall()
    DB.close()
    list_of_tuples = []
    count = 1
    for e in range(len(result)/2):
        list_of_tuples.insert(0,(result[count-1][0],result[count-1][1],result[count][0],result[count][1],))
        count += 2
    print list_of_tuples    
    return list_of_tuples
    
