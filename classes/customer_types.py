# Write your independent Customer account type classes here
# """TO DO
# 1. control customer_pf by only allowing 3 rentals out at a time and no r rated movies
# 2. control customer_sf by allowing 1 video and no r rated movies
# 3. control customer_sx by allowing 1 rental irregardless of rating
# 4. control customer_px by allowing 3 rentals max irregardless of rating
# 5. manage customer id, first name, last name, current list of video rentals (by title), each separated by a forward slash "/"
# 6. make sure to limit a customer based on their account type
# """

from classes.customer import Customer


class Customer_pf(Customer):#<--overrides rent_a_video method to meet account conditions | "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies
    def __init__(self,id,account_type,first_name,last_name,video_rentals):
         #implicit customer object created-> This means customer count and video rentals taken care of
         super().__init__(id,account_type,first_name,last_name,video_rentals)

class Customer_sf(Customer):#<--overrides rent_a_video method to meet account conditions | "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
    def __init__(self,id,account_type,first_name,last_name,video_rentals):
         super().__init__(id,account_type,first_name,last_name,video_rentals)

class Customer_sx(Customer):#<--overrides rent_a_video method to meet account conditions| "sx" = standard account: max 1 rental out at a time
    def __init__(self,id,account_type,first_name,last_name,video_rentals):
         super().__init__(id,account_type,first_name,last_name,video_rentals)

class Customer_px(Customer):#<--overrides rent_a_video method to meet account conditions| "px" = premium account: max 3 rentals out at a time***inherits rent_a_video method that already meets account conditions, that's why it isn't imported to runner
    def __init__(self,id,account_type,first_name,last_name,video_rentals):
         super().__init__(id,account_type,first_name,last_name,video_rentals)