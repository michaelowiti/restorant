class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def add_review(self, review):
        self.reviews.append(review)

    def customers(self):
        return list({review.customer for review in self.reviews})

    def average_star_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        average_rating = total_ratings / len(self.reviews)
        return average_rating