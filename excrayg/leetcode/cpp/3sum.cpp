
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:    
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    vector<vector<int> > threeSum(vector<int> &nums) {
        // write your code here
        std::sort(nums.begin(), nums.end());
        vector<vector<int> > res;
        int n = nums.size();
        for(int i = 0; i < n-2; i++)
        {
            int j = i+1;
            int k = n-1;
            while(j<k)
            {
                
                vector<int> p;
                int s = nums[i] + nums[j] + nums[k];
                if(s==0)
                {
                    p.push_back(nums[i]);
                    p.push_back(nums[j]);
                    p.push_back(nums[k]);
                    std::sort(p.begin(), p.end());
                    res.push_back(p);
                }
                else if(s > 0)
                {
                    k--;
                }
                else
                {
                    j++;
                }
            }
        }
        
        return res;
    }
};

int main()
{
  Solution s;
  vector<int> a;
  a.push_back(-1);
  a.push_back(1);
  a.push_back(0);

  s.threeSum(a);
}
