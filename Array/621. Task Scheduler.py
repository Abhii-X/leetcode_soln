'''

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order,
but there's a constraint: there has to be a gap of at least n intervals between two tasks with the
same label.
Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. 
The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. 
By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.'''


Link:https://leetcode.com/problems/task-scheduler/description/

#Code:

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        f={}
        for i in tasks:
            f[i]=f.get(i,0)+1
        print(f)
        maxi=max(f.values())
        print(maxi)
        count=0
        for x in f.values():
            if x==maxi:
                count+=1
        a=(maxi-1)*(n+1)+count
        return max(len(tasks),a)
