# Write you Customer Class here
# """TO DO
# 1. add customer 
# 2. rent out video
# 3. return video
# 4. con
# """
from classes.store import Store

class Customer(Store):
    total_customers = 0
    # all_customers = []
    customers = {} #<--class variable/attribute

    def __init__(self, _id, first_name, last_name, _account_type, _current_video_rentals=[]):#<--instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = _current_video_rentals #or we can put the list here _current_video_rentals = []
        self._id = Customer.total_customers
        Customer.total_customers += 1

        Customer.all_customers.append(self)

    @property#<--getter
    def get_id(self, _id):
        pass

    @property
    def get_current_video_rentals(self, _current_video_rentals):#<--see whatever videos are checked out to that customer by id, possibly list or str from list
        pass

    @property#<--setter
    def set_rent_a_video(self, _current_video_rentals):#<--current video rentals available in the inventory
        pass

    @property
    def set_return_a_video(self, _current_video_rentals):#<--return whichever video rentals are checked out to that customer by id
        pass

    @classmethod#<--class method
    def get_customer_by_id(cls):
        pass
        # Store.load_data("customers")

    def get_customer_rented_videos(self):#<--instance method
        pass
    
    @classmethod
    def create_customer(cls):
        pass

    
# Customer.load_data()
    