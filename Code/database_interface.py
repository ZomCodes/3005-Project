import psycopg2
from random import randint


def connect_db(): # This function is used to connect to the database
    conn = psycopg2.connect(
        database="FitForMoreGym", 
        user="postgres",
        password="John10",
        host="localhost",  
        port="5432"
    )
    return conn

def close_db(conn): # This function is used to close the connection to the database
    conn.close()

def add_member(name, goals, metrics): #This function is used to add a member to the system
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nextval('member_id_seq')")  
        new_member_id = randint(5,100)
        cursor.execute("INSERT INTO Member (memberID, name, fitnessGoals, healthMetrics) VALUES (%s, %s, %s, %s)", (new_member_id, name, goals, metrics))
        conn.commit()
        print("Member added successfully! Member ID:", new_member_id)
    except (Exception, psycopg2.Error) as error:
        print("Error adding member:", error)
    finally:
        close_db(conn)  

def update_member_profile(member_id, name, goals, metrics): #This function is used to update the profile of a member
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Member SET name = %s, fitnessGoals = %s, healthMetrics = %s WHERE memberID = %s",
            (name, goals, metrics, member_id)
        )
        conn.commit()
        print("Member profile updated successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error updating member profile:", error)
    finally:
        close_db(conn)

def get_member_dashboard_data(member_id):   #This function is used to get the dashboard data of a member
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name, fitnessGoals, healthMetrics FROM Member WHERE memberID = %s", (member_id,))
        result = cursor.fetchone()

        if result:
            name, goals, metrics = result
            return name, goals, metrics
        else:
            return None  
    except (Exception, psycopg2.Error) as error:
        print("Error fetching member data:", error)
        return None  # Handle errors
    finally:
        close_db(conn)

def schedule_session(session_id, member_id, trainer_id, time, room_id): #This function is used to schedule a session
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Session (sessionID, memberID, trainerID, time, roomID) VALUES (%s, %s, %s, %s, %s)",
               (session_id, member_id, trainer_id, time, room_id))
        conn.commit()
        print("Session scheduled successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error scheduling session:", error)
    finally:
        close_db(conn)

def view_member_profile(member_name): #This function is used to view the profile of a member
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT memberID, name, fitnessGoals, healthMetrics FROM Member WHERE name ILIKE %s", (f"%{member_name}%",))  
        results = cursor.fetchall()

        if results:
            print("Member Profiles (Partial Matches):")
            for member_id, name, goals, metrics in results:
                print(f"\nID: {member_id}, Name: {name}")
                print(f"  Goals: {goals}")
                print(f"  Metrics: {metrics}")
        else:
            print("No members found with that name.")
    except (Exception, psycopg2.Error) as error:
        print("Error fetching member profile:", error)

def get_sessions_by_room(room_id): #This function is used to get all the sessions in a room
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT sessionID, memberID, trainerID, time, roomID FROM Session WHERE roomID = %s", (room_id,))
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error fetching sessions by room:", error)
        return []  
    finally:
        close_db(conn)



