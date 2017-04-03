
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(long x) {
        // write your code here
        
        long m = 0;
        long s = 0;
        long e = x;
        
        while(s<=e)
        {
            m = s +(e-s)/2;
            cout<<m<<s<<e<<endl;
            if(m*m == x)
            {
                return m;
            }
            else if (m*m < x)
            {
                s = m+1;
            }
            else
            {
                e = m-1;
            }
        }
        
        return m;
    }
};


int main()
{

    Solution s;
    s.sqrt(999999999);

}
