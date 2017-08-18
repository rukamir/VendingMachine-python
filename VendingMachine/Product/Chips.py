'''
Created on Jun 4, 2014

@author: jimmy.roland
'''

from VendingMachine.Machine.ProductBase import ProductBase

class Chips(ProductBase):
    '''
    classdocs
    '''
    name = "Chips"


    def __init__(self):
        '''
        Constructor
        '''
        print("Chips ctor activated!!")
  
    
    def sound(self):
        '''
        The sound the item makes when it falls.
        '''
        print("Crinkle!")