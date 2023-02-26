import psycopg2
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()



def call_db(query: str, *args):
    connection = psycopg2.connect(database="postgres",
    user="admin",
    password="20MaximiLLiaN12",
    host="localhost")

    cursor = connection.cursor()
    cursor.execute(query, args)
    data = cursor.fetchall()
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
    return "Hello Linda"

@app.get("/create")
def root():
    create_database()
    return "DB Created"
@app.get("/seedRestaurant")
def seed_restaurant():
    create_restaurant = """
    INSERT INTO restaurant (
    name, 
    city,
    street,
    postalcode
    ) VALUES (
    ?, ?, ?, ?
    )
    """

    with open("seed_files/restaurant_seed.json", "r") as restaurant_seed:
        data = json.load(restaurant_seed)

    for restaurant in data["restaurant"]:
        psycopg2.call_db(create_restaurant, restaurant["name"], restaurant["city"],
                   restaurant["street"], restaurant["postalcode"])
    return "Restaurants seeded"

@app.get("/seedPerson")
def seedPerson():
    seedPerson
    return "Db seeded with data"

@app.get("/getPersons")
def get_persons():
    get_persons_query = """SELECT * FROM person"""
    data = call_db(get_persons_query)
    return data

@app.get("/getPerson")
def get_persons():
    get_persons_query = """SELECT * FROM person"""
    data = call_db(get_persons_query)
    return data

@app.get("/getRestaurants")
def get_restaurants():
    get_restaurants_query = """SELECT * FROM restaurant"""
    data = call_db(get_restaurants_query)
    return data