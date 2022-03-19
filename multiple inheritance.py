#inheritance
class godfather():
    eyes="yellowish"

    def intro(self):
        return "i am godfather"
    

class dad(godfather):
    
    hair="brown"
    nose="long & straight"
    voice="rough"

    def intro(self):
        return "i am dad class"
    
class mom(godfather):
    face="round"
    skin="fair"
    

    def intro(self):
        return "i am mom class"
    
class child(mom,dad):
    voice="sweet"
    def intro(self):
        return "i am child class"

obj=child()
