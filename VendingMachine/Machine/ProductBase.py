'''
Created on Jun 4, 2014

@author: jimmy.roland
'''

#from abc import ABCMeta, abstractmethod


class ProductBase(object):
    '''
    Basic product with no description.
    '''
    #__metaclass__ = ABCMeta
    
    name = ''

    #@abstractmethod
    def __init__(self):
        '''
        Constructor
        '''
        print("!!Default used!!")
        
        
    '''
    Returns a string of the products name.
    '''
    def getProductName(self):
        return self.name
    
    
    '''
    OVERWRITE: Return a string representing product falling.
    '''
    #@ProductBase.sound
    def sound(self):
        print("Item released!")