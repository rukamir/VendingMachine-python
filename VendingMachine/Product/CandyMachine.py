'''
Created on Jun 20, 2014

@author: jimmy.roland
'''
from VendingMachine.Machine.IVendMachine import IVendMachine
from array import array
from collections import list
from collections import defaultdict

class CandyMachine(IVendMachine):
    '''
    This is the a machine that implements the IVendMachine interface.
    '''
    _totalFunds         = 0.0               # Total cost of combined purchases
    _transactionTotal   = 0                 # Total number of transactions
    _allowance          = 0.0               # amount available to spend
    _locationCount      = 6                 # number of locations in machine
    _itemLimit          = 10                # item limit per location
    _prices             = array('f')        # Holds prices per location
    _inventory          = defaultdict(list)
    

    def __init__(self):
        '''
        Constructor
        '''
        print("Candy Machine open for business!!")
        
        # Zero out prices
        for _ in range(0, self._locationCount):
            self._prices.append(0.0)
            
            
    def addFunds(self, amt):
        '''Adds spendable money to the machine. Return unused money with cancel().
        '''
        if (amt > 0):
            self._allowance = amt
            print("Added $" + str(amt) + ".")
        else:
            print("No funds added. Available funds: {}".format(*self._allowance))
        
        
    def selectItem(self, itemLocation):
        # Validate:
        #    Location
        #    Proper funding
        #    Item is available in given location
        item = ""
        if (self._locationCount < itemLocation):
            print("Invalid Location!")
            return
        
        if (self._allowance >= self._prices[itemLocation]):
            #print(self._inventory[itemLocation])                
            if (self._inventory[itemLocation]):
                item = self._inventory[itemLocation].pop(0)
        else:
            print("Invalid funds for this location.")
            return
        
        # Test to see if item is valid
        if (not item):
            print("Invalid item!")
            item = None
        else:
            item.sound()
            self._allowance -= self._prices[itemLocation]
            self._totalFunds += self._prices[itemLocation]
            self._transactionTotal += 1
            
        print(`self._allowance` + " left.")
        return item
    
    
    def addProduct(self, prod, cnt, locationId):
        # Validate:
        #    Location ID
        #    Room for more
        retAmt = cnt
        if (self._locationCount >= locationId):
            while (len(self._inventory[locationId]) < self._itemLimit & retAmt > 0):
                self._inventory[locationId].append(prod)
                retAmt -= 1
        else:
            print("Invalid location!!!")
            
        # Notify user of what happened
        print("Added " + (cnt - retAmt) + " with " + retAmt + " left over.\n")
        return retAmt
       
        
    def setPrice(self, locationId, price):
        if (locationId <= self._locationCount):
            self._prices[locationId] = price
        else:
            print("Not a valid location. Try another selection.")
            
            
    def cancel(self):
        '''Aborts any further transactions and returns excess funding.'''
        print("Money has been returned.")
        retMoney = self._allowance
        self._allowance = 0.0
        return retMoney
    
    
    def displaySelection(self):
        for i in self._inventory:
            print(`self._prices[i]` + ": Location " + `i` + " has " + self._inventory[i][1].getProductName())
    
    
    def displayStatistics(self):
        printValues = (self._transactionTotal, self._totalFunds)
        print("**************************\n****Machine Statistics****\n**************************\nTotal Transactions: {0}\nTotal income: {1}\n**************************".format(*printValues))
        