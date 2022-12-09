from phonebook_item import PhonebookItem


class Model:
    def __init__(self):
        self.phonebook_items = []

    def add_item(self, first_name, last_name, phone_number):
        self.phonebook_items.append(PhonebookItem(first_name, last_name, phone_number))

    def modify_item(self, index, first_name, last_name, phone_number ):
        self.phonebook_items[index] = PhonebookItem(first_name, last_name, phone_number)

    def delete_item(self, index):
        self.phonebook_items.pop(index)

    def get_items(self):
        return self.phonebook_items

    def get_item(self, index):
        return self.phonebook_items[index]
