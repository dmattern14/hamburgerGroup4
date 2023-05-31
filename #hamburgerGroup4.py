#hamburgerGroup4
# Authors: Group 4 (Braxdon Simmons, Blake McAvoy, Dylan Mattern, Aly Leavitt, Saxon Cullimore, and Mckay Abbott)
# Description: Hamburger Door Dash (program to track how many hamburgers each customer eats)




import random




# Order class creation
class Order:
   def __init__(self):
       self.burger_count = self.randomBurgers()
  
   # Assign random burger counts to order
   def randomBurgers(self):
       return random.randint(1, 20)




# Person class creation
class Person:
   def __init__(self):
       self.customer_name = self.randomName()
    def randomName(self):
       # Create list of 9 names for random selection
       asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
       return random.choice(asCustomers)




# Customer class creation
class Customer(Person):
   def __init__(self):
       super().__init__()
       self.order = Order()




# Create an empty queue to hold customer objects
queue = []


# Create an empty dictionary to store customer names and total burger counts
dictCustomers = {}




# Generate 100 customers and add them to the queue
for _ in range(100):
   customer = Customer()
   queue.append(customer)
    # Update the dictionary with the customer's name and burger count
   if customer.customer_name in dictCustomers:
       dictCustomers[customer.customer_name] += customer.order.burger_count
   else:
       dictCustomers[customer.customer_name] = customer.order.burger_count


   # Pop first item from queue so as to be empty upon loop completion
   queue.pop(0)




# Sort the dictionary by the total number of burgers ordered in descending order
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)


# Print the customer name and total burger count for each customer
for customer in listSortedCustomers:
   print(customer[0].ljust(19), customer[1])