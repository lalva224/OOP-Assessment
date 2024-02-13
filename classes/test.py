class Customer:
    customer_count = 0
    def __init__(self,account_type,fname,lname):
        self.customer_id = Customer.customer_count + 1
        Customer.customer_count+=1
        self.fname = fname
        self.lname = lname
        self.video_rentals = []
    def __repr__(self):
        return f"Id:{self.customer_id}| First Name : {self.f_name} | Last Name : {self.l_name}\n"

    def add_video_rental(self,video):
        self.video_rentals.append(video)
    
    def view_video_rental(self):
        return self.video_rentals

class FreeCustomer(Customer):
     def __init__(self,f_name,l_name):
         #implicit customer object created
         super().__init__(f_name,l_name)

class PremiumCustomer(Customer):
    pass

# Example usage
# free_customer = FreeCustomer()
# premium_customer = PremiumCustomer()
# free_customer_2 = FreeCustomer()

customer1 = Customer("Mike","Hawk")
free_customer = FreeCustomer("Leandro","Alvarez")
premium_customer = PremiumCustomer("John","Smith")
print(type(customer1).__name__)



customer1.