from customer import Customer
from restaurant import Restaurant

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create restaurants
restaurant1 = Restaurant("Delicious Eatery")
restaurant2 = Restaurant("Tasty Bistro")

# Add reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test the methods
print("-------------- Testing Customer methods --------------")
print("")

# full_name()
print("Customer 1 full name:")
print(customer1.full_name())  # Output: John Doe
print("-------------------------------------------")

# restaurants()
print("Customer 1 reviewed restaurants:")
print([restaurant.name for restaurant in customer1.restaurants()])
# Output: ['Delicious Eatery', 'Tasty Bistro']
print("-------------------------------------------")

# reviews()
print("Ratings for Restaurant 1:")
print([review.rating for review in restaurant1.reviews])
# Output: [4, 5]
print("-------------------------------------------")

# customers()
print("Customers who reviewed Restaurant 1:")
print([customer.full_name() for customer in restaurant1.customers()])
# Output: ['John Doe', 'Jane Smith']
print("-------------------------------------------")

# num_reviews()
print("Number of reviews by Customer 1:")
print(Customer.num_reviews(customer1))  # Output: 2
print("-------------------------------------------")

# find_by_name()
print("Finding customer by name 'John Doe':")
found_customer = Customer.find_by_name("John Doe")
print(found_customer.full_name())  # Output: John Doe
print("-------------------------------------------")

# find_all_by_given_name()
print("Finding customers with given name 'Jane':")
customers_with_given_name = Customer.find_all_by_given_name("Jane")
print([customer.full_name() for customer in customers_with_given_name])
# Output: ['Jane Smith']
print("-------------------------------------------")

# average_star_rating()
print("Average star rating for Restaurant 1:")
average_rating = restaurant1.average_star_rating()
print(average_rating)  # Output: 4.5
print("-------------------------------------------")