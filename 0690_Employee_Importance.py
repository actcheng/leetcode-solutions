# Problem 690
# Date completed: 2019/09/24 

# 176 ms
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {emp.id: emp for emp in employees}
        if id not in dic: return
        
        def sumImportance(id):
            imp = dic[id].importance
            for sub in dic[id].subordinates:
                imp += sumImportance(sub)
            return imp
            
        return sumImportance(id)
