import json
"""
each product should have a title, a tag, a 10 second video and optionally pictures
maybe add a photo by a 

"""
class product:
    def __init__(self,video):
        self.video=video
        self.pictures=[]

    def addPhoto(self,photo):
        """
        need to check to make sure a photo is a singular photo and not a group or
        :param photo: a singular photo
        :return: a success message or a failure message
        """
        if (len(self.pictures)>=10):
            return "you must first delete a picture to add a new one"
        else:
            self.pictures.append(photo)
            return "photo successfully added"

