# Write you Customer Class here
# """TO DO
# 1. add customer 
# 2. rent out video
# 3. return video
# 4. con
# """
# from store import Store
# from video import Video
class Customer:
    customer_ids = set()
    def __init__(self,id,account_type,f_name,l_name,video_rentals):
        self.id = int(id)
        Customer.customer_ids.add(id)
        self.f_name = f_name
        self.l_name = l_name
        self.video_rentals = list(video_rentals)
        self.account_type = account_type

    def __repr__(self):
        return f"Id:{self.customer_id}| First Name : {self.f_name} | Last Name : {self.l_name} Account Type: {type(self).__name__}\n"


    def add_video_rental(self,video):
        self.video_rentals.append(video)
    
    def view_video_rental(self):
        return self.video_rentals