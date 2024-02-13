# Write your Store Class here
# """TO DO
# 1. read csv and load both video and customer data to terminal program
# 2. ability to be able to see the customer database and the types of accounts each customer has
# 3. ability to run store in terminal program
# """
import csv
from classes.customer import Customer
from classes.customer_types import Customer_pf
from classes.customer_types import Customer_px
from classes.customer_types import Customer_sf
from classes.customer_types import Customer_sx
from classes.video import Video
class Store:
    def __init__(self,name):
        self.name = name
        self.customers = []
        self.videos = []
    
    def match_customer(self,customer_dict):
        match customer_dict["account_type"]:
            case "sx":
                customer = Customer_sx(customer_dict["id"],customer_dict["account_type"],customer_dict["first_name"],customer_dict["last_name"],customer_dict["current_video_rentals"])
            case "sf":
                customer = Customer_sf(customer_dict["id"],customer_dict["account_type"],customer_dict["first_name"],customer_dict["last_name"],customer_dict["current_video_rentals"])
            case "px":
                customer = Customer_px(customer_dict["id"],customer_dict["account_type"],customer_dict["first_name"],customer_dict["last_name"],customer_dict["current_video_rentals"])
            case "pf":
                customer = Customer_pf(customer_dict["id"],customer_dict["account_type"],customer_dict["first_name"],customer_dict["last_name"],customer_dict["current_video_rentals"])
        
        return customer


    def store_customer_data(self):
        with open("./data/customers.csv","r") as file:
            customer_reader = csv.DictReader(file)
            for customer_dict in customer_reader:
                customer = self.match_customer(customer_dict)
                self.customers.append(customer)
        
        return "Customer data stored!"
    
    def store_video_data(self):
        with open("./data/inventory.csv","r") as file:
            video_reader = csv.DictReader(file)
            for video_dict in video_reader:
                video = Video(**video_dict)
                self.videos.append(video)
        
        return "Video data stored!"

store = Store("Blockbuster")
store.store_video_data()
print(store.videos)