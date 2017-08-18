'''
Created on Jun 4, 2014

@author: jimmy.roland
'''
from abc import ABCMeta, abstractmethod

class IVendMachine(object):
    '''
    Determines the required methods of how you interface with a vending machine.
    '''
    __metaclass__ = ABCMeta


    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    
    @abstractmethod
    def addFunds(self, amt):
        '''Adds money to the current machine.
        
        Args:
            amt: cash value to add to the machine.
            
        Returns:
            N/A
        '''
        pass
    
    
    @abstractmethod
    def selectItem(self, itemLocation):
        '''Selects an item by location in current machine.
        
        Args:
            itemLocation: id of location of the item you want to be returned.
            
        Returns:
            The selected item.
        '''
        pass
    
    @abstractmethod
    def addProduct(self, prod, cnt, locationId):
        '''Add a product to the machine.
        
        Args:
            prod: ProductBase to add to this machine.
            cnt: Number of this product you want to add to this machine.
            locationId: Which location this item will be placed.
            
        Returns:
            Numeric value for any over stock that cannot fit in the machine.
        '''
        pass
    
    
    @abstractmethod
    def setPrice(self, locationId, price):
        '''Changes the price of a location.
        
        Args:
            locationId: location within the machine for the price to be set.
            price: cost for any item at this location in the machine.
            
        Return:
            N/A
        '''
        pass
    
    
    @abstractmethod
    def cancel(self):
        '''Ends the machine and returns any excess funding.
        '''
        pass
    
    
    @abstractmethod
    def displaySelection(self):
        '''Prints to the screen all of the front slots of the machine and prices.
        '''
        pass
    
    
    @abstractmethod
    def displayStatistics(self):
        '''Prints to screen # of transactions and amount of money collected.
        '''
        pass