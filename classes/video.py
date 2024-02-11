# Write your video Class here
# """TO DO
# """
# from store import Store
from classes.store import Store

class Video(Store):

    videos = {d["id"]: d for d in Store.load_data("inventory")}

    def __init__(self, _id=0, _title=None, _rating=None, release_year=0, _copies_available=0):
        self._id = _id
        self._title = _title
        self._rating = _rating
        self.release_year = int(release_year)
        self._copies_available = int(_copies_available)

    @classmethod#<--getter, class method
    def get_a_video_by_title(cls, title):
        if Video.get_title in Video.videos:
            return f"Video.title is in {Video.videos[Video.title]}"
        else:
            return "That title is not available."

    @classmethod#<--class method
    def list_inventory(cls):
        video1 = Store.load_data("inventory")
        video = {d["id"]: d for d in video1}
        return video

    @property#<--getter, n/a input
    def get_id():
        pass

    @property#<--n/a input
    def get_title():
        pass

    @property#<--n/a input
    def get_rating():
        pass

    @property#<--n/a input
    def get_copies_available():#<--parent:_copies_available
        pass

    @property#<--integer for input, possibly from store inventory by id
    def set_rent_a_video(int):#<--parent: _copies_available
        pass

    @property#<--integer for input, possibly from store inventory by id
    def set_return_a_video(int):#<--parent: _copies_available
        pass

# video_instance = Video("Ghostbusters")
# print(video_instance._title)
# Video.list_inventory()
# store_instance = Store("Blockbuster")
# store_instance.load_data("inventory")
# video_instance.get_a_video_by_title("The Godfather")