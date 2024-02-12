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
import csv

class Customer(Store):
    total_customers = 0

    customers = {d["id"]: d for d in Store.load_data("customers")}#<--class variable/attribute
    

    def __init__(self, _id, first_name, last_name, _account_type, _current_video_rentals=[]):#<--instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = _current_video_rentals #or we can put the list here 
        self._id = _id

        
    def __str__(self):
        return f"ID: {self._id} | Fullname: {self.first_name} {self.last_name} | AccountType: {self._account_type} | Current Video Rentals: {self._current_video_rentals}"
    
    def __repr__(self):
        return f"ID: {self._id} | Fullname: {self.first_name} {self.last_name} | AccountType: {self._account_type} | Current Video Rentals: {self._current_video_rentals}"


    @property
    def get_current_video_rentals(self):#<--see whatever videos are checked out to that customer by id, possibly list or str from list
        current_videos = []
        id_key = ""
        list_of_dicts = [value for value in Customer.customers.values()]
        for el in list_of_dicts:
            id_key = el["id"]
            # print(id_key)
            if id_key:
                # print(list(el.values())[-1])#<--got the current videos
                current_videos.append(list(el.values())[-1])
                # return list(el.values())[-1]#<--got the current videos
                return current_videos



        # pass
        # self.get_customer_by_id(self._id)
        # if "id" in Customer.customers:
        #     return f"Getting current video rentals: {Customer.customers.current_video_rentals}"
            # return Customer.customers.current_video_rentals






    # @get_current_video_rentals.setter#<--setter
    # def set_rent_a_video(self, rent_videos):#<--current video rentals available in the inventory
    #     # self.video = new_set_rent_a_video#<--?
    #     if isinstance(rent_videos, str):
    #         self._current_video_rentals = rent_videos
    #     else:
    #         print("Must be string")





    # @get_current_video_rentals.setter
    # def set_return_a_video(self):#<--return whichever video rentals are checked out to that customer by id
    #     pass




    @classmethod#<--class method
    def get_customer_by_id(cls, _id):
        # current_videos = []
        id_key = ""
        list_of_dicts = [value for value in Customer.customers.values()]
        for el in list_of_dicts:
            id_key = el["id"]
            # print(id_key)
            return id_key
            # if id_key:
            #     print(id_key)
            #     # return Customer.customers.get()
            #     print(cls.customers.get(cls.first_name))
                # print(list(el.values())[2])#<--got the current names
                # return list(el.values())[3]#<--got the current videos



    
    # @classmethod
    # def create_customer(cls):
    #     return cls.create_customer
    