import psycopg2
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def print_menu():
    print(
        """
    1: Create database
    2: Seed database
    3: Get persons
    4: Get restaurants
    5: Get reviews
    6: Update person
    7: Post review
    8: Delete review
    9: Exit program
    """
    )
    pass

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

@app.get("/getRestaurants")
def get_restaurants():
    get_restaurants_query = """SELECT * FROM restaurant"""
    data = call_db(get_restaurants_query)
    return data

def main():
    print_menu()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            print("1 - Not yet implemented")
        case 2:
            print("2 - Not yet implemented")
        case 3:
            persons = get_persons()
            print(persons)
        case 4:
            restaurants = get_restaurants()
            print(restaurants)
        case 5:
            print("5 - Not yet implemented")
        case 6:
            print("6 - Not yet implemented")
        case 7:
            print("7 - Not yet implemented")
        case 8:
            print("8 - Not yet implemented")
        case 9:
            exit()
        case _:
            print("Please enter a valid choice")


while __name__ == "__main__":
    main()