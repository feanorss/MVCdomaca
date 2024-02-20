from shoemodel import ShoeModel
from shoeview import ShoeView
from shoe import Shoe

class ShoeController:
    def __init__(self):
        self.model = ShoeModel()
        self.view = ShoeView()

    def add_shoe(self,id, gender_type, type, color, price, brand, size):
        if price < 0:
            self.view.display_message("Error: Shoe price cannot be less than 0.")
            return  # Exit the method without adding the shoe

        existing_shoe = self.model.find_shoe_by_id(id)
        if existing_shoe:
            self.view.display_message("Error: A shoe with this ID already exists.")
            return

        new_shoe = Shoe(id, gender_type, type, color, price, brand, size)
        self.model.add_shoe(new_shoe)


    def show_shoes(self):
        shoes = self.model.get_shoes()
        self.view.display_shoes(shoes)

    def show_shoes_by_size(self, size):
        shoes = self.model.find_shoes_by_size(size)
        self.view.display_shoes(shoes)

    def show_total_price_of_shoes(self):
        total_price = self.model.get_total_price_of_shoes()
        self.view.display_total_price(total_price)

    def delete_shoe_by_id(self, id):
        if self.model.delete_shoe_by_id(id):
            self.view.display_message("Shoe deleted successfully.")
        else:
            self.view.display_message("Shoe not found.")