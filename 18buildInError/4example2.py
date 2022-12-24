#rise example example2
class Mobile:
        def __init__(self,name):
                self.name=name

class MobileStore:
        def __init__(self):
                self.mobiles=[]
        def add_mobile(self,new_mobile):
                if isinstance(new_mobile,Mobile):
                        self.mobiles.append(new_mobile)
                else:
                        raise TypeError('new mobile should be object of mobile class')

oneplus=Mobile('one+ 6')
samsung='samsung galaxy s8'
mobostore=MobileStore()
mobostore.add_mobile(oneplus)
mobo_phone=mobostore.mobiles
print(mobo_phone[0].name)