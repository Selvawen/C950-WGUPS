# Define Package Class
class Package:

    def __init__(self, ID, address, city, state, zipcode, delivery_deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck = None

    # Overloaded string conversion method to create a string representation of the attributes
    def __str__(self):

        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.delivery_deadline, self.weight, self.delivery_time,
                                                       self.status, self.truck)

    # Set delivery status based on delivery time
    def get_status(self, elapsed_time):

        if self.delivery_time < elapsed_time:
            self.status = "Delivered"

        elif self.departure_time > elapsed_time:
            self.status = "En route"

        else:
            self.status = "At hub"
