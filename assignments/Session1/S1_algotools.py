# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief exercise of miscellaneous algorithm

##import numpy for array
import numpy

##import random for random number generator
import random


## calculate the positve number average of the table
#@param table : list of number to calculate the average
#@return average of the list
def average_above_zero(table) :
    
    result = 0
    n_number = 0
    
    if not table:
        raise ValueError("table is empty")
        
    for number in table :
            
        if number > 0 :
            try :
                result += number
                n_number += 1
            except TypeError :
                continue
        
    if n_number > 0 :
        result /= float(n_number)
        
    return float(result)


##give the highest value of a table
#@param table where we want the highest value
#@return index of the highest value of the table and his value
def max_value(table) :

    if not table :
        raise ValueError("table is empty")
    
    n_max = table[0]
    i_max = 0
    for i,number in enumerate(table) :
        if number > n_max :
            n_max = number
            i_max = i

    return i_max, float(n_max)


##reverse a reverse
#@param table to reverse
#@return table reversed
def reverse_table(table) :
    
    if not table :
        raise ValueError("table is empty")

    length = len(table)
    r_index = length - 1
    for i in range(length/2) :
        table[i], table[r_index] = table[r_index], table[i]
        r_index -= 1

    return table


##give cordinates of the object in a binary image
#@param m_2d is the binary image
#@return cordinates of the objects 
def roi_bbox(m_2d) :

    if not isinstance(m_2d, numpy.ndarray):
        raise ValueError("parameter is not a numpy array type")
    
    x_min = 0
    x_max = m_2d.shape[1] - 1
    y_min = 0
    y_max = m_2d.shape[0] - 1

    find_min = False
    
    for y in range(m_2d.shape[0]) :
        for x in range(m_2d.shape[1]) :
            if m_2d[y,x] > 0 :
                y_min,x_min = y,x
                find_min = True
                break
        if (find_min) :
            break

    for y in range(y_min+1, m_2d.shape[0]) :
        if m_2d[y,x_min] == 0 :
            y_max = y-1
            break

    for x in range(x_min+1, m_2d.shape[1]) :
        if m_2d[y_min,x] == 0 :
            x_max = x-1
            break
            

    return numpy.array([[y_min,x_min],[y_min,x_max],[y_max,x_min],[y_max,x_max]])

##fill randomly a character table with the caracter "X"
#@param table we want to fill
#@param vfill how many cells do we want to fill in the table ?
#@return table filled randomly
def random_fill_sparse(table, vfill) :

    if not isinstance(table, numpy.ndarray):
        raise ValueError("parameter is not a numpy array type")
    empty_cell = []
    i_coord = 0

    for y in range(table.shape[0]) :
        for x in range(table.shape[1]) :
            empty_cell.append((y,x))
            
    if (vfill > len(empty_cell)) :
        raise ValueError("Your array is too small")

    for i in range(vfill) :
        i_coord = alea(len(empty_cell))
        table[empty_cell[i_coord][0], empty_cell[i_coord][1]] = "X"
        del empty_cell[i_coord]

##give a random number
#@param v interval of the number which will be generate
#@return a random number
def alea(v) :
    return random.randint(0, v-1)

##remove all white space in the string
#@param table string where we want to remove its white spaces
#@return a string whithout its white spaces
def remove_whitespace(table) :
    return "".join( [c for c in table if c not in " \n\t\r"] )


##shuffle a list
#@param list which will be shuffle
#@return list shuffled
def shuffle(list_in) :

    list_cp = list_in[:]
    list_shuffle = []

    for i in range(len(list_cp)) :
        i_coord = alea(len(list_cp))
        list_shuffle.append(list_cp[i_coord])
        del list_cp[i_coord]

    return list_shuffle

#(a) 10,15,7,1,3,3,9
#       --> 1,15,7,10,3,3,9
#       --> 1,3,7,10,15,3,9
#       --> 1,3,3,10,15,7,9
#       --> 1,3,3,7,15,10,9
#       --> 1,3,3,7,9,10,15

#(b) yes it does
#(c) n(n-1)/2 itérations
#(d) 5 swap
#(e) same as iteration
#(f) O(n²)
#(g)
#size   |swap           |comparaisons
#50     |47             |1225
#100    |95             |4950
#500    |494            |124750            

##sort a list with the sort selective algorithm
#@param list to sort
#@return list sorted
def sort_selective(list_in) :
    compare = 0
    permutation = 0
    for i in range(len(list_in)) :
        i_min = i
        for j in range(i + 1, len(list_in)) :
            compare += 1
            if list_in[j] < list_in[i_min] :
                i_min = j
                
        if i_min != i : 
            #swap python style
            list_in[i_min], list_in[i] = list_in[i], list_in[i_min]
            permutation += 1

    if __debug__ :
        print("(DEBUG)sort selective : \nlength : {}\ncompare : {}\npermutation : {}".format(len(list_in), compare, permutation))
        
    return list_in



#(a) 10,15,7,1,3,3,9
#       --> 10,15,7,1,3,3,9
#       --> 10,7,15,1,3,3,9
#       --> 10,7,1,15,3,3,9
#       --> 10,7,1,3,15,3,9
#       --> 10,7,1,3,3,15,9
#       --> 10,7,1,3,3,9,15
#       --> etc...

#(b) yes it does
#(c) n(n-1) itérations
#(d) too many
#(e) same as iteration
#(f) O(n²)
#(g)
#size   |swap           |comparaisons
#50     |719            |2450
#100    |2537           |9900
#500    |64325          |249500    

##sort a list with the sort bubble algorithm
#@param list to sort
#@return list sorted
def sort_bubble(list_in) :
    compare = 0
    permutation = 0
    for i in range(len(list_in)) :
        #this is an optimization : no check last position once swap
        #for j in range(0, len(list_in)-i-1) :
        for j in range(0, len(list_in)-1) :
            compare += 1
            if list_in[j] > list_in[j+1] :
                permutation += 1
                list_in[j], list_in[j+1] = list_in[j+1], list_in[j]
                
    if __debug__ :
        print("(DEBUG)sort bubble : \nlength : {}\ncompare : {}\npermutation : {}".format(len(list_in), compare, permutation))
             
    return list_in


#running time

if __name__ == '__main__' :
    
    print(average_above_zero([1,2,3.2,"zpefk"]))
    print(max_value([1]))
    print(reverse_table([1,2,3,4,5]))

    tab = numpy.array([[0,0,0],
                       [0,0,0],
                       [1,1,1],
                       [1,0,0],
                       [1,0,0],
                       [1,0,0]])
    print(roi_bbox(tab))

    chartab = numpy.chararray((10,14))
    chartab[:] = "O"
    random_fill_sparse(chartab, 42)
    print(chartab)

    word = "\rzpzke\n    zepfok  \tfkpzeofk   "
    print(remove_whitespace(word))

    list_to_shuffle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(shuffle(list_to_shuffle))

    list_to_sort_selective = [alea(1000) for _ in range(500)]
    print(list_to_sort_selective)
    print(sort_selective(list_to_sort_selective))


    list_to_sort_bubble = [alea(1000) for _ in range(500)]
    print(list_to_sort_bubble)
    print(sort_bubble(list_to_sort_bubble))

