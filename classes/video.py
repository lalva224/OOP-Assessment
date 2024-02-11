# Write your video Class here
# """TO DO
# """
from store import Store
# from classes.store import Store

class Video:

    videos = {}

    def __init__(self, _id=0, _title=None, _rating=None, release_year=0, _copies_available=0):
        self._id = int(_id)
        self._title = _title
        self._rating = _rating
        self.release_year = int(release_year)
        self._copies_available = int(_copies_available)

    @classmethod#<--getter, class method
    def get_a_video_by_title(cls):
        pass

    @classmethod#<--class method
    def list_inventory(cls):
        Store.load_data("inventory")

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

# videos_instance = Video()
# Video.list_inventory()
store_instance = Store("Blockbuster")
store_instance.load_data("inventory")