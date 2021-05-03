#Muhammad Tariq
#A9.2
#https://github.com/iamsheraz/csd-310

import mysql.connector
from mysql.connector import errorcode



config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
   

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES ('Jon', 'Cena', 1)")


    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()


    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")
    

    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Aqua', last_name = 'Man' WHERE first_name = 'Jon'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")

    cursor.execute("DELETE FROM player WHERE first_name = 'Jon'")
    cursor.execute("DELETE FROM player WHERE first_name = 'Cena'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

    

   





except mysql.connector.Error as err:
 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    
    db.close()
