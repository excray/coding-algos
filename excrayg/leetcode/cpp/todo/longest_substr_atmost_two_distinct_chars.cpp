

// # Given a string S, find the length of the longest substring T that contains at most two
// # distinct characters.
// # For example,
// # Given S = “eceba”,
// # T is "ece" which its length is 3.

#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

string print_longest(string s);

int main()
{
    // string s;
    // cout << "Enter a string:\n";
    // cin >> s;
    
    cout << print_longest("eceba");
    cout << print_longest("eceebbbbbbca");
    cout << print_longest("eceba");
    cout << print_longest("eceba");
    cout << print_longest("eceba");
    cout << print_longest("eceba");
    cout << print_longest("eceba");
}

string print_longest(string s)
{
    int max_len = 0;
    int max_start = 0, max_end = 0;
    
    int start_idx = 0;
    
    while(start_idx < s.length())
    {
        unordered_set<char> unique_chars;
        int tail = start_idx;
        while(unique_chars.size() <= 2 && tail < s.length())
        {
            char c = s[tail];
            unique_chars.emplace(c);
            tail++;
        }
        int cur_len = tail-start_idx-1;
        if(cur_len > max_len)
        {
            max_len = cur_len;
            max_start = start_idx;
        }
        start_idx++;
    }
    
    string longest_str = s.substr(max_start, max_len) + "\n";
    return longest_str;
}