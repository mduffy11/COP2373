import random
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
    "Cape Coral": 233025,
    "Gainesville": 148720,
    "Daytona Beach": 86015
}

# Store the historical growth profile for each city
historical_profiles = {
    "Sarasota": {"avg": 0.004508, "min": -0.014769, "max": 0.026532},
    "Orlando": {"avg": 0.023265, "min": 0.007624, "max": 0.038443},
    "Tampa": {"avg": 0.012846, "min": -0.021120, "max": 0.023907},
    "Miami": {"avg": 0.011982, "min": -0.076302, "max": 0.055511},
    "Tallahassee": {"avg": 0.012201, "min": -0.003557, "max": 0.051404},
    "Jacksonville": {"avg": 0.013222, "min": 0.004478, "max": 0.020617},
    "Fort Myers": {"avg": 0.029560, "min": -0.034960, "max": 0.079905},
    "Cape Coral": {"avg": 0.027834, "min": -0.003979, "max": 0.075349},
    "Gainesville": {"avg": 0.014599, "min": 0.004574, "max": 0.070428},
    "Daytona Beach": {"avg": 0.016013, "min": -0.032949, "max": 0.054809}
}


# Function to simulate future population values
def simulate_population(connection, city_data, historical_profiles, years=20):
    # Create the cursor
    cursor = connection.cursor()

    # Build empty row array
    simulated_rows = []

    # Loop through each city and starting population
    for city, starting_population in city_data.items():
        # Set the first population value
        current_population = starting_population

        # Get the historical profile for the city
        profile = historical_profiles[city]

        # Loop through the next 20 years
        for year in range(2026, 2026 + years):
            # Generate a growth rate based on historical values
            growth_rate = random.triangular(
                profile["min"],
                profile["max"],
                profile["avg"]
            )

            # Calculate the new population
            current_population = max(1, round(current_population * (1 + growth_rate)))

            # Append the simulated row
            simulated_rows.append((city, year, current_population))

    # Insert simulated rows into database
    cursor.executemany("""
        INSERT OR REPLACE INTO population (city, year, population)
        VALUES (?, ?, ?)
    """, simulated_rows)

    # Commit changes
    connection.commit()


# Function to print population records for one city
def print_city_population(connection, city):
    # Create the cursor
    cursor = connection.cursor()

    # Select the records for the chosen city
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (city,))

    # Store the query results
    rows = cursor.fetchall()

    # Print the city heading
    print(f"\nPopulation records for {city}:")

    # Print each year and population value
    for year, population in rows:
        print(f"{year}: {population:,}")


# Function to print a simple text chart for one city
def print_city_growth_chart(connection, city):
    # Create the cursor
    cursor = connection.cursor()

    # Select the records for the chosen city
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (city,))

    # Store the query results
    rows = cursor.fetchall()

    # Find the highest population for scaling
    max_population = max(population for year, population in rows)

    # Print the chart heading
    print(f"\nPopulation growth chart for {city}:")

    # Print a scaled bar for each year
    for year, population in rows:
        bar_length = int((population / max_population) * 50)
        print(f"{year}: {'*' * bar_length} {population:,}")


# Function to count the rows in the table
def count_population_rows(connection):
    # Create the cursor
    cursor = connection.cursor()

    # Count the rows in the table
    cursor.execute("""
        SELECT COUNT(*)
        FROM population
    """)

    # Store the count result
    count = cursor.fetchone()[0]

    # Print the row count
    print(f"\nRow count: {count}")


# Run a temporary simulation test
random.seed()

# Store the database file name
database = "population_MD.db"

# Create the database connection
connection = create_database(database)

# Insert the starting city data
insert_starting_data(connection, city_data)

# Simulate the future population data
simulate_population(connection, city_data, historical_profiles)

# Print the total number of rows
count_population_rows(connection)

# Print the yearly population records for one city
print_city_population(connection, "Orlando")

# Print a simple text chart for one city
print_city_growth_chart(connection, "Orlando")

# Close the database connection
connection.close()