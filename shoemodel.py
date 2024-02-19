from shoe import Shoe

class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def get_shoes(self):
        return self.shoes

    def find_shoes_by_size(self, size):
        matching_shoes = []  # Initialize an empty list to hold matching shoes
        for shoe in self.shoes:
            if shoe.size == size:
                matching_shoes.append(shoe)  # Add the matching shoe to the list
        return matching_shoes  # Return the list of matching shoes

    def get_total_price_of_shoes(self):
        total_price = sum(shoe.price for shoe in self.shoes if shoe.price >= 0)
        return total_price

    def delete_shoe_by_id(self, id):
        for i, shoe in enumerate(self.shoes):
            if shoe.id == id:
                del self.shoes[i]
                return True  # Shoe found and deleted
        return False  # Shoe not found

    def find_shoe_by_id(self, id):
        for shoe in self.shoes:
            if shoe.id == id:
                return shoe
        return None