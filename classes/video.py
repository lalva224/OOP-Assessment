# Write your video Class here
# """TO DO
# """
# from store import Store
class Video:
    def __init__(self,id, title,rating,release_year,copies_available):
        self.id = int(id)
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available= int(copies_available)

    def __repr__(self):
        return f"Id: {self.id}| Title:{self.title}| Rating: {self.rating} | Release Year: {self.release_year} | Number of Copies: {self.copies_available}\n"

