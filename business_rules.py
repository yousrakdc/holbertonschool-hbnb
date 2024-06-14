#!/usr/bin/python3
"""
Set of rules to define the business rules of the website -> we don't need them as a simple document 
but we need to put them in the managments files and in the unitest doc.
"""

# Dictionary to store user's email
users_email = {}

# class define the rules
class Business_rules(BaseVariables):

    def __init__(self, rule):
        self.rule = rule

    @unique_email   # we need to compare the new user's email with a dictionary.
    def unique_email(self):
        email = users.email
        if email in users_email:
            return False
        else:
            users_email[email] = users
            return True

    
    @aplace_ahost   # one place must have one host
    def aplace_ahost(self):
        if place.host is none:
            return False
        else:
            return True
    
    @ahost_mulplaces   # a host can have multiple places
    def ahost_mulplaces(self):
        return   # how to present this ?
    
    @host_reviews      # a host can't review their own place
    def host_reviews(self):
        place = reviews.place
        user = reviews.user
        if place.host == user:
            return False
        else:
            return True
    

# Define actions when rules are triggered
class Actions:
    @rule_action(params={"user": FIELD_NUMERIC})   # add a new user in the user email dictionary
    def add_user(self, user):
        users_email[user.email] = user

    @rule_action(params={"place": FIELD_NUMERIC, "user": FIELD_NUMERIC})   # assign the place to a host 
    def assign_host(self, place, user):
        place.host = user
        user.hosted_places.append(place)

    @rule_action(params={"review": FIELD_NUMERIC})   # add review to the review list
    def add_review(self, review):
        review.place.reviews.append(review)
