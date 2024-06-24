#!/usr/bin/python3

"""
Module with unittests for Review class
"""

import unittest
from models.reviews import Review

class TestReview(unittest.TestCase):
    """
    Test class for Review class
    """

    def test_create_review(self):
        """
        Check if the instantiation of review object works properly
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_initiate_review(self):
        """
        Test if attributes are initialized to default values
        """
        review = Review()
        self.assertEqual(review.user, "")
        self.assertEqual(review.place, "")
        self.assertEqual(review.rating, 0)
        self.assertEqual(review.comment, "")

    def test_set_valid_review_attributes(self):
        """
        Test setting valid attributes to an Review instance
        """
        review = Review()
        self.user = "Mario Jumpman"
        self.place = "Peach Castle"
        self.rating = 5
        self.comment = "Amazing view, the Toads are so cute and helpful !"

        self.assertEqual(review.user, "Mario Jumpman")
        self.assertEqual(review.place, "Peach Castle")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Amazing view, the Toads are so cute and helpful !")

if __name__ == "__main__":
    unittest.main()


# Check if the ID ALWAYS stays the same

# Check if created_at is set during creation of a new review object
# and stays the same

# Check if updated_at is set during edition of the review object

# A Host trying to write a review for his own place

# Create a review too big
# => rules for reviews size

# Remove a review
