from random import randint

class Die():
    def __init__(self,num_side=6):
        '''默认骰子为六面'''
        self.num_side=num_side
    
    def roll(self):
        '''返回一个位于1和骰子总面数中间的数'''
        return randint(1,self.num_side)