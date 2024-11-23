# Define Truck Class

class Truck:

    def __init__(self, max_packages, average_speed, num_packages, packages, total_miles, address, depart_time):
        self.maxPackages = max_packages
        self.averageSpeed = average_speed
        self.numPackages = num_packages
        self.packages = packages
        self.totalMiles = total_miles
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    # Overloaded string conversion method to create a string representation of the attributes
    def __str__(self):

        return "%s, %s, %s, %s, %s, %s, %s" % (self.maxPackages, self.averageSpeed, self.numPackages, self.packages,
                                               self.totalMiles, self.address, self.depart_time)
