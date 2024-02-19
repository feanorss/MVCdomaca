class ShoeView:
    @staticmethod
    def display_shoes(shoes):
        for shoe in shoes:
            print(f"ID: {shoe.id}, Gender: {shoe.gender_type}, Type: {shoe.type}, Color: {shoe.color}, Price: ${shoe.price}, Brand: {shoe.brand}, Size: {shoe.size}")
    @staticmethod
    def display_total_price(total_price):
        print(f"Total price of all shoes: ${total_price}")

    @staticmethod
    def display_message(message):
        print(message)