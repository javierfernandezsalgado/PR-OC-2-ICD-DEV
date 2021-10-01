

class Camera(Device):
    def __init__(self,id):
        super(Device,self).__init__(id)
    # Take a picture from the camera and deploy in the select folder
    # folder: File system folder when the picture is deployed
    def take_picture(self,folder):
        pass
    # Get a binary image.
    def get_image(self):
        pass
    #Take a video from the camera and deployed in the <<folder>>
    #Folder: Folder where the video is deployed.
    def take_a_video(self,folder):
        pass
