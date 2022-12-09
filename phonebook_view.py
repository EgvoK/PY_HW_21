ADD_TO_START_INDEX = 1


class MenuDisplay:
    @staticmethod
    def display(options):
        print("Phonebook Application\nThe following commands are available: ")
        for key, value in options.items():
            print(f"{key}. {value}")
        print("\n")


class AddItemDisplay:
    @staticmethod
    def display(first_name, last_name):
        print(f"Item {first_name} {last_name} successfully added to phonebook!")


class ModifyItemDisplay:
    @staticmethod
    def display(index):
        print(f"Item {index + ADD_TO_START_INDEX} successfully modified!")


class DeleteItemDisplay:
    @staticmethod
    def display(index):
        print(f"Item {index + ADD_TO_START_INDEX} has been successfully deleted!")


class AllItemsDisplay:
    @staticmethod
    def display(items):
        if not items:
            print("Phonebook is empty!")
        else:
            for key, value in enumerate(items):
                print(key + ADD_TO_START_INDEX, value)


class ItemDisplay:
    @staticmethod
    def display(index, item):
        print(index + ADD_TO_START_INDEX, item)
