# -*- coding: utf8 -*-
import random
'''
state 更新版
新的方法
状态是变化的量，将变化封装起来，将动作和行为放到状态里，这样每个状态只要实现它自己的那套行为。
为每个状态创建状态类，这些类负责在对应的动作下糖果机的行为

将动作和行为委托给状态类
添加游戏状态类
'''

#有25分钱的状态
class HasQuarterState(object):
    def __init__(self,gumballMachine):#传入糖果机的实例
        self.gumballMachine = gumballMachine

    def insertQuarter(self): #投入25分钱动作
        print("You cannot insert another quarter")

    def ejectQuarter(self): #退出25分钱动作
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        #之后糖果机的状态切换到没有25分钱状态

    def turnCrank(self):#转动曲柄动作
        print("You turned....")
        #加入游戏状态
        #产生随机数
        self.winner = random.randint(1, 50)
        #这个数为1你就赢了
        if self.winner == 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())
            
        #self.gumballMachine.setState(self.gumballMachine.getSoldState())
        #之后糖果机的状态切换到售出糖果状态

    def dispense(self): #发放糖果动作，这是个内部动作，此处实现没有作用
        print("No gumball dispense")

#糖果售罄状态
class SoldOutState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")
    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")
    def turnCrank(self):
        print("You turned, but there's no gumball")
    def dispense(self):
        print("No gumball dispense")

#没有25分钱状态
class NoQuarterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
    def ejectQuarter(self):
        print("You haven't inserted a quarter")
    def turnCrank(self):
        print("You turned, but there's no quarter")
    def dispense(self):
        print("You need to pay first")

#售出糖果状态
class SoldState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount()>0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

#游戏状态
class WinnerState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    # 你赢了，如果糖果没了，那就算了，只能白赢了；
    def dispense(self):
        print("You are winner! You get 2 gumball for youe quarter")
        if self.gumballMachine.getCount()==0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount()>0:
                self.gumballMachine.releaseBall()
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

#糖果机类
class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs
#=========创建每一个状态的状态实例====================#
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
#=========end=========================================#
        if self.count > 0:
            self.state = self.noQuarterState
#============每个状态的get方法和set方法===============#
    def getSoldOutState(self):
        return self.soldOutState
    def getNoQuarterState(self):
        return self.noQuarterState
    def getHasQuarterState(self):
        return self.hasQuarterState
    def getSoldState(self):
        return self.soldState
    def getWinnerState(self):
        return self.winnerState
    def setState(self, state):
        self.state = state
#=========end=========================================#
#============将方法委托给当前的状态===================#
    def insertQuarter(self):
        self.state.insertQuarter()
    def ejectQuarter(self):
        self.state.ejectQuarter()
    
    def turnCrank(self):
        if self.state == self.hasQuarterState:
            self.state.turnCrank()
            self.state.dispense()
        else:
            self.state.turnCrank()
    
    
#=========end=========================================#
    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1
#============检查状态和糖果数量的方法=================#
    def getState(self):
        print(self.state)
    def getCount(self):
        return self.count

def main():
    gumballMachine = GumballMachine(100)
    print(gumballMachine.getCount())
    for i in xrange(20):
        print("======================{0}====================".format(i+1))
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
    print(gumballMachine.getCount())

if __name__=='__main__':
    main()
