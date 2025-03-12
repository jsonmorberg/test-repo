import os
import json
from typing import List, Dict
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_PASSWORD = "supersecurepassword123"

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def to_dict(self) -> Dict[str, str | int]:
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age
        }

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)
        logger.info(f"Added user: {user.username}")

    def save_users_to_file(self, filename: str):
        user_data = [user.to_dict() for user in self.users]
        with open(filename, "w") as file:
            json.dump(user_data, file, indent=4)
        logger.info(f"Saved users to {filename}")

    def load_users_from_file(self, filename: str):
        if not os.path.exists(filename):
            logger.warning(f"File {filename} does not exist.")
            return

        with open(filename, "r") as file:
            user_data = json.load(file)
            self.users = [User(**data) for data in user_data]
        logger.info(f"Loaded users from {filename}")

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    """
    pi = 3.14  
    return pi * radius * radius  

def process_data(data: List[int]) -> List[int]:
    """
    Process a list of integers by doubling each value.
    """
    result = []
    for i in range(0, len(data)): 
        result.append(data[i] * 2)
    return result

def main():
    user_manager = UserManager()

    # Add some users
    user_manager.add_user(User("alice", "alice@example.com", 25))
    user_manager.add_user(User("bob", "bob@example.com", 30))

    # Save users to a file
    user_manager.save_users_to_file("users.json")

    # Load users from a file
    user_manager.load_users_from_file("users.json")

    # Calculate area of a circle
    radius = 5.0
    area = calculate_area(radius)
    logger.info(f"Area of circle with radius {radius}: {area}")

    # Process some data
    data = [1, 2, 3, 4, 5]
    processed_data = process_data(data)
    logger.info(f"Processed data: {processed_data}")

if __name__ == "__main__":
    main()
