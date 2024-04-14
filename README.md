# 3005-Project

Video: https://youtu.be/O5p4Sh5GoGA

Repo Organization
- Code (Python Code)
  - app.py
  - database_interface.py
- ProjectDocuments.pdf (Diagrams and explanation)
- SQL
  - DDL.sql (table creation)
  - DML.sql (sample data)

Prerequisites 
- Python3 downloaded
- PostgreSQL database server

Setup
- If need be "pip install psycopg2"
- Create a PostgreSQL database named 'FitForMoreGym'
- Execute the DDL.sql script to create the tables
- Exectue the DML.sql script to create sample data

Running the Application
- Within database_interface.py, locate the def connect_db(), change the user and password to your specific Postgre credentials
- Open terminal and run "python3 app.py" or any other way to run app.py
