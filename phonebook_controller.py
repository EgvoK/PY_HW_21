import os
import sys

from phonebook_view import *
from phonebook_model import Model

ADD_TO_START_INDEX = 1


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Controller:
    OPTIONS = {'1': 'Show Phonebook',
               '2': 'Show Phonebook Item',
               '3': 'Add Item',
               '4': 'Modify Item',
               '5': 'Delete Item',
               '0': 'Exit'}

    def __init__(self):
        self.model = Model()

    def menu(self):
        cls()
        self.show_menu()

        while True:
            option = input("Enter the option number: ")
            cls()
            self.show_menu()
            if option in self.OPTIONS.keys():
                if option == "1":
                    self.display_items()
                if option == "2":
                    self.display_item()
                if option == "3":
                    self.add_item()
                if option == "4":
                    self.modify_item()
                if option == "5":
                    self.delete_item()
                if option == "0":
                    sys.exit()
            else:
                print("Error! Incorrect option number!")

    def show_menu(self):
        MenuDisplay.display(self.OPTIONS)

    def display_items(self):
        AllItemsDisplay.display(self.model.get_items())

    def display_item(self):
        index = self.ask_index()
        try:
            item = self.model.get_item(index)
            ItemDisplay.display(index, item)
        except IndexError:
            print("Error! Incorrect index!")

    def add_item(self):
        first_name = self.ask_first_name()
        last_name = self.ask_last_name()
        phone_number = self.ask_phone_number()
        self.model.add_item(first_name, last_name, phone_number)
        AddItemDisplay.display(first_name, last_name)

    def modify_item(self):
        index = self.ask_index()
        first_name = self.ask_first_name()
        last_name = self.ask_last_name()
        phone_number = self.ask_phone_number()
        try:
            self.model.modify_item(index, first_name, last_name, phone_number)
            ModifyItemDisplay.display(index)
        except IndexError:
            print("Error! Incorrect index!")

    def delete_item(self):
        index = self.ask_index()
        try:
            self.model.delete_item(index)
            DeleteItemDisplay.display(index)
        except IndexError:
            print("Error! Incorrect index!")

    @staticmethod
    def ask_index():
        while True:
            try:
                index = int(input("Enter index of item: "))
                return index - ADD_TO_START_INDEX
            except ValueError:
                print("Error! Enter a number!")

    @staticmethod
    def ask_first_name():
        while True:
            return input("Enter first name: ").strip()

    @staticmethod
    def ask_last_name():
        while True:
            return input("Enter last name: ").strip()

    @staticmethod
    def ask_phone_number():
        while True:
            try:
                phone_number = int(input("Enter phone number: "))
                return phone_number
            except ValueError:
                print("Error! Enter a number!")
