class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list({review.customer() for review in self.reviews})

    def average_star_rating(self):
        total_ratings = sum(review.rating() for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews
