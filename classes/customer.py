# Write you Customer Class here
# """TO DO
# 1. add customer 
# 2. rent out video
# 3. return video
# 4. con
# """

from store import Store
from video import Video
# from classes.store import Store
# from classes.video import Video

class Customer:
    total_customers = 0
    all_customers = []
    customers = {} #<--class variable/attribute

    def __init__(self, _id=None, first_name=None, last_name=None, _account_type=None, _current_video_rentals=[]):#<--instance attributes
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = _current_video_rentals #or we can put the list here _current_video_rentals = []
        # self._id = Customer.total_customers
        # Customer.total_customers += 1

        # Customer.customers.update(Store.load_data("customers"))
        # Customer.customers.update(Store.load_data(Store.row))
        # print(Customer.customers)

        # Customer.all_customers.append(self)



    @classmethod#<--class method
    def list_customers(cls):
        Store.load_data("customers")
        # data = Store.load_data("customers")
        # Customer.all_customers.append(data)
        # return Customer.all_customers

    # @classmethod#<--getter
    # def get_id(cls):
    #     customers = Store.load_data("customers")
    #     # print(customers)
    #     # for i in customers:
    #     #     Customer.all_customers.append(i)
    #     # # Customer.all_customers = []
    #     print(customers)

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
        pass

    @property#<--setter
    def set_rent_a_video(self, _current_video_rentals):#<--current video rentals available in the inventory
        pass

    @property
    def set_return_a_video(self, _current_video_rentals):#<--return whichever video rentals are checked out to that customer by id
        pass

    @classmethod#<--class method
    def get_customer_by_id(cls):
        # list[Store.load_data("customers")]
        # list(Customer.customers.keys())
        pass

    def get_customer_rented_videos(self):#<--instance method
        pass
    
    @classmethod
    def create_customer(cls):
        pass

    
# Customer.load_data()
# Customer.list_customers()
customer_instance = Customer("Ann")
Customer.list_customers()

    
    