
class GNSS(Device):
    def __init__(self,id):
        super(Device,self).__init__(id)
    def latitude(self):
        pass
    def longitude(self):
        pass
    def quality_signal(self):
        pass

class GPS(GNSS):
    def __init__(self,id):
        super(GNSS,self).__init__(id)
    def latitude(self):
        super(GNSS,self).latitude()
    def longitude(self):
        super(GNSS,self).longitude()
    def quality_signal(self):
        super(GNSS,self).quality_signal()

class Galileo(GNSS):
    def __init__(self,id):
        super(GNSS,self).__init__(id)
    def latitude(self):
        super(GNSS,self).latitude()
    def longitude(self):
        super(GNSS,self).longitude()
    def quality_signal(self):
        super(GNSS,self).quality_signal()


class Glonass(GNSS):
def __init__(self,id):
        super(GNSS,self).__init__(id)
    def latitude(self):
        super(GNSS,self).latitude()
    def longitude(self):
        super(GNSS,self).longitude()
    def quality_signal(self):
        super(GNSS,self).quality_signal()
