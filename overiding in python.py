class parent():
    voice='rough'
    hair='brown'
    eyes='blue'

    def intro (self):
        return 'i am a parent class'

class child():
    def intro(self):   #method overriding
        return 'i am a child class'
obj=child()

