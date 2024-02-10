# Write your Store Class here
# """TO DO
# 1. read csv and load both video and customer data to terminal program
# 2. ability to be able to see the customer database and the types of accounts each customer has
# 3. ability to run store in terminal program
# """

import csv

class Store:
    def __init__(self, name):#<--instance attributes
        self.name = name

    def customer_type_maker(self):#<--instance method, input from customer class so you can see the customer list and be able to change the type of account each customer has
        pass


    def load_data(file):#<--instance method, input file name, ie inventory or customer, no return, just loading data from csv
        # video_list = []
        with open(f'../data{file}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                # print(', '.join(row))
        # return video_list


    def run_the_store():#<-- instance method, no input, example return "Thank you, please come again!"
        pass

Store.load_data()