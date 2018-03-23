'''
Created on Nov 19, 2017

@author: kai
'''
from multiprocessing import Pool

    
def cube (i,x) :
    return [i, x*x*x]
 
if __name__ == '__main__':
    inputList = [1,2,3,4,5]
    outputList = inputList[:]
    print (str(inputList))
    print (str(outputList))

    with Pool() as pool:
        result = pool.starmap(cube, enumerate(inputList))
    print (str(result))
    
    for i in result :
        outputList[i[0]] = i[1]
        
    print (str(outputList))