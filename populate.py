#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

DB = psycopg2.connect("dbname = tournament")
c = DB.cursor()
#Add a tournament
c.execute("INSERT INTO tournaments(name) VALUES('ChessTournament')")
DB.commit()
c.execute("SELECT * FROM tournaments;")
result = c.fetchall()
tourney_id = result[0][0]

#Add players to the players table 
c.execute("INSERT INTO players(name) VALUES('J Player1 Wilson');")
c.execute("INSERT INTO players(name) VALUES('R Player2 Beater');")
c.execute("INSERT INTO players(name) VALUES('T Player3 Howard');")
c.execute("INSERT INTO players(name) VALUES('W Player4 Rourke');")
c.execute("INSERT INTO players(name) VALUES('V Player5 Tedds');")
c.execute("INSERT INTO players(name) VALUES('H Player6 Mat');")
c.execute("INSERT INTO players(name) VALUES('U Player7 Willows');")
c.execute("INSERT INTO players(name) VALUES('R Player8 Talbot');")
DB.commit()
#Record matches
c.execute("INSERT INTO matches VALUES(%s,1,2,2,0);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,3,4,0,2);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,5,6,1,1);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,7,8,0,2);",(tourney_id,))

c.execute("INSERT INTO matches VALUES(%s,1,4,0,2);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,8,5,2,0);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,6,2,2,0);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,3,7,1,1);",(tourney_id,))

c.execute("INSERT INTO matches VALUES(%s,4,8,0,2);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,6,1,1,1);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,5,3,0,2);",(tourney_id,))
c.execute("INSERT INTO matches VALUES(%s,7,2,2,0);",(tourney_id,))
DB.commit()
#Insert all players and 'ChessTournament's id into tournament_players
c.execute("INSERT INTO tournament_players VALUES(%s,1) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,2) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,3) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,4) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,5) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,6) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,7) ;",(tourney_id,))
c.execute("INSERT INTO tournament_players VALUES(%s,8) ;",(tourney_id,))

DB.commit()
DB.close()