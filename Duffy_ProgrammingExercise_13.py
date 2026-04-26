import sqlite3

# Function to build the database
def create_database(database):
    # Create the connection
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # Create the population table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL,
            PRIMARY KEY (city, year)
        )
    """)

    # Save the table setup
    connection.commit()

    # Return the database connection
    return connection


# Function that inserts the data into table
def insert_starting_data(connection, starting_population):
    # Create the cursor
    cursor = connection.cursor()

    # Build empty row array
    rows = []

    # Loop through data and append as rows
    for city, population in starting_population.items():
        rows.append((city, 2025, population))

    # Insert rows into database
    cursor.executemany("""
        INSERT OR REPLACE INTO population (city, year, population)
        VALUES (?, ?, ?)
    """, rows)

    # Commit changes
    connection.commit()


# Store the starting 2025 population data
city_data = {
    "Sarasota": 57764,
    "Orlando": 334854,
    "Tampa": 414547,
    "Miami": 487014,
    "Tallahassee": 205089,
    "Jacksonville": 1009833,
    "Fort Myers": 99918,
    "St. Petersburg": 267102,
    "Cape Coral": 233025,
    "Gainesville": 148720,
    "Daytona Beach": 86015
}

# Function to print all rows in the population table
def print_population_table(connection):
    # Create the cursor
    cursor = connection.cursor()

    # Select all rows from the population table
    cursor.execute("""
        SELECT city, year, population
        FROM population
        ORDER BY city, year
    """)

    # Store all rows from the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)


database = "population_MD.db"
connection = create_database(database)
insert_starting_data(connection, city_data)
print_population_table(connection)
connection.close()