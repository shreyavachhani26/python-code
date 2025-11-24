# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 12:30:21 2025

@author: ADMIN
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("---------------------------")

    # Method to apply discount
    def apply_discount(self, percentage):
        discount_amount = (percentage / 100) * self.price
        self.price -= discount_amount

# (a) Create two book objects
book1 = Book("The Secret", "Rhonda Byrne", 499)
book2 = Book("Atomic Habits", "James Clear", 650)

print("Book Details Before Discount:")
book1.display_details()
book2.display_details()

# (b) Apply 10% discount to one book (book2)
book2.apply_discount(10)

print("Book Details After Applying 10% Discount on Book 2:")
book2.display_details()
