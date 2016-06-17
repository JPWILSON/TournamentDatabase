##About

This project models a swiss-pairings types tournament. With it, one can 
manage tournaments (that is, tracking matches, leaders, adding and deleting players and 
determing the winner and overall standings).
It is a PostgreSQL database with python modules that allow manipulation of the database. 


  It contains the basic functionality and in addition:
  	- Allows for draws instead of only wins and losses
      (A win gets 2 points, a draw gets 1 point, a loss gets 0 points)
  	- Allows for multiple tournaments to be played
  It contains the following files:
  	- Schema Diagram.jpg * this is a visualisation of the four tables and how the 
                              are related
  	- tournament.py 		 * this contains my python functions to query the database
  	- tournament.sql 		 * this contains my database schema, with four tables. 
  	- populate.py 			 * this may not be necessary, but explains how I populated
  							           my database during testing and development
  	- tournament_test.py * this contains the UPDATED test suite, provided by Udacity.
                           The changes to this file are listed at the TOP of this README


##How To Use

- Get started by installing the dev env (vagrant up, ssh, etc). Open psql, i\ tournament.sql, then
    run the populate.py or the tournament_test.py files to check that it works as required.  
- This may be obvious, but, there is no redundant code in the comments, and everything can be used, as per the explanations in the comments. 
- Please read the comments in the code, they are exhaustive, to the point of tedium,
  but at the very least, should eliminate confusion on what my code does, and how it does this. 
- Ensure that Python is installed on the machine running these modules. (2.7 or later) 
- Make sure that the relevant python modules are located in the same folder
- Run the various functions in tournament.py to test the funcionality of the database.
  Note that populate.py and tournament_test.py may assist in checking the functionality. 


##Project Explanation

The project will i. allow for draws ii. accomodate multiple tournaments. 

Additional functions in tournament.py are required for the added functionality. Those added are: 
   - countPlayersTournament()
   - registerPlayerTourney()
   - registerTourney()
   - winnerTourney()
   - playerStandings_tourney() - commented out for ease of testing. 



##Contributing

I will load this on GitHub and then happilly welcome anyone to provide any constructive 
criticism of this project in particular, or my coding in general. I just want to get better. 
(This updated submission is not yet updated to GITHub, rather, I will submit after grading of the project, in case there are further errors.)


##License

tl;dr - The MIT License (MIT)

So, I don't really care about trying to own information, this isn't the 90s.
Do what you like with this or anything else as I don't think anyone can actually own information, just because current laws say that they can. I mean, who am I to say who can
know what, or who on earth thinks they can dictate what my mind is allowed to know...
So, take this and use it, and any other code I write. 


##Add Later

This is still a tiny little repository, but as it grows I intend to add:
-FAQ
-Table of Contents
