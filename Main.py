'''
Created on Jun 4, 2014

@author: jimmy.roland
'''

from VendingMachine.Product.Chips import Chips
from VendingMachine.Product.CandyMachine import CandyMachine

if __name__ == '__main__':
    x = ""
    #x = raw_input("Do something: ")
    #print(x)
    bag = Chips()
    print(bag.getProductName())
    
    print("Machine created!")
    mach = CandyMachine()
    mach.addFunds(10)
    mach.setPrice(2, 2)
    mach.setPrice(0, 0)
    mach.setPrice(1, 1)
    mach.addProduct(bag, 2, 2)
    mach.addProduct(bag, 2, 0)
    mach.addProduct(bag, 2, 1)
    mach.addProduct(bag, 2, 5)
    mach.displaySelection()  
    item = mach.selectItem(1)
    item = mach.selectItem(1)
    item = mach.selectItem(1)
    #print(item.getProductName())
    mach.displayStatistics()