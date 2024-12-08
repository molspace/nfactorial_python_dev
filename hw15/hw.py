import random

"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = set()
        
    def add_ingredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.add(ingredient)
        else:
            raise ValueError(f'Ingredient {ingredient} was already added in Pizza.')

"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.current_floor: int = 0

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1
        else:
            pass

    def get_current_floor(self):
        return self.current_floor

"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self._stack = list()

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("Can't pop an empty stack.")
        self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0

"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Can't withdraw bigger than balance amount.")
        self.balance -= amount

    def check_balance(self):
        return self.balance

"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError("Age can't be less than 0.")
        self.age = age

    def birthday(self):
        self.age += 1

"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        raise NotImplementedError("Implement the 'sound' method for your class.")

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Can't divide by zero.")
        return x / y

"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed > 0:
            raise ValueError("Speed can't be negative.")
        self.speed = speed

        if mileage > 0:
            raise ValueError("Mileage can't be negative.")
        self.mileage = mileage

"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class StudentCourse:
    def __init__(self, name):
        self.name = name
        
class Course:
    def __init__(self):
        self.students = list()

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        return self.students

"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = list()

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        departure_hour, departure_minute = self.departure.split(":")
        self.departure = f"{int(departure_hour) + delay_time}:{departure_minute}"

"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = list()

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book

"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
    
    def add(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            raise ValueError(f"Matrix sizes don't match. Need: {self.rows} x {self.cols}")
        self.new_matrix = [[[] * self.cols] * self.rows]
        for row_idx in range(other.rows):
            for col_idx in range(other.cols):
                self.new_matrix[row_idx][col_idx] = self.new_matrix[row_idx][col_idx] + other[row_idx][col_idx]

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.width == self.height


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius**2, 1)

    def circumference(self):
        return round(2 * 3.14 * self.radius, 1)

"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sides do not form a valid triangle.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))**0.5

"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        raise NotImplementedError("Implement the 'area' method for your class.")

    def perimeter(self):
        raise NotImplementedError("Implement the 'perimeter' method for your class.")

class Circle(Circle):
    def __init__(self, radius):
        super().__init__(radius)

class Rectangle(Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)

class Triangle(Triangle):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b, side_c)

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        self.playlist = list()
        self.current_song = None

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        self.current_song = self.playlist[0]
        return self.current_song

    def next_song(self):
        current_index = self.playlist.index(self.current_song)
        if current_index == len(self.playlist) - 1:
            current_index = -1
        self.current_song = self.playlist[current_index + 1]
        return self.current_song

    def shuffle(self):
        random.shuffle(self.playlist)

"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Can't sell more items than are in stock.")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity

"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")

"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

class School:
    def __init__(self):
        self.teachers = list()
        self.students = list()

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
        return self.teachers + self.students

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
        RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self._deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop()

    def count(self):
        return len(self._deck)
