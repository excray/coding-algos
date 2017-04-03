
#include<iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
      // write your code here
      cout<<"remove";
      int e = A.size()-1;
      if(e==0)
      {
        return e;
      }
      int nl = 0;
      vector<int>::iterator b = A.begin();
      cout<<"how"<<endl;
      while(b != b+e)
      {
        cout<<"what"<<endl;
        if(*b == elem)
        {
          int t = *b;
          *b = A[e];
          A[e--] = t;
          nl+=1;
        }
        b++;
      }

      return nl;
    }
};


int main()
{
  cout<<"Wait";
  Solution s;
  vector<int> A;
  cout<<"Call";
  s.removeElement(A, 0);    
  return 0;
}
