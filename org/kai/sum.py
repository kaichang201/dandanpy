'''
Created on Nov 18, 2017

@author: kai
'''
import math
from lib2to3.pytree import Node
from multiprocessing.semaphore_tracker import SemaphoreTracker

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matchList = []
        counter = 0
        for number in nums:
            if number in matchList :
                return (matchList.index(number), counter)
            matchList.append(target - number)
            counter += 1
            
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        returnValue = 0
        
        if (x >= 0) :
            returnValue = int(str(x)[::-1])
        else :
            returnValue = int(str(x * -1)[::-1]) * -1
        if (abs(returnValue) > math.pow(2, 31) - 1) :
            return 0
        else :
            return returnValue
        
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) :
            return False
        reverse = int(str(x)[::-1])
        if (reverse > 2147483647) :
            return False
        if (x == reverse) :
            return True
        return False
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanChart = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        returnValue=romanChart[s[::-1][0]]

        for i,c in enumerate(s[::-1][1:],start=1) :
            if (romanChart[s[::-1][i-1]] <= romanChart[c] ) :
                returnValue += romanChart[c]
            else :
                returnValue -= romanChart[c] 
        return returnValue
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs : # if list empty, return blank
            return ''
        if len(strs) == 1 : # if list only has 1 string, return it
            return strs[0]
        
        for i,s in enumerate(min(strs, key=len), start=0) :  # iterate through characters of shortest string
            for str1 in strs : # iterate through all other strings
                if (str1[i] != s) : # if a mismatch found
                    return min(strs, key=len)[0:i]     
        return min(strs, key=len)
    
    def isValid(self, s) :
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s :
            if c == ')' :
                if (len(stack) == 0 or stack.pop() != '(') :
                    return False
            elif c == '}' :
                if (len(stack) == 0) or stack.pop() != '{' :
                    return False
            elif c == ']' :
                if (len(stack) == 0) or stack.pop() != '[' :
                    return False
            else :
                stack.append(c)
        return len(stack) == 0
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2 :
            return l1 or l2
        if l1.val < l2.val :
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else :
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        print (nums)
        return newTail + 1
    
    def removeElement(self, nums, val) :
        """   
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, tailIndex = 0, len(nums) -1
        while (i < tailIndex) :
            while  nums[tailIndex] == val  :
                tailIndex -= 1
                if tailIndex <= i :
                    break
            if nums[i] == val :
                nums[i],nums[tailIndex] = nums[tailIndex], nums[i]
                tailIndex -= 1
            i +=1
            print (i,tailIndex,nums)
        if val in nums :
            return nums.index(val)
        else :
            return len(nums)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:  # found
            return nums.index(target)
        elif target < nums[0] : # less than
            return 0
        elif target > nums[-1] : # greater than
            return len(nums)
        else :
            for i in range (0,len(nums)) : #between
                if target > nums[i] and target < nums[i+1] :
                    return i+1

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1 :
            return "1"
        else :
            outStr = ''
            inStr = self.countAndSay(n-1)
            i,j = 0 , len(inStr) -1
            while i <= j :
                counter = 1

                while i < j and inStr[i] == inStr[i+1] :
                    i += 1
                    counter +=1
                outStr +=  str(counter) + inStr[i]
                i +=1
            return outStr
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2 :
            returnNode = ListNode(l1.val + l2.val)
        elif l1 is not None and l2 is None :
            returnNode = l1
        elif l2 is not None and l1 is None :
            returnNode = l2
        else :
            return None

        if returnNode.val >= 10 :
            returnNode.val -= 10
            if l1 is not None and l1.next is not None :
                l1.next.val += 1
            elif l2 is not None and l2.next is not None :
                l2.next.val += 1
            elif l1 is not None and l1.next is None :
                l1.next = ListNode(1)
            elif l2 is not None and l2.next is None :
                l2.next = ListNode(1)
                
        if  l1 is not None and l2 is not None :
            returnNode.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1 is None and l2 is not None :
            returnNode.next = self.addTwoNumbers(None,l2.next)
        elif l1 is not None and l2 is None :
            returnNode.next = self.addTwoNumbers(l1.next, None)

        return returnNode
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #print ("{0:b}".format(x))
        #print ("{0:b}".format(y))
        out = x^y
        #print ("{0:b}".format(out))
        return "{0:b}".format(out).count('1')
    
    def solveAliceBob(self, a0, a1, a2, b0, b1, b2):
    # Complete this function
        alice = 0;
        bob = 0;
        
        if a0 > b0 :
            alice += 1
        elif b0 > a0 :
            bob += 1
        
        if a1 > b1 :
            alice += 1
        elif b1 > a1 :
            bob += 1
        
        if a2 > b2 :
            alice += 1
        elif b2 > a2 :
            bob += 1
        return [alice, bob]
    
    def joinElements(self, myList = []):
    # Complete this function
        return ' '.join(str(x) for x in myList[::-1])
    
    def parse (self, G):
        returnValue = -1
        tracker = -1
        sources = G['sources']
        machines = G['machines']
        #print ("sources ", sources)
        #print ("machines ", machines)
        mr = dict()
        mm = dict()
        resources = dict();

        # break into matrixes or machine resource, machine machine
        for key, value in machines.items():
            inputMe = value['input']
            for key1, value1 in inputMe.items():
                if key1.startswith('s') :
                    if key not in mr:
                        mr[key] = dict()
                    mr[key][key1]=value1
                else :
                    if key not in mm:
                        mm[key] = dict()
                    mm[key][key1]=value1
        #print ("m_r ", mr)
        #print ("m_m ", mm)
        
        # scan through mm, and multiple out the dependencies of machines
        for m1, v1 in mm.items() :
            for m2, multi1 in v1.items() :
                if m2 in mm :
                    for m3, multi2 in mm[m2].items() :
                        mm[m2][m3] = multi2 * multi1
        #print ("m_r ", mr)
        #print ("m_m ", mm)
        
        # scan through mm, and multiple out the dependencies
        for m1, v1 in mm.items() :
            for m2, multi1 in v1.items() :
                if m2 in mr :
                    for m3, multi2 in mr[m2].items() :
                        mr[m2][m3] = multi2 * multi1
        #print ("m_r ", mr)
        #print ("m_m ", mm)
        
        # add up resources
        for m1, v1 in mr.items() :
            for m2, multi1 in v1.items() :
                if m2 not in resources :
                    resources[m2] = dict()
                    resources[m2] = 0
                resources[m2] += multi1
        
        print ("sources" + str(sources))
        print ("resources " + str(resources))
        
        for resource, multi in resources.items() :
            if resource not in sources :
                returnValue = 0
            if resource in sources and returnValue != 0 and multi != 0 :
                tracker = int(sources[resource] / multi)
                if tracker < returnValue or returnValue == -1:
                    returnValue = tracker
        
        return returnValue
            
                        

if __name__ == '__main__':
    myKai1 = { "sources" : {"s1": 90,
                          "s2": 130,
                          "s3": 110},
               "machines" : {
                   "m1":{
                        "input": {"s1":4,
                                  "s2":2
                                 },
                        "output": 1
                        },
                    "m2":{ 
                        "input": {"s3":5
                                },
                        "output": 1
                        },
                    "m3":{ 
                        "input": {
                            "m1":1,
                            "m2":2,
                            "s2":5
                                },
                        "output": 1
                        }
            }
            }
    myKai2 = { "sources" : {"s1": 90,
                          "s2": 130,
                          "s3": 110},
               "machines" : {
                   "m1":{
                        "input": {"s1":4,
                                  "s2":2
                                 },
                        "output": 1
                        },
                    "m2":{ 
                        "input": {"s3":5
                                },
                        "output": 1
                        },
                    "m3":{ 
                        "input": {
                            "m1":1,
                            "m2":2,
                            "s2":5
                                },
                        "output": 1
                        }
                             ,    
                    "m4":{ 
                        "input": {
                            "m3":2,
                                },
                        "output": 1
                        }
            }
            }
    myKai3 = { "sources" : {"s1": 90,
                          "s2": 130,
                          "s3": 110},
               "machines" : {
                   "m1":{
                        "input": {"s1":4,
                                  "s2":5
                                 },
                        "output": 1
                        },
                    "m2":{ 
                        "input": {"s3":2
                                },
                        "output": 1
                        },
                    "m3":{ 
                        "input": {
                            "m1":1,
                            "m2":2,
                            "s2":5
                                },
                        "output": 1
                        }
                             ,    
                    "m4":{ 
                        "input": {
                            "m3":2,
                                },
                        "output": 1
                        }
            }
            }
    myKai4 = { "sources" : {"s1": 90,
                          "s2": 130,
                          "s3": 110},
               "machines" : {
                   "m1":{
                        "input": {"s1":4,
                                  "s2":5
                                 },
                        "output": 1
                        },
                    "m2":{ 
                        "input": {"s3":2
                                },
                        "output": 1
                        },
                    "m3":{ 
                        "input": {
                            "m1":1,
                            "m2":2,
                            "s2":5
                                },
                        "output": 1
                        }
                             ,    
                    "m4":{ 
                        "input": {
                            "m3":2,
                            "s4": 5
                                },
                        "output": 1
                        }
            }
            }
    print (Solution.parse(Solution, myKai1))
    print (Solution.parse(Solution, myKai2))
    print (Solution.parse(Solution, myKai3))
    print (Solution.parse(Solution, myKai4))

    #print ("4 3 2 1", Solution.joinElements (Solution, [1, 2, 3, 4]))

    #print ("0 3", Solution.solveAliceBob (Solution, 1, 1, 1, 2,2,2))
    #print ("3 0", Solution.solveAliceBob (Solution, 2, 2, 2, 1,1,1))
    #print ("2 0", Solution.solveAliceBob (Solution, 2, 2, 2, 1,2,1))
    #print ("1 0", Solution.solveAliceBob (Solution, 2, 2, 2, 2,2,1))

    #print ("2", Solution.hammingDistance(Solution,1,4))
    #print ("1", Solution.countAndSay(Solution,1))
    #print ("11", Solution.countAndSay(Solution,2))
    #print ("21", Solution.countAndSay(Solution,3))
    #print ("1211", Solution.countAndSay(Solution,4))
    #print ("111221", Solution.countAndSay(Solution,5))
    #print (2, Solution.searchInsert(Solution,[1,3,5,6], 5))
    #print (1, Solution.searchInsert(Solution,[1,3,5,6], 2))
    #print (4, Solution.searchInsert(Solution,[1,3,5,6], 7))
    #print (0, Solution.searchInsert(Solution,[1,3,5,6], 0))

    # print (2, Solution.strStr(Solution,"hello", "ll"))
    # print (-1, Solution.strStr(Solution,"hello", "123"))
    
    #print (2, Solution.removeElement(Solution,[3,2,2,3], 3))
    #print (5, Solution.removeElement(Solution,[3,2,2,3,2,2,2,3], 3))
    #print (6, Solution.removeElement(Solution,[3,2,2,2,2,2,2,3], 3))
    #print (0, Solution.removeElement(Solution,[3,3,3], 3))
    #print (0, Solution.removeElement(Solution,[3], 3))
    #print (0, Solution.removeElement(Solution,[], 3))
    #print (1, Solution.removeElement(Solution,[1], 3))
    #print (1, Solution.removeElement(Solution,[4,5], 4))
    #print (1, Solution.removeElement(Solution,[4,5], 5))
    #print (1, Solution.removeElement(Solution,[2,2,3], 2))
    #print (3, Solution.removeElement(Solution,[2,2,3], 4))


    #print ('1', Solution.removeDuplicates(Solution,[1]))
    #print ('1', Solution.removeDuplicates(Solution,[1,1]))
    #print ('1', Solution.removeDuplicates(Solution,[1,1,1]))
    #print ('1', Solution.removeDuplicates(Solution,[1,1,1,1]))
    #print ('3', Solution.removeDuplicates(Solution,[1,2,3]))
    #print ('3', Solution.removeDuplicates(Solution,[1,1,2,3]))
    #print ('4', Solution.removeDuplicates(Solution,[1,1,2,2,3,3,3,3,5]))
    # print ('true', Solution.isValid(Solution,''))
    # print ('true', Solution.isValid(Solution,'()'))
    # print ('false', Solution.isValid(Solution,'[}'))
    # print ('false', Solution.isValid(Solution,'['))
    # print ('false', Solution.isValid(Solution,'}'))
    # print ('true',Solution.isValid(Solution,'([])'))
    # print ('false', Solution.isValid(Solution,'([]}'))

    # print (Solution.twoSum(Solution,[3,2,4],6))
    # print (Solution.reverse(Solution, 123))
    # print (Solution.reverse(Solution, -123))
    # print (Solution.isPalindrome(Solution, 123))
    # print (Solution.isPalindrome(Solution, -123))
    # print (Solution.isPalindrome(Solution, 121))
    # print (Solution.isPalindrome(Solution, 9876556789))      
    # print (Solution.romanToInt(Solution, 'I'))  
    # print (Solution.romanToInt(Solution, 'III'))
    # print (Solution.romanToInt(Solution, 'IV'))
    # print (Solution.romanToInt(Solution, 'V'))
    # print (Solution.romanToInt(Solution, 'VI'))
    # print (Solution.romanToInt(Solution, 'IX'))
    # print (Solution.romanToInt(Solution, 'XVII'))
    # print (Solution.romanToInt(Solution, 'XXXXIII'))
    # print (Solution.romanToInt(Solution, 'XXXXVIII'))
    # print (Solution.romanToInt(Solution, 'XXXXIX'))
    # print (Solution.romanToInt(Solution, 'XC'))
    # print (Solution.longestCommonPrefix(Solution, []))
    # print (Solution.longestCommonPrefix(Solution, ['abcd']))
    # print (Solution.longestCommonPrefix(Solution, ['abcd','bbcd']))
    # print (Solution.longestCommonPrefix(Solution, ['abcd','abcd']))    
    # print (Solution.longestCommonPrefix(Solution, ['abcd','abcd','bbcd']))    
    # print (Solution.longestCommonPrefix(Solution, ['abcd','abcd','abc']))    
    # print (Solution.longestCommonPrefix(Solution, ['abcd','abcd','abce']))    
    # print (Solution.longestCommonPrefix(Solution, ['aa','a']))    
    