#include <cstddef>
#include <iostream>

using namespace std;


size_t max(int a, int b)
{
    return a>b?a:b;
}

size_t abs1(int x)
{
    if(x < 0)
    {
        return -1*x;
    }
    
    return x;
}

class Solution {
public:

    size_t get_num_repeating_sets(const string& s)
    {
        size_t n = s.length();
        char prev = NULL, curr = NULL;
        size_t i = 0;
        size_t num_repeat = 0, num_succ = 0;
        while(i < n)
        {
            curr = s[i];
            if(prev == NULL)
            {
                prev = curr;
                num_succ += 1;
            }
            else
            {
                if(prev == curr)
                {
                    num_succ += 1;
                    if(num_succ == 3)
                    {
                        num_repeat += 1;
                        prev = NULL;
                        num_succ = 0;
                    }
                }
                else
                {
                    prev = curr;
                    num_succ = 1;
                }
            }
            i+=1;
        }
        
        return num_repeat;
    }
    
    size_t get_num_unmet_conditions(const string& s)
    {
        size_t i = 0;
        size_t n = s.length();
        
        size_t l = 0, u = 0, d = 0;
        
        while(i < n)
        {
            char c = s[i];
            if(c >= 'a' && c <= 'z')
            {
                if(l == 0) l += 1;
            }
            else if(c >= 'A' && c <= 'Z')
            {
                if(u == 0) u += 1;
            }
            else if(c >= '0' && c <= '9')
            {
                if(d == 0) d += 1;
            }
            i+=1;
        }
        
        return max(0, 3-(l+u+d));
    }
    
    int strongPasswordChecker(string s) {
        
        size_t min_len = 6;
        size_t max_len = 20;
        
        size_t len = s.length();
        
        if(len < 6)
        {
            size_t chars_to_add_or_remove = min_len - len;
            size_t num_repeating_sets = get_num_repeating_sets(s);
            size_t num_unmet_conditions = get_num_unmet_conditions(s);
            // cout<<chars_to_add_or_remove<<" "<<num_repeating_sets<<" "<<num_unmet_conditions<<endl;
            return max(max(num_repeating_sets, num_unmet_conditions), chars_to_add_or_remove);
        }
        else if(len > 20)
        {
            size_t chars_to_add_or_remove = len - max_len;
            size_t num_repeating_sets = get_num_repeating_sets(s);
            size_t num_unmet_conditions = get_num_unmet_conditions(s);
            return max(max(num_repeating_sets, num_unmet_conditions), chars_to_add_or_remove);
        }
        else
        {
            size_t num_repeating_sets = get_num_repeating_sets(s);
            size_t num_unmet_conditions = get_num_unmet_conditions(s);
            cout<<" "<<num_repeating_sets<<" "<<num_unmet_conditions<<endl;
            return max(num_repeating_sets, num_unmet_conditions);
        }
    }
};

int main()
{

    cout<<Solution().strongPasswordChecker("aaAA11");
    return 0;
}