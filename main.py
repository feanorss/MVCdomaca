from shoecontroller import ShoeController

controller = ShoeController()


controller.add_shoe(1, "Men", "Sneaker", "Black", 100, "Nike", 10)
controller.add_shoe(2, "Women", "Running", "White", 120, "Adidas", 8)
controller.add_shoe(3, "Men", "Casual", "Blue", 85, "Vans", 10)
controller.add_shoe(4, "Women", "Sneaker", "Red", 90, "Converse", 7)
controller.add_shoe(5, "Men", "Running", "Grey", 110, "New Balance", 11)
controller.add_shoe(6, "Women", "Boot", "Black", 150, "Timberland", 8)
controller.add_shoe(7, "Men", "Sandal", "Brown", 50, "Birkenstock", 10)
controller.add_shoe(8, "Women", "Flat", "Beige", 65, "Toms", 9)
controller.add_shoe(9, "Men", "Boot", "Black", 140, "Dr. Martens", 10)
controller.add_shoe(10, "Women", "Heel", "Pink", 130, "Steve Madden", 8)
controller.add_shoe(10, "Women", "Heel", "Pink", 130, "Steve Madden", 8)

print("Showing all shoes:")
controller.show_shoes()
print("\nShowing shoes of size 10:")
controller.show_shoes_by_size(10)

controller.show_total_price_of_shoes()

controller.delete_shoe_by_id(1)


# from shoecontroller import ShoeController
#
# def main():
#     controller = ShoeController()
#
#     # Adding shoes with the new parameters
#     controller.add_shoe(1, "Men", "Sneaker", "Black", 100, "Nike", 10)
#     controller.add_shoe(2, "Women", "Running", "White", 120, "Adidas", 8)
#
#     controller.show_shoes()
#
# if __name__ == "__main__":
#     main()