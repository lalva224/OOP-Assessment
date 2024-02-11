# Write you Customer Class here
# """TO DO
# 1. add customer 
# 2. rent out video
# 3. return video
# 4. con
# """

# from store import Store
# from video import Video
from classes.store import Store
from classes.video import Video

class Customer(Store):
    total_customers = 0
    customers = {d["id"]: d for d in Store.load_data("customers")}#<--class variable/attribute
    # customers = {int(d["id"]): d for d in Store.load_data("customers")}#making the key int
    print(customers)
    # print(customers.get("id")("account_type"))

    def __init__(self, _id, first_name, last_name, _account_type, _current_video_rentals):#<--instance attributes
        # super().__init__(self, id=None)
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = _current_video_rentals #or we can put the list here _current_video_rentals = []
        

    def __str__(self):
        return f"ID: {self._id} | Fullname: {self.first_name} {self.last_name} | AccountType: {self._account_type} | Current Video Rentals: {self._current_video_rentals}"


    @classmethod#<--getter
    def get_id(cls, _id):
        if Customer._id in Customer.customers:
            # print(f"Found: {Customer.customers[id]}")
            print(Customer._id)
        # customers = list(Store.load_data("customers"))
        # print(customers)
        # for i in customers:
        #     Customer.all_customers.append(i)
        # # Customer.all_customers = []
        # print(customers)
        # pass

    # @property#<--getter
    # def get_id(self, _id):
    #     customers = Store.load_data("customers")
    #     # print(customers)
    #     for i in customers:
    #         Customer.all_customers.append(i)
    #     # Customer.all_customers = []
    #     print(customers)

    @property
    def get_current_video_rentals(self, _current_video_rentals):#<--see whatever videos are checked out to that customer by id, possibly list or str from list
        return self.get_current_video_rentals
        # Customer.get_customer_by_id()
        # if "id" in Customer.customers:
        #     return Customer.customers.current_video_rentals

    @get_current_video_rentals.setter#<--setter
    def set_rent_a_video(self):#<--current video rentals available in the inventory
        # self.video = new_set_rent_a_video#<--?
        pass

    @get_current_video_rentals.setter
    def set_return_a_video(self):#<--return whichever video rentals are checked out to that customer by id
        if "id" in Customer.customers:
            pass

    @classmethod#<--class method
    def get_customer_by_id(cls):
        if "id" in Customer.customers:
            return Customer.customers["id"]


    def get_customer_rented_videos(self):#<--instance method
        for key, value in Customer.customers.items():
            # print(key, value)
            if "id" in Customer.customers == isinstance(value, dict): 
                return value.get("current_video_rentals")
#***********may need to turn dictionary of dictionaries into a list to work with data more easily
            #this statement works, while looping through the data---
            # if isinstance(value, dict):
            #     print(value.get("current_video_rentals"))

    
    @classmethod
    def create_customer(cls):
        return cls.create_customer

    
# Customer.load_data("customers")
# Customer.list_customers()
# customer1 = Customer(7, "Becky", "Boop", "sx", [])
# customer1.get_id(7)
# Customer.list_customers()
# Store.load_data("customers")
# Customer.get_id(3)
# _id=None, first_name=None, last_name=None, _account_type=None, _current_video_rentals=[]
    
    