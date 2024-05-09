import cx_Oracle
import dotenv

username = dotenv.get_key('.env', 'DB_USER')
password = dotenv.get_key('.env', 'DB_PASSWORD')
dsn = "172.16.64.222:1522/orclpdb"


try:
    global connection
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("Connection to Oracle database established successfully.")
except cx_Oracle.DatabaseError as e:
    print("Error connecting to Oracle database:", e)

def disconnect_from_database(connection):
    """Closes the connection to the Oracle database."""
    connection.close()

def execute_sql_query(connection, query):
    """Executes an SQL query and returns the result."""
    cursor = connection.cursor()
    print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def execute_sql_statement(connection, statement):
    """Executes an SQL statement."""
    print(statement)
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    connection.commit()

def get_teams(connection):
    """Retrieves all teams from the database."""
    query = "SELECT * FROM TEAM"
    teams = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return teams

def get_members(connection):
    """Retrieves all members from the database."""
    query = "SELECT * FROM MEMBER"
    members = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return members

def get_mentor_scoring(connection):
    """Retrieves mentor scoring data from the database."""
    query = "SELECT * FROM MENTOR_SCORES"
    mentor_scores = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return mentor_scores

def get_judge_scoring(connection):
    """Retrieves judge scoring data from the database."""
    query = "SELECT * FROM JUDGE_SCORES"
    judge_scores = execute_sql_query(connection, query)
    return judge_scores

def get_final_scores(connection):
    """Retrieves final scores from the database."""
    query = "SELECT * FROM FINAL_SCORESHEETS"
    final_scores = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return final_scores

def get_team_submission(connection):
    """Retrieves team submissions from the database."""
    query = "SELECT * FROM SUBMISSIONS"
    submissions = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return submissions

def get_extensions(connection):
    """Retrieves extension board allocations from the database."""
    query = "SELECT * FROM EXTENTION_BOARD_ALLOCATION"
    extensions = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return extensions

def get_checkin(connection):
    """Retrieves check-in data from the database."""
    query = "SELECT * FROM CHECK_INTIME"
    checkin = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return checkin

def get_mentors():
    """Retrieves mentors from the database."""
    query = "SELECT * FROM MENTORS"
    mentors = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return mentors

def get_judges():
    """Retrieves judges from the database."""
    query = "SELECT * FROM JUDGES"
    judges = execute_sql_query(connection, query)
    disconnect_from_database(connection)
    return judges

def put_team(connection,team_name):
    """Inserts a new team into the database."""
    statement = f"""
        BEGIN
            INSERT_TEAM('{team_name}');
        END;
        
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_member(connection,member_name, email, college_name, ph_no, team_id):
    """Inserts a new member into the database."""
    statement = f"""
    
        BEGIN
            INSERT MEMBER('{member_name}', '{email}', '{college_name}', '{ph_no}', {team_id});
        END;
    
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_mentor(connection,mentor_id, mentor_name, mentor_ph):
    """Inserts a new mentor into the database."""
    statement = f"INSERT INTO MENTORS (Mentor_Id, Mentor_Name, Mentor_Ph) VALUES ({mentor_id}, '{mentor_name}', '{mentor_ph}')"
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_judge(connection,judge_id, judge_name):
    """Inserts a new judge into the database."""
    statement = f"INSERT INTO JUDGES (Judge_Id, Judge_Name) VALUES ({judge_id}, '{judge_name}')"
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_checkin(connection,member_id):
    """Inserts a check-in record for a member into the database."""
    statement = f"""
    
        BEGIN
            check_in_member({member_id});
        END;
    
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_extension(connection,extention_board_no, team_id):
    """Inserts an extension board allocation into the database."""

    statement = f"INSERT INTO extention_Board_Allocation VALUES({extention_board_no},{team_id});"

    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_mentor_scoring(connection,mentor_id, team_id, team_score):
    """Inserts mentor scoring data into the database."""
    statement = f"""
    
        BEGIN
            add_mentor_scores({mentor_id},{team_id},{team_score});
        END;
    
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_judge_scoring(connection,team_id, judge_id, score):
    """Inserts judge scoring data into the database."""
    statement = f"""
    
        BEGIN 
            add_judges_scores({team_id},{judge_id},{score});
        END;
    
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

def put_submissions(connection,teamid,ppt,github):
    statement = f"""
    
        BEGIN
            update_submissions({teamid}, '{ppt}', '{github}');
        END;
    
    """
    execute_sql_statement(connection, statement)
    disconnect_from_database(connection)

