import sys
sys.path.append('../') 
from OOP.OOP_lesson import *

def test_custom_exception():
    num=150
    assert Exception,num==150
def test_product() ->None :
    product1=product("Test",100,0)
    assert product1.quantity==0, product1.name=="test"

def test_divide_nuber():
    num1=50
    num2=0
    assert ZeroDivisionError