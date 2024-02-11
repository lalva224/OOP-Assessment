# ENSURE EVERYTHING BELOW IS COMMENTED WHEN YOU SUBMIT YOUR ASSESSMENT AND RUN TESTS
from classes.store import Store
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx

# # """TO DO
# # 1. exit terminal

# # """

# menu = """
# == Welcome to Code Platoon Video! ==
# 1. View store video inventory
# 2. View customer rented videos
# 3. Add new customer
# 4. Rent video
# 5. Return video
# 6. Exit
# """

# def run_terminal():
#     while True:
#     choice = input(menu)
#     if choice == "1":
#         pass
#     elif choice == "2":
#         pass
#     elif choice == "3":
#         pass
#     elif choice == "4":
#         pass
#     elif choice == "5":
#         pass
#     elif choice == "6":
#         break
#     else:
#         run_terminal()

# run_terminal()


block_buster = Store("Block Buster")
block_buster.load_data("inventory")
block_buster.load_data("customers")
print(block_buster.run_the_store())
