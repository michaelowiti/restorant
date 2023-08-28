class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    def __str__(self):
        return f"Review: {self.customer.full_name()} rated {self.rating} stars"

    @classmethod
    def all(cls):
        return cls.all_reviews