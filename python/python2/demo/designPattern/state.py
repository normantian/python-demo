# -*- coding: utf8 -*-
'''
 糖果机游戏
 其中一共有四个状态

售出糖果
糖果售罄
有25分钱
没有25分钱
操作糖果机会设计四个动作
投入25分钱
退回25分钱
转动曲柄
发放糖果 这个动作是糖果机内部的动作，机器自己调用
'''

class GumballMachine:
    def __init__(self, count):
        self.SOLD_OUT = 0 #糖果售罄状态
        self.NO_QUARTER = 1 #没有25分钱
        self.HAS_QUARTER = 2 #有25分钱
        self.SOLD = 3 #售出糖果状态
        self.state = self.SOLD_OUT  #初始状态为`没有25分钱状态`
        self.count = count  #设置一个糖果数量变量，它为0时就是糖果售罄的状态
        if self.count > 0:  #此处如果糖果数大于0，则状态为初始状态
            self.state = self.NO_QUARTER

    def insertQuarter(self): #投入25分钱动作
        if self.state == self.HAS_QUARTER:
            print "You cannot insert another quarter"
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print "You insert a quarter" 
        elif self.state == self.SOLD_OUT:
            print "You can't insert a quarter, the machine is sold out"
        elif self.state == self.SOLD:
            print "Please wait, we're already giving you a gumball"

    def ejectQuarter(self):   #退回25分钱
        if self.state == self.HAS_QUARTER:
            print "Quarter returned"
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print "You haven't inserted a quarter"
        elif self.state == self.SOLD:
            print "Sorry, you already turned the crank"
        elif self.state == self.SOLD_OUT:
            print "You can't eject, you haven't inserted a quarter yet"

    #转动曲柄动作
    def turnCrank(self):
        if self.state == self.SOLD:
            print("Turning twice doesn't get you another gumball!")
        elif self.state == self.NO_QUARTER:
            print("You turned, but there's no quarter")
        elif self.state == self.SOLD_OUT:
            print("You turned, but there's no gumball")
        elif self.state == self.HAS_QUARTER:
            print("You turned....")
            self.state = self.SOLD
            self.dispense()     #切换到发放糖果这个内部动作上
            
    def dispense(self):     #发放糖果动作
        if self.state == self.SOLD:
            print("A gumball comes rolling out the slot")
            self.count = self.count - 1     #发放一次糖果，糖果数量要减1
            if self.count == 0:    #糖果数量为0了，切换到糖果售罄的状态
                print("Oops, out of gumballs")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You need to pay first")
        elif self.state == self.SOLD_OUT:
            print("No gumball dispense")
        elif self.state == self.HAS_QUARTER:
            print("No gumball dispense")

    def getCount(self):
        print(self.count)
    def getState(self):
        print(self.state)

def main():
    gumballMachine = GumballMachine(2)
    gumballMachine.getCount()
    gumballMachine.getState()
    print("=====================================================")
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.ejectQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    gumballMachine.getCount()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    print("=====================================================")
    gumballMachine.turnCrank()

if __name__=='__main__':
    main()
