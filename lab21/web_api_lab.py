# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 19:28:00 2025

@author: ADMIN
"""

import requests

# GET Request
print("\n--- GET Request Example ---")

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print("Fetched Posts:")
    for post in posts[:5]:  # Print first 5 posts
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")


# POST Request
print("\n--- POST Request Example ---")

url = 'https://jsonplaceholder.typicode.com/posts'

new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

response = requests.post(url, json=new_post)

if response.status_code == 201:
    created_post = response.json()
    print("Created Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")




# Error Handling Example
print("\n--- Error Handling Example ---")

url = 'https://jsonplaceholder.typicode.com/posts/1000'  # Invalid ID

response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    print("Fetched Post:", post)
else:
    print(f"Error: {response.status_code} - {response.reason}")
