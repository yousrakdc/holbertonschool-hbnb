#!/usr/bin/python3

"""
Module with unittests for Review class
"""

import unittest
from datetime import datetime
from models.reviews import Review

class TestReview(unittest.TestCase):
    """
    Test class for Review class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.review = Review(user="Mario Jumpman", place="Peach Castle", rating=5, comment="Amazing view, the Toads are so cute and helpful !")

    def test_create_review(self):
        """
        Check if the instantiation of review object works properly
        """
        self.assertIsInstance(self.review, Review)

    def test_initiate_review(self):
        """
        Test if attributes are initialized to default values
        """
        review = Review(user="", place="", rating=0, comment="")
        self.assertEqual(review.user, "")
        self.assertEqual(review.place, "")
        self.assertEqual(review.rating, 0)
        self.assertEqual(review.comment, "")

    def test_set_valid_review_attributes(self):
        """
        Test setting valid attributes to a Review instance
        """
        self.assertEqual(self.review.user, "Mario Jumpman")
        self.assertEqual(self.review.place, "Peach Castle")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Amazing view, the Toads are so cute and helpful !")

    def test_id_is_unique(self):
        """
        Check if the ID is unique for each review
        """
        review2 = Review(user="Luigi", place="Luigi's Mansion", rating=4, comment="Spooky but fun!")
        self.assertNotEqual(self.review.id, review2.id)

    def test_created_at_is_set(self):
        """
        Check if created_at is set during creation of a new review object
        """
        self.assertIsNotNone(self.review.created_at)
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_is_set(self):
        """
        Check if updated_at is set during creation of a new review object
        """
        self.assertIsNotNone(self.review.updated_at)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_updated_at_changes_on_update(self):
        """
        Check if updated_at is set during edition of the review object
        """
        old_updated_at = self.review.updated_at
        self.review.comment = "Updated comment"
        self.review.updated_at = datetime.utcnow()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_host_cannot_review_own_place(self):
        """
        A Host trying to write a review for his own place
        """
        with self.assertRaises(ValueError):
            Review.create({"user": "Host", "place": {"host": "Host"}, "rating": 5, "comment": "Great place!"})

    def test_remove_review(self):
        """
        Remove a review
        """
        review_id = self.review.id
        Review.delete(review_id)
        self.assertIsNone(Review.read(review_id))

if __name__ == "__main__":
    unittest.main()
