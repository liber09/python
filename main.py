import psycopg2
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
connection_string = "dbname=python_assignment user=admin"



def call_db(query: str, *args):
    connection = psycopg2.connect(database="python_assignment",
user="admin",
password="20MaximiLLiaN12",
host="localhost",
port= '5432')
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

def create_database():
    conn =  psycopg2.connect(connection_string)
    try:
        with conn:
            with conn.cursor() as curs:
                with open(
                    "/Users/lindabergsangel/Library/Mobile Documents/com~apple~CloudDocs/Documents/Lindas skola/Data Scientist/Python programmering/Python/setupDb.sql", "r"
                ) as file:
                    sql = file.read() 
                curs.execute(sql)
    finally:
        conn.close()

@app.get("/")
def root():
    return "Hello"

@app.get("/create")
def root():
    create_database()
    return "DB Created"

@app.get("/test")
async def test():
    return {"message": "Test"}

def seedPerson():
    create_person = """
    INSERT INTO person (
    first_name, 
    last_name,
    born,
    city,
    gender
    ) VALUES (
    ?, ?, ?, ?, ?
    )
    """

    with open("seed_files/person_seed.json", "r") as person_seed:
        data = json.load(person_seed)

    for person in data["persons"]:
        psycopg2.call_db(create_person, person["first_name"], person["last_name"],
                   person["born_year"], person["city"], person["gender"])

@app.get("/seedPerson")
def seedPerson():
    seedPerson
    return "Db seeded with data"