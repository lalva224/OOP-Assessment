# # ENSURE EVERYTHING BELOW IS COMMENTED WHEN YOU SUBMIT YOUR ASSESSMENT AND RUN TESTS
from classes.store import Store
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx, Customer_px
from classes.customer import Customer
from classes.video import Video

store = Store("BlockBuster")
store.store_video_data()
store.store_customer_data()
print(store.videos[1].title)
def view_inventory(store):
    return store.videos

def view_customer_rented_videos(store):
    customer_id = int(input("Give me customer id: "))
    customer = find_customer_by_id(store,customer_id)
    if customer==None:
        return "Customer Not Found"
    return customer.video_rentals 

def find_customer_by_id(store,input_id):
    for customer in store.customers:
        if customer.id==input_id:
            return customer

def add_new_customer(store):
    print("Enter the following details: ")
    id = input("Id: ")
    if id in Customer.customer_ids:
        print("Sorry Id taken please use another one!")
        return
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    account_type = input("Account Type: ")
    customer = None
    match account_type:
        case "sx":
            customer = Customer_sx(id,account_type,f_name,l_name,[])
        case "sf":
            customer = Customer_sf(id,account_type,f_name,l_name,[])
        case "px":
            customer = Customer_px(id,account_type,f_name,l_name,[])
        case "pf":
            customer = Customer_pf(id,account_type,f_name,l_name,[])
    store.customers.append(customer)

def rent_video(store):
    customer_id = int(input("What is your customer id?: "))
    customer = find_customer_by_id(store,customer_id)
    if customer==None:
        print("Sorry customer not found!")
        return
    view_inventory(store)
    title = input("Please Enter a title to rent: ")

    movie_to_rent = find_movie_by_title(store,title)
    customer_type = customer.account_type
    rented_movies = len(customer.video_rentals)

    #is video in inventory?
    if movie_to_rent not in store.videos:
        return "Title not found"
    #Is there enough available copies? AC >0?
    if movie_to_rent.copies_available==0:
        return "No copies available at the moment"
    #if sx and rented_movies ==1 then cannot purchase
    if (customer_type =='sx' or customer_type== 'sf')and rented_movies==1:
        return "Sorry Customers may only Rent 1 movie at a time!"
    #if px and rented_movies==3 then cannot purchase
    if  (customer_type =='px' or customer_type =='pf')and rented_movies==3:
        return "Sorry Premium Customers may only rent up to 3 movies at a time!"
    #if sf and rented movies ==1 OR movie_to_rent == 'r' then cannot purchase
    if (customer_type =='sf' or customer_type== 'pf') and movie_to_rent.rating == 'R':
        return "Sorry family members cannot purchase movies rated R!"

    ## if reached here then succesful purchase
    movie_to_rent.copies_available-=1
    customer.video_rentals.append(movie_to_rent)

def return_video(store):
    customer_id = int(input("Give me customer id: "))
    customer = find_customer_by_id(store,customer_id)
    if customer==None:
        return "Customer Not Found"
    #display customers current videos. If there are none then encourage them to purchase!
    videos = customer.video_rentals
    if videos==0:
        print("No videos found! Would you like to rent?")
    print(customer.video_rentals)
    #get movie title, then use helper to get the movie object
    movie_title = input("Which movie title would you like to return?:  ")
    movie = find_movie_by_title(store,movie_title)

    movie.copies_available+=1
    customer.video_rentals.remove(movie)


def find_movie_by_title(store,title_name):
    for video in store.videos:
        if video.title == title_name:
            return video
        
while True:
    print("""
   == Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
   """)
    user_input = int(input("Please select an option: "))
    if user_input==1:
        print(view_inventory(store))
    elif user_input==2:
        print(view_customer_rented_videos(store))
    elif user_input ==3:
        print(add_new_customer(store))
    elif user_input ==4:
        print(rent_video(store))
    elif user_input==5:
        print(return_video(store))
    if user_input==6:
        break

 


