// #13.13 Write a function that takes as input a string s and a list L of equal length strings and returns all substrings of S which are contactenation of all the strings in L. Each string in L must appear exactly once and the ordering is immaterial.


/**
 * You are given a string, S, and a list of words, L, that are all of the same length. 
 * Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
 * For example, given:
 * S: "barfoothefoobarman"
 * L: ["foo", "bar"]
 * You should return the indices: [0,9].
 * (order does not matter).
 */
 
 
 #include <iostream>
 #include <string>
 #include <vector>
 #include <unordered_map>
 using namespace std;
 
 int search_from_idx(const string s, const int len, int curr_idx, int num_of_words_found, unordered_map<string, int>& map_of_words)
 {
     cout << "String: " << s << " Curr Idx: " << curr_idx << " Length: " << len << endl;
     if(num_of_words_found == map_of_words.size())
     {
         return curr_idx;
     }
     if(curr_idx+len > s.length())
     {
         return -1;
     }
     string cand = s.substr(curr_idx, len);
     cout<<" Candidate: " << cand << endl;
     auto it = map_of_words.find(cand);
     if(it == map_of_words.end())
     {
         return -1;
     }
     else
     {
         int num_count = it->second;
         if(num_count == 0)
         {
             num_of_words_found+=1;
             it->second = 1;
         }
         else
         {
             return -1;
         }
     }
     return search_from_idx(s, len, curr_idx+len, num_of_words_found, map_of_words);
 }
 
 vector<string> get_substrings(const string s, const vector<string>& list_of_words)
 {
     vector<string> candidates;
     int num_chars = s.length();
     int len = list_of_words[0].length();
     int num_words = list_of_words.size();
     
     for(int start_idx = 0; start_idx < num_chars-len; start_idx++)
     {
         unordered_map<string, int> map_of_words;
         for(const auto& word: list_of_words)
         {
             map_of_words[word] = 0;
         }
        //  string cand = s.substring(start_idx, start_idx + len);
         int num_words_found = 0;
         int end_idx = search_from_idx(s, len, start_idx, num_words_found, map_of_words);
         if(end_idx != -1)
         {
             candidates.emplace_back(s.substr(start_idx, end_idx-start_idx));
         }
     }
     
     return candidates;
 }
 
 
 int main()
 {
     // while(1)
     // {
     //     string s;
     //     int n;
     //     vector<string> list_of_words;
     //     cout << "Enter a string: ";
     //     getline(cin, s);
     //     if(s.empty())
     //     {
     //         cout << "Exiting\n";
     //         break;
     //     }
     //     cout << "\nEnter number of words in list: ";
     //     cin >>  n;
     //     for(int i = 0; i < n; i++)
     //     {
     //         string l;
     //         cin >> l;
     //         list_of_words.emplace_back(l);
     //     }
     //     vector<string> candidates = get_substrings(s, list_of_words);
     //     cout << "\nPrinting all candidates: ";
     //     for(const auto& cand : candidates)
     //     {
     //         cout << cand << endl;
     //     }
     // }
     
        string s = "foobbarthebarfoo";
        vector<string> list_of_words = {"foo", "bar"};
        
        vector<string> candidates = get_substrings(s, list_of_words);
        cout << "\nPrinting all candidates: ";
        for(const auto& cand : candidates)
        {
            cout << cand << endl;
        }
 }