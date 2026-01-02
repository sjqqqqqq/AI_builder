# Lesson 3 Homework: Mystery Script
# This script contains several intentional errors. 
# Use your CER card to fix them with AI!

import math
import sys

def calculate_circle_area(radius):
    # Hint: Check for syntax errors above
    return math.pi * radius ** 2

def display_welcome_message():
    print("Welcome to the Lesson 3 Mystery Challenge!")
    print("Let's see if you can fix me.")

def main():
    display_welcome_message()
    
    # Intentional Dependency Error (if tabulate is not installed)
    try:
        from tabulate import tabulate
        data = [["Circle", "Area"], ["Example", 12.5]]
        print(tabulate(data, headers="firstrow"))
    except ImportError:
        print("\n[ERROR] Module 'tabulate' not found. This is a Dependency Error!")
        print("Use your CER card to ask AI how to install it.")

    # Intentional Runtime Error
    user_radius = 5 # Fixed: Changed from string "5" to integer 5
    print(f"\nCalculating area for radius {user_radius}...")
    
    # This will cause a TypeError because you can't square a string
    area = calculate_circle_area(user_radius)
    print(f"The area is: {area}")

if __name__ == "__main__":
    main()
