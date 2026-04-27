import sqlite3
import random
import matplotlib.pyplot as plt

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

# Store growth models derived from each city's past population changes
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

        # Get the historical growth model for the city
        profile = historical_profiles[city]

        # Loop through the next 20 years
        for year in range(2026, 2026 + years):
            # Generate a growth rate from the city's historical model
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


# Function to let the user choose a city
def choose_city(connection, show_list=True):
    # Create the cursor
    cursor = connection.cursor()

    # Select all city names from the table
    cursor.execute("""
        SELECT DISTINCT city
        FROM population
        ORDER BY city
    """)

    # Store the city names in a list
    cities = [row[0] for row in cursor.fetchall()]

    # Display the city choices
    if show_list:
        print("\nChoose a city to display population growth:")
        for number, city in enumerate(cities, start=1):
            print(f"{number}. {city}")

    # Loop until the user enters a valid choice
    while True:
        try:
            # Ask for the city number
            choice = int(input("\nEnter the number of the city: "))

            # Check that the choice is valid
            if 1 <= choice <= len(cities):
                # Return the selected city name
                return cities[choice - 1]
            else:
                print("Enter a valid number from the list.")

        except ValueError:
            # Handle non-numeric input
            print("Enter a whole number.")


# Function to ask whether to display another city
def choose_again():
    # Loop until the user enters a valid answer
    while True:
        # Ask whether to continue
        answer = input("\nWould you like to choose another city? (y/n): ").strip().lower()

        # Return True for yes
        if answer == "y":
            return True

        # Return False for no
        if answer == "n":
            return False

        # Prompt again for invalid input
        print("Enter y for yes or n for no.")


# Function to plot population growth for the selected city
def plot_population(connection, selected_city):
    # Create the cursor
    cursor = connection.cursor()

    # Select the year and population data for the chosen city
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (selected_city,))

    # Store the results from the query
    results = cursor.fetchall()

    # Build the year list
    years = [row[0] for row in results]

    # Build the population list
    populations = [row[1] for row in results]

    # Create the graph window
    plt.figure(figsize=(10, 6))

    # Create the line graph
    plt.plot(years, populations, marker="o")

    # Add the graph title
    plt.title(f"Population Change for {selected_city}")

    # Label the x-axis
    plt.xlabel("Year")

    # Label the y-axis
    plt.ylabel("Population")

    # Add grid lines
    plt.grid(True)

    # Adjust the layout
    plt.tight_layout()

    # Display the graph
    plt.show()


# Function to run the full program
def main():
    # Store the database file name
    database = "population_MD.db"

    # Create the database connection
    connection = create_database(database)

    # Insert the starting city data
    insert_starting_data(connection, city_data)

    # Simulate the future population data
    simulate_population(connection, city_data, historical_profiles)

    # Display the city list once
    show_list = True

    # Keep prompting until the user chooses to stop
    while True:
        # Let the user choose a city
        selected_city = choose_city(connection, show_list)

        # Plot the selected city's population data
        plot_population(connection, selected_city)

        # Stop reprinting the city list
        show_list = False

        # Break the loop if the user does not want another city
        if not choose_again():
            break

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    main()