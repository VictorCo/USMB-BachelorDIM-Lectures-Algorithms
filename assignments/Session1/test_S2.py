# -*- coding: utf-8 -*-

import pytest
import numpy

#for array not numpy 
#from collections import Counter


from S1_algotools import *

##Unit testing
#Module : S1_algotools.py
#Function : average_above_zero
def test_averageAboveZero_emptyTable():
    table = []
    with pytest.raises(ValueError) :
        average_above_zero(table)

def test_averageAboveZero_noPostiveNumbers():
    table = [-1,-2,-4,-8]
    assert average_above_zero(table) == 0.0

def test_averageAboveZero_stringValue():
    table = ["hello", "test"]
    assert average_above_zero(table) == 0.0

def test_averageAboveZero_stringValue():
    table = ["hello", "test"]
    assert average_above_zero(table) == 0.0

def test_averageAboveZero_mixUpType():
    table = ["hello", -1, (1,4)]
    assert average_above_zero(table) == 0.0

def test_averageAboveZero_onlyPositiveIntValue():
    table = [2,4,8,16]
    assert average_above_zero(table) == 7.5

def test_averageAboveZero_onlyPositiveValue():
    table = [1.5,2.5,10,10]
    assert average_above_zero(table) == 6

def test_averageAboveZero_positiveAndNegativeValue():
    table = [-1,5,8,-23,-321]
    assert average_above_zero(table) == 6.5

def test_averageAboveZero_positiveValueWithMixUpType():
    table = [1,2,3,4,5,(1,23,68),-4,"str"]
    assert average_above_zero(table) == 3.0


##Unit testing
#Module : S1_algotools.py
#Function : max_value

def test_maxValue_emptyTable():
    table = []
    with pytest.raises(ValueError) :
        max_value(table)

def test_maxValue_onlyPositiveValue():
    table = [5,4,8,3,1]
    assert max_value(table) == (2,8)

def test_maxValue_onlyNegativeValue():
    table = [-1,-2,-1,-5,-3]
    assert max_value(table) == (0,-1)

def test_maxValue_positiveAndNegativeValue():
    table = [5,-3,-30,30,0]
    assert max_value(table) == (3,30)

def test_maxValue_mixUpType():
    table = [5,-3,-30,30,0,"str"]
    with pytest.raises(ValueError) :
        max_value(table)

##Unit testing
#Module : S1_algotools.py
#Function : reverse_table

def test_reverseTable_emptyTable():
    table = []
    with pytest.raises(ValueError) :
        reverse_table(table)

def test_reverseTable_intType():
    table = [5,4,8,3,1]
    assert reverse_table(table) == [1,3,8,4,5]

def test_reverseTable_MixUpType():
    table = ["str",[4,2,3],(1,1,2),3,1]
    assert reverse_table(table) == [1,3,(1,1,2),[4,2,3],"str"]


##Unit testing
#Module : S1_algotools.py
#Function : reverse_table

def test_roiBbox_emptyTable() :
    table = []
    with pytest.raises(ValueError) :
        roi_bbox(table)

def test_roiBbox_noNumpyType() :
    table = [1,2,3]
    with pytest.raises(ValueError) :
        roi_bbox(table)

def test_roiBbox_square() :
     table = numpy.array([ [0,0,0],
                           [0,0,0],
                           [1,1,1],
                           [1,1,1],
                           [1,1,1],
                           [0,0,0] ])
     assert numpy.alltrue(roi_bbox(table) == numpy.array([[2,0],[2,2],[4,0],[4,2]]))


def test_roiBbox_triangle() :
     table = numpy.array([ [0,0,0],
                           [0,0,0],
                           [1,1,1],
                           [1,1,0],
                           [1,0,0],
                           [0,0,0] ])
     assert numpy.alltrue(roi_bbox(table) == numpy.array([[2,0],[2,2],[4,0],[4,2]]))


##Unit testing
#Module : S1_algotools.py
#Function : random_fill_sparse
def test_randomFillSparse_emptyTable():
    table = []
    with pytest.raises(ValueError) :
        random_fill_sparse(table,0)

def test_randomFillSparse_noNumpyType():
    table = []
    with pytest.raises(ValueError) :
        random_fill_sparse(table,0)

def test_randomFillSparse_vFillIsTooHigh():
    table = numpy.chararray((2,5))
    table[:] = "O"
    vFill = 100
    with pytest.raises(ValueError) :
        random_fill_sparse(table,vFill)

def test_randomFillSparse_countCross():
    table = numpy.chararray((10,14))
    table[:] = "O"
    vFill = 100
    num = 0
    random_fill_sparse(table,vFill)
    unique, counts = numpy.unique(table, return_counts=True)
    num = dict(zip(unique, counts))
    assert num["X"] == vFill
    

##Unit testing
#Module : S1_algotools.py
#Function : remove_whitespace

def test_removeWhitespace_emptyString():
    string = ""
    assert remove_whitespace(string) == ""

def test_removeWhitespace_removeAllTypeOfWhiteSpace():
    string = "\tHello\nThis is \rStroustrup    .\n\n\n"
    assert remove_whitespace(string) == "HelloThisisStroustrup."


##Unit testing
#Module : S1_algotools.py
#Function : sort_selective

def test_sortSelective_emptyList():
    list_in = []
    assert sort_selective(list_in) == []

def test_sortSelective_run():
    list_in = [1,0,-1,5,-3]
    assert sort_selective(list_in) == [-3,-1,0,1,5]


##Unit testing
#Module : S1_algotools.py
#Function : sort_bubble

def test_sortBubble_emptyList():
    list_in = []
    assert sort_bubble(list_in) == []

def test_sortBubble_run():
    list_in = [1,0,-1,5,-3]
    assert sort_bubble(list_in) == [-3,-1,0,1,5]
