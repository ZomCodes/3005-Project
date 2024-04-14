import database_interface
from random import randint

def display_members(): # This function is used to display all members in the system
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT memberID, name FROM Member")
    results = cursor.fetchall()
    database_interface.close_db(conn)  

    if results:
        print("Member List:")
        for member_id, name in results:
            print(f"ID: {member_id}, Name: {name}")
    else:
        print("No members found.")

def get_trainer_schedule(trainer_id): #This function is used to get all the sessions of a trainer
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT sessionID, memberID, time, roomID FROM Session WHERE trainerID = %s", (trainer_id,))
        results = cursor.fetchall()
        return results  # Return a list of sessions 
    except (Exception, psycopg2.Error) as error:
        print("Error fetching trainer schedule:", error)
        return []  # Return an empty list on error
    
def get_member_sessions(member_id): #This function is used to get all the sessions of a member
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT sessionID, trainerID, time, roomID FROM Session WHERE memberID = %s", (member_id,))
        results = cursor.fetchall()
        return results  # Return a list of sessions 
    except (Exception, psycopg2.Error) as error:
        print("Error fetching member sessions:", error)
        return []  # Return an empty list on error

def display_trainers(): #This function is used to display all trainers in the system
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT trainerID, name, availability FROM Trainer")
        results = cursor.fetchall()

        if results:
            print("Trainers:")
            for trainer_id, name, availability in results:
                print(f"ID: {trainer_id}, Name: {name}, Availability: {availability}")
        else:
            print("No trainers found.")
    except (Exception, psycopg2.Error) as error:
        print("Error fetching trainer data:", error)

def display_rooms(): #This function is used to display all rooms in the system
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT roomID, roomName FROM Room")
        results = cursor.fetchall()

        if results:
            print("Available Rooms:")
            for room_id, room_name in results:
                print(f"ID: {room_id}, Name: {room_name}")
        else:
            print("No rooms found.")
    except (Exception, psycopg2.Error) as error:
        print("Error fetching room data:", error)

def get_member_info(): #This function is used to get the information of a member
    name = input("Enter member name: ")
    goals = input("Enter fitness goals: ")
    metrics = input("Enter health metrics: ")
    return name, goals, metrics

def display_main_menu(menu_choice): #This function is used to display the main menu
    if menu_choice == '1':
        print("1. Add Member")
        print("2. Update Member Profile") 
        print("3. View Member Dashboard")
        print("4. Schedule Session")
        print("X. Exit")
   
   
    if menu_choice == '2':
        print("5. Set Trainer Availability")
        print("6. View Member Profile")
        print("X. Exit")
    
    if menu_choice == '3':
        print("7. Manage Room Bookings")
        print("8. Monitor Equipment Maintenance")
        print("X. Exit")

def update_member(): #This function is used to update the information of a member
    display_members()
    print("\n")
    member_id = input("Enter the ID of the member to update: ")
    name = input("Enter new name: ")
    goals = input("Enter new fitness goals: ")
    metrics = input("Enter new health metrics: ")

    try:
        database_interface.update_member_profile(member_id, name, goals, metrics)
    except (Exception, psycopg2.Error) as error:
        print("Error updating member profile:", error)

def view_member_dashboard(): #This function is used to view the dashboard of a member
    display_members()
    member_id = int(input("Enter member ID to view dashboard: "))

    try:
        name, goals, metrics = database_interface.get_member_dashboard_data(member_id)

        if name:
            print(f"\nMember Dashboard ({name}):")
            print("Fitness Goals:", goals)
            print("Health Metrics:", metrics)
        else:
            print("Member not found.")
    except (Exception, psycopg2.Error) as error:
        print("Error fetching member data:", error)

def schedule_session(): #This function is used to schedule a session
    display_members()
    session_id = randint(5, 100)
    member_id = int(input("Enter member ID: "))

    print("Member's Current Sessions:")
    sessions = get_member_sessions(member_id)  
    if sessions:
        for session in sessions:
            print(f"Session ID: {session[0]}, Time: {session[1]} ...")  
    else:
        print("No current sessions.")

    display_trainers()
    trainer_id = int(input("Enter trainer ID: "))

    print("Trainer's Current Schedule:")
    sessions = get_trainer_schedule(trainer_id)  
    if sessions:
        for session in sessions: 
            print(f"Session ID: {session[0]}, Time: {session[1]} ...")  
    else:
        print("No current sessions.")

    time_slot = input("Enter desired time slot (morning, noon, afternoon): ")

    display_rooms()
    room_id = int(input("Enter room ID: "))

    try:
        database_interface.schedule_session(session_id, member_id, trainer_id, time_slot, room_id)
    except (Exception, psycopg2.Error) as error:
        print("Error scheduling session:", error)

def set_trainer_availability(): #This function is used to set the availability of a trainer
    print("Select Trainer to Update Availability:")
    display_trainers()
    trainer_id = int(input("Enter trainer ID: "))

    print("Current Sessions:")
    sessions = get_trainer_schedule(trainer_id)
    if sessions:
        for session in sessions: 
            print(f"Session ID: {session[0]}, Time: {session[1]}, ...")
    else:
        print("No current sessions.")

    new_availability = input("Enter your availability for today (morning, noon, afternoon): ")

def view_member_profile(): #This function is used to view the profile of a member
    member_name = input("Enter member name: ")
    database_interface.view_member_profile(member_name)

def manage_room_bookings(): #This function is used to manage the bookings of a room
    display_rooms()  

    room_id = int(input("Enter the ID of the room to manage: "))

    print("Sessions in Selected Room:")
    display_sessions = database_interface.get_sessions_by_room(room_id)  
    if display_sessions:
        for session in display_sessions:
            # Display session details 
            print(f"Session ID: {session[0]}, Time: {session[1]} ...")
    else:
        print("No sessions found in this room.")

def monitor_equipment_maintenance(): #This function is used to monitor the maintenance of equipment
    conn = database_interface.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT equipmentID, equipmentName, status FROM Equipment")
        results = cursor.fetchall()

        if results:
            print("Equipment Maintenance Status:")
            for equipment_id, name, status in results:
                print(f"ID: {equipment_id}, Name: {name}, Status: {status}")
        else:
            print("No equipment found in the system.")
    except (Exception, psycopg2.Error) as error:
        print("Error fetching equipment maintenance data:", error)

if __name__ == "__main__":
    print("\nFitForMore Gym Management System\n")
    
    menu_choice = input("Are you a member (1), trainer (2), or admin (3)? (Enter 1, 2, or 3): ")
    
    if menu_choice == '1':
        print("Welcome to the Member Portal!")
    elif menu_choice == '2':
        print("Welcome to the Trainer Portal!")
    elif menu_choice == '3':
        print("Welcome to the Admin Portal!")

    while True:
        if menu_choice == '1':
            display_main_menu('1')

        if menu_choice == '2':
            display_main_menu('2')

        
        if menu_choice == '3':
            display_main_menu('3')
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name, goals, metrics = get_member_info() 
            database_interface.add_member(name, goals, metrics)

        
        if choice == '2':
            update_member()
        
        if choice == '3':
            view_member_dashboard()

        if choice == '4':
            schedule_session()

        if choice == '5':
            set_trainer_availability()

        if choice == '6':
            view_member_profile()

        if choice == '7':
            manage_room_bookings()

        if choice == '8':
            monitor_equipment_maintenance()

        if choice == 'X':
            break

    print("Thank you for using FitForMore Gym Management System!")

