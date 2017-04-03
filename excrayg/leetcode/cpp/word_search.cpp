
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <iostream>
using namespace std;

typedef vector<vector<string>> SolVector;


vector<string> get_neigh(string node, unordered_set<string> &visited, vector<string> &dict)
{
    
    int m = node.length();
    vector<string> neighs;
    for(int i = 0; i < m; i++)
    {
        char to_replace = node[i];
        for(char j = 'a'; j <= 'z'; j++)
        {
            if(j == to_replace)
            {
                continue;
            }
            node[i] = j;
            // cout<<node<<" ";
            unordered_set<string>::iterator it = visited.find(node);
            vector<string>::iterator it1 = find(dict.begin(), dict.end(), node);
            if(it1 != dict.end() && it == visited.end())
            {
                neighs.emplace_back(node);
            }
        }
        node[i] = to_replace;
    }
    return neighs;
}

vector<string> construct_path(unordered_map<int, string> &path, int total_levels)
{
    vector<string> new_path;
    for(int i = 0; i <= total_levels; i++)
    {
        new_path.emplace_back(path[i]);
        // cout<<path[i]<<" ";
    }
    // cout<<endl;
    return new_path;
}

void bfs(string start, string end, vector<string> &dict, SolVector &all_paths)
{
    queue<pair<vector<string>, string>> q;
    unordered_set<string> visited;
    // unordered_map<int, string> path;
    
    vector<string> path;
    q.emplace(make_pair(path, start));
    visited.emplace(start);
    int min_level = 1000;

    while(!q.empty())
    {
        pair<vector<string>, string> elem = q.front();
        q.pop();
        vector<string> cur_path = elem.first;
        string node = elem.second;
        // cout<<node<<": "<<level<<endl;
        // path[level] = node;
        // cout<<node<<endl;
        if(node == end)
        {
            int level = cur_path.size();
            if(min_level > level) min_level = level;
            if(level > min_level) break;
            // vector<string> new_path = construct_path(path, level);
            cur_path.emplace_back(node);
            all_paths.emplace_back(cur_path);   
            visited = unordered_set<string>();
            // cout<<"Found"<<endl;
        }
        else
        {
            vector<string> neigh = get_neigh(node, visited, dict);
            cur_path.emplace_back(node);
            for(auto n : neigh)
            {
                // cout<<n<<" ";
                q.emplace(make_pair(cur_path, n));
                // visited.emplace(n);
            }
            // cout<<endl;
        }
    }
}

vector<vector<string> > findLadders(string start, string end, vector<string> &dict) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    
    SolVector all_ans;
    if(start == end)
    {
        vector<string> v = {start};
        all_ans.emplace_back(v);
        return all_ans;
    }
    dict.emplace_back(end);
    bfs(start, end, dict, all_ans);
    
    return all_ans;
}

int main()
{
    vector<string> v = {"baba","abba","aaba","bbbb","abaa","abab","aaab","abba","abba","abba","bbba","aaab","abaa","baba","baaa","bbaa","babb"};
    SolVector ans = findLadders("bbaa", "babb", v);
    for(auto a : ans)
    {
        for(auto p : a)
        {
            cout<<p<<" ";
        }
        cout<<endl;
    }
    return 0;
}
