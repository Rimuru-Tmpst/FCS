# "We Deliver" program.


import sys
from collections import deque

class Driver:
    def __init__(self, driver_id, name, start_city):
        self.driver_id = driver_id
        self.name = name
        self.start_city = start_city

    def __str__(self):
        return f"{self.driver_id}, {self.name}, {self.start_city}"

class WeDeliver:
    def __init__(self):
        self.drivers = []  # List to store drivers
        self.cities = {}   # Dictionary to store cities and their neighbors
        self.driver_id_counter = 1  # To keep track of driver IDs

    def generate_driver_id(self):
        # Generate unique driver ID based on the counter
        driver_id = f"ID{str(self.driver_id_counter).zfill(3)}"
        self.driver_id_counter += 1
        return driver_id

    def add_driver(self, name, start_city):
        if start_city not in self.cities:
            add_city = input(f"'{start_city}' is not in the city database. Would you like to add it? (y/n): ")
            if add_city.lower() != 'y':
                print("Driver not added.")
                return
            else:
                self.cities[start_city] = []  # Initialize with no neighbors
                print(f"City '{start_city}' added successfully.")
        driver_id = self.generate_driver_id()
        new_driver = Driver(driver_id, name, start_city)
        self.drivers.append(new_driver)
        print(f"Driver '{name}' with ID {driver_id} added successfully!")

    def view_all_drivers(self):
        if not self.drivers:
            print("No drivers available.")
        else:
            print("\nList of Drivers:")
            for driver in self.drivers:
                print(driver)

    def check_similar_drivers(self):
        if not self.drivers:
            print("No drivers available.")
            return
        city_drivers = {}
        for driver in self.drivers:
            city_drivers.setdefault(driver.start_city, []).append(driver.name)
        
        print("\nSimilar Drivers (Grouped by Start City):")
        for city, drivers in city_drivers.items():
            print(f"{city}: {', '.join(drivers)}")

    def show_cities(self):
        if not self.cities:
            print("No cities available.")
        else:
            print("\nList of Cities (Z to A):")
            for city in sorted(self.cities.keys(), reverse=True):
                print(city)

    def search_city(self, keyword):
        found_cities = [city for city in self.cities.keys() if keyword.lower() in city.lower()]
        if found_cities:
            print("Cities found:", ", ".join(found_cities))
        else:
            print("No cities found with that keyword.")

    def print_neighboring_cities(self, city_name):
        if city_name in self.cities:
            neighbors = self.cities[city_name]
            if neighbors:
                print(f"Neighboring cities of '{city_name}': {', '.join(neighbors)}")
            else:
                print(f"'{city_name}' has no neighboring cities.")
        else:
            print("City not found in the database.")

    def add_neighboring_cities(self, city_name):
        if city_name not in self.cities:
            print(f"City '{city_name}' does not exist in the database.")
            return
        neighbor = input(f"Enter a city name to add as a neighbor to '{city_name}': ")
        if neighbor not in self.cities:
            add_city = input(f"'{neighbor}' is not in the city database. Would you like to add it? (y/n): ")
            if add_city.lower() != 'y':
                print("Neighbor city not added.")
                return
            else:
                self.cities[neighbor] = []
                print(f"City '{neighbor}' added successfully.")
        if neighbor in self.cities[city_name]:
            print(f"'{neighbor}' is already a neighbor of '{city_name}'.")
        else:
            self.cities[city_name].append(neighbor)
            self.cities[neighbor].append(city_name)  # Assuming bidirectional
            print(f"Neighbor '{neighbor}' added to '{city_name}' successfully.")

    def print_drivers_delivering_to_city(self, destination_city):
        if destination_city not in self.cities:
            print(f"City '{destination_city}' does not exist in the database.")
            return

        def bfs(start_city):
            visited = set()
            queue = deque([start_city])
            while queue:
                city = queue.popleft()
                if city == destination_city:
                    return True
                if city not in visited:
                    visited.add(city)
                    queue.extend(self.cities.get(city, []))
            return False

        delivering_drivers = []
        for driver in self.drivers:
            if bfs(driver.start_city):
                delivering_drivers.append(driver.name)
        
        if delivering_drivers:
            print(f"Drivers delivering to '{destination_city}': {', '.join(delivering_drivers)}")
        else:
            print(f"No drivers found delivering to '{destination_city}'.")

    
def main_menu():
    system = WeDeliver()


    while True:
        print("\nHello! Please enter:")
        print("1. To go to the drivers’ menu")
        print("2. To go to the cities’ menu")
        print("3. To exit the system")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            drivers_menu(system)
        elif choice == '2':
            cities_menu(system)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def drivers_menu(system):
    while True:
        print("\nDrivers' Menu")
        print("1. To view all drivers")
        print("2. To add a driver")
        print("3. Check similar drivers")
        print("4. To go back to the main menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            system.view_all_drivers()
        elif choice == '2':
            name = input("Enter driver's name: ").strip()
            if not name:
                print("Driver name cannot be empty.")
                continue
            start_city = input("Enter start city: ").strip()
            if not start_city:
                print("Start city cannot be empty.")
                continue
            system.add_driver(name, start_city)
        elif choice == '3':
            system.check_similar_drivers()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def cities_menu(system):
    while True:
        print("\nCities' Menu")
        print("1. Show cities")
        print("2. Search city")
        print("3. Print neighboring cities")
        print("4. Print drivers delivering to city")
        print("5. Add neighboring cities")
        print("6. Go back to the main menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            system.show_cities()
        elif choice == '2':
            keyword = input("Enter city search keyword: ").strip()
            if not keyword:
                print("Search keyword cannot be empty.")
                continue
            system.search_city(keyword)
        elif choice == '3':
            city_name = input("Enter the city name: ").strip()
            if not city_name:
                print("City name cannot be empty.")
                continue
            system.print_neighboring_cities(city_name)
        elif choice == '4':
            destination_city = input("Enter the destination city: ").strip()
            if not destination_city:
                print("Destination city cannot be empty.")
                continue
            system.print_drivers_delivering_to_city(destination_city)
        elif choice == '5':
            city_name = input("Enter the city name to add neighbors to: ").strip()
            if not city_name:
                print("City name cannot be empty.")
                continue
            system.add_neighboring_cities(city_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()





import json

class WeDeliver:
    # ... [existing methods] ...

    def save_data(self, drivers_file='drivers.json', cities_file='cities.json'):
        drivers_data = [{'driver_id': d.driver_id, 'name': d.name, 'start_city': d.start_city} for d in self.drivers]
        with open(drivers_file, 'w') as f:
            json.dump(drivers_data, f, indent=4)
        
        with open(cities_file, 'w') as f:
            json.dump(self.cities, f, indent=4)
        
        print("Data saved successfully.")

    def load_data(self, drivers_file='drivers.json', cities_file='cities.json'):
        try:
            with open(drivers_file, 'r') as f:
                drivers_data = json.load(f)
                for d in drivers_data:
                    self.drivers.append(Driver(d['driver_id'], d['name'], d['start_city']))
                    # Update driver_id_counter to avoid ID conflicts
                    id_num = int(d['driver_id'][2:])
                    if id_num >= self.driver_id_counter:
                        self.driver_id_counter = id_num + 1
        except FileNotFoundError:
            print("Drivers file not found. Starting with an empty drivers list.")
        
        try:
            with open(cities_file, 'r') as f:
                self.cities = json.load(f)
        except FileNotFoundError:
            print("Cities file not found. Starting with an empty cities list.")



def main_menu():
    system = WeDeliver()
    system.load_data()  # Load existing data
    try:
        while True:
            print("\nHello! Please enter:")
            print("1. To go to the drivers’ menu")
            print("2. To go to the cities’ menu")
            print("3. To exit the system")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                drivers_menu(system)
            elif choice == '2':
                cities_menu(system)
            elif choice == '3':
                system.save_data()  # Save data before exiting
                print("Exiting the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice, please try again.")
    except KeyboardInterrupt:
        # Handle abrupt exits
        system.save_data()
        print("\nExiting the system. Goodbye!")
        sys.exit()
