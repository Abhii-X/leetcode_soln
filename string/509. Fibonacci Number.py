'''

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.'''

class Solution {
public:
    int fib(int n) {
        int a=0;
        int b=1;
        int next=a+b;
        if (n==0){
            return 0;
        }
        else{
            for(int i=2;i<=n;i++){
                next=a+b;
                 a=b;
                b=next;
            }
        }
        return next;
    }
};
