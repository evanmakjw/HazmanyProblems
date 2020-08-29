class hazman():
    def __init__(self):
        self.maskCount = 0
        self.sanitizerCount = 0

    def give_mask(self):
        self.maskCount -= 1; 
        print("{0} masks left".format(self.maskCount) )

    def give_sanitizer(self):
        self.sanitizerCount -= 1; 
        

    def give_supplies(self, target):
        if self.maskCount > 0:
            self.give_mask(target)
            masked = True

        if self.sanitizerCount > 0:
            self.give_sanitizer(target)
            sanitized = True; 

        target.take_supplies(masked, sanitized)


    def pick_up_masks(self):
        self.maskCount += 5; 

    def pick_up_sanitiser(self):
        self.sanitizerCount+= 5;

    def clean_object(self, obj):
        obj.decontaminate();

    def test_citizen(self):
        pass
    # def send_to_isolate(self):

hazzy = hazman()
hazzy.give_mask()
print("hello")
    # body of the constructor