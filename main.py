# Import classes and data files
import Truck
from Package import Package
from CreateHashTable import CreateHashMap

import csv
import datetime

# Load address data from CSV file into a list
with open("WGUPS_Addresses.csv") as addressFile:
    CSV_Address = csv.reader(addressFile)
    CSV_AddressList = []
    next(CSV_Address) # Skip header row
    for row in CSV_Address:
        CSV_AddressList.append(row) # Append each address record to the list

# Load distance data from CSV file into a list
with open("WGUPS_Distance.csv") as distanceFile:
    CSV_Distance = csv.reader(distanceFile)
    CSV_DistanceList = []
    next(CSV_Distance) # Skip header row
    for row in CSV_Distance:
        CSV_DistanceList.append(row)  # Append each distance record to the list

# Load package data from CSV file into a list
with open("WGUPS_Packages.csv") as packageFile:
    CSV_Packages = csv.reader(packageFile)
    CSV_PackageList = []
    next(CSV_Packages) # Skip header row
    for row in CSV_Packages:
        CSV_PackageList.append(row) # Append each package record to the list


# Method to create Package objects from CSV file and add them to a hash table
def add_packages(filename, hash_table):
    with open(filename) as package_file:
        package_data = csv.reader(package_file)
        next(package_data)  # Skip first line to remove header
        for package in package_data:  # Set attributes
             # Extract package details
            pack_id = int(package[0])
            pack_address = package[1]
            pack_city = package[2]
            pack_state = package[3]
            pack_zip = package[4]
            pack_deadline = package[5]
            pack_weight = package[6]
            pack_status = "At hub"

            # Use attribute variables to create new Package object
            pack = Package(pack_id, pack_address, pack_city, pack_state,
                           pack_zip, pack_deadline, pack_weight, pack_status)

            # Insert the package into the hash table
            hash_table.ht_insert(pack_id, pack)


# Method to calculate distance between two addresses based on their ID
def calculate_distance(x, y):
    distance = CSV_DistanceList[x][y]
    if distance == '':
        distance = CSV_DistanceList[y][x]

    return float(distance)


# Method to find the ID number of an address
def get_address_id(address):
    for r in CSV_AddressList:
        if address in r[2]: # Compare the address string
            return int(r[0]) # Return the corresponding ID


# Create Truck objects with default attributes
# Truck objects represent delivery vehicles with specific capabilities
truck1 = Truck.Truck(16, 18, None,
                     [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = Truck.Truck(16, 18, None,
                     [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = Truck.Truck(16, 18, None,
                     [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

# Create hash table and load in packages
hash_Table = CreateHashMap()
add_packages("WGUPS_Packages.csv", hash_Table)


# Method to assign trucks with packages using nearest neighbor
def assign_packages(truck):
    unsorted = []

    # Move packages into a list of unsorted packages to sort and assign them
    for idNum in truck.packages:
        package = hash_Table.ht_search(idNum)
        unsorted.append(package)
    truck.packages.clear()

    # Find nearest package to truck and insert back into truck's package array
    while len(unsorted) > 0:
        destination = 2000
        next_package = None

        # Check the distance between truck and each package and determine next package
        for package in unsorted:
            if calculate_distance(get_address_id(truck.address), get_address_id(package.address)) <= destination:
                destination = calculate_distance(get_address_id(truck.address), get_address_id(package.address))
                next_package = package

        # Assign next package to truck and remove from unsorted list
        truck.packages.append(next_package.ID)
        unsorted.remove(next_package)

        truck.totalMiles += destination  # Add mileage from each truck to the trucks total mileage
        truck.address = next_package.address  # Update trucks starting location to package location in each iteration

        # Update time for truck and next package
        truck.time += datetime.timedelta(hours=destination / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


# Sort the packages using the truck objects created previously
assign_packages(truck1)
assign_packages(truck2)
truck3.depart_time = min(truck1.time, truck2.time)
assign_packages(truck3)
totalMiles = truck1.totalMiles + truck2.totalMiles + truck3.totalMiles


# Main class displays user interface in console
def main():
    # Display welcome message and menu
    print("WGU Parcel Tracking Service:")
    while True:  # Keeps the program running until the user selects Option 4
        print("""
            1. Print status of all packages and total miles
            2. Print status of individual package across time zones
            3. Print status of all packages at a specific time 
            4. Exit
            """)
        ans = input("Enter the number representing your choice(1-4): ")
        if ans == "1":
            # Print combined miles and every package that will be delivered
            print(f'WGUPS trucks have {totalMiles:.1f} miles on their combined routes today.')
            print(f'Truck 1 has {truck1.totalMiles:.1f} miles.')
            print(f'Truck 2 has {truck2.totalMiles:.1f} miles.')
            print(f'Truck 3 has {truck3.totalMiles:.1f} miles.')
            print("All packages scheduled today: ")
            for packageID in range(1, 41):
                package = hash_Table.ht_search(packageID)

                if package.ID in truck1.packages:
                    package.truck = 'Truck 1'

                elif package.ID in truck2.packages:
                    package.truck = 'Truck 2'

                elif package.ID in truck3.packages:
                    package.truck = 'Truck 3'

                print(str(package))

        elif ans == "2":
            # Display the available time ranges
            print("Check the status of a package across three time ranges.")
            print("Time Ranges:")
            print("1. Between 8:35 a.m. and 9:25 a.m.")
            print("2. Between 9:35 a.m. and 10:25 a.m.")
            print("3. Between 12:03 p.m. and 13:12 p.m.")
            
            try:
                # Prompt the user to enter the package number
                user_package = int(input("Enter the package number: "))
                package = hash_Table.ht_search(user_package)
                
                # Define the time ranges
                time_ranges = [
                    datetime.timedelta(hours=8, minutes=35),
                    datetime.timedelta(hours=9, minutes=25),
                    datetime.timedelta(hours=9, minutes=35),
                    datetime.timedelta(hours=10, minutes=25),
                    datetime.timedelta(hours=12, minutes=3),
                    datetime.timedelta(hours=13, minutes=12)
                ]
                
                # Iterate through each time range
                for i in range(3):
                    print(f"\nChecking status for time range {i+1} ({time_ranges[2*i]} to {time_ranges[2*i+1]}):")
                    user_time = time_ranges[2*i]  # Start of the time range
                    
                    # Update package 9's address if time is past 10:30
                    if user_time >= datetime.timedelta(hours=10, minutes=20) and package.ID == 9:
                        package.address = '410 S. State St.'
                        package.city = 'Salt Lake City'
                        package.state = 'Utah'
                        package.zipcode = '84111'
                    
                    # Determine which truck the package is on
                    if package.ID in truck1.packages:
                        package.truck = 'Truck 1'
                    elif package.ID in truck2.packages:
                        package.truck = 'Truck 2'
                    elif package.ID in truck3.packages:
                        package.truck = 'Truck 3'
                    
                    # Print package status for the given time
                    package.get_status(user_time)
                    print(str(package))

            except ValueError:
                print("Invalid input. Please enter a valid package number.")

        elif ans == "3":
            # Take as input a time and display information for all packages
            try:
                user_time = input("Using the format HH:MM:SS, please enter a time: ")
                (h, m, s) = user_time.split(":")
                format_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                for packageID in range(1, 41):
                    package = hash_Table.ht_search(packageID)
                    package.get_status(format_time)

                    # Check if time is passed 10:30 and update package 9's incorrect address
                    if format_time >= datetime.timedelta(hours=10, minutes=20, seconds=0) and packageID == 9:
                        package.address = '410 S. State St.'
                        package.city = 'Salt Lake City'
                        package.state = 'Utah'
                        package.zipcode = '84111'

                    if package.ID in truck1.packages:
                        package.truck = 'Truck 1'

                    elif package.ID in truck2.packages:
                        package.truck = 'Truck 2'

                    elif package.ID in truck3.packages:
                        package.truck = 'Truck 3'

                    print(str(package))
            except ValueError:
                print("Invalid time entered. Please try again.")

        elif ans == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("\nNot a valid option. Please choose an option 1-4.\n")


if __name__ == "__main__":
    main()
