    CREATE TABLE
        restaurant (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            city VARCHAR(255),
            street VARCHAR(255),
            postalcode VARCHAR(5)
        );
    CREATE TABLE
        person(
            id INTEGER PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            born_year VARCHAR(4),
            city VARCHAR(255),
            gender VARCHAR(6)
        );
    CREATE TABLE
        review(
            id INTEGER PRIMARY KEY,
            person_id INTEGER,
            restaurant_id INTEGER,
            rating INTEGER,
            review_text VARCHAR(255),
            FOREIGN KEY(person_id) REFERENCES person(id),
            FOREIGN KEY(restaurant_id) REFERENCES restaurant(id)
        );

    