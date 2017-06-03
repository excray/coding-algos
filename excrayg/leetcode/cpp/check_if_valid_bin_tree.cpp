// Trees/Graphs
// Given a head to a Graph where each Node only has 2 neighbors each, determine if it is a valid binary tree.
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <stdexcept>
#include <iostream>
#include <string>
using namespace std;


class Graph
{
  
  public:
    void add_node(int u);
    void add_edge(int u, int v);
    bool is_valid_binary_tree();
  private:
    unordered_map<int, vector<int>> _graph;
};

void Graph::add_node(int u)
{
    auto itr = _graph.find(u);
    if(itr != _graph.end())
    {
        throw runtime_error("Error: Node already in graph");
    }
    else
    {
        _graph[u] = {};
    }
}

void Graph::add_edge(int u, int v)
{
    auto itr1 = _graph.find(u);
    auto itr2 = _graph.find(v);
    if(itr1 == _graph.end() || itr2 == _graph.end())
    {
        throw runtime_error("Error: Node not found in graph");
    }
    else
    {
        _graph[u].emplace_back(v);
    }
}

bool Graph::is_valid_binary_tree()
{
    int root_node = 1;
    vector<int> stack;
    unordered_set<int> visited;
    stack.emplace_back(root_node);
    while(!stack.empty())
    {
        int node = stack.back();
        cout<<"Visiting node: "<<node<<endl;
        stack.pop_back();
        auto iter = visited.find(node);
        if(iter != visited.end())
        {
            cout<<"Cycle found: Invalid binary tree"<<endl;
            return false;
        }
        visited.insert(node);
        int num_children = _graph[node].size();
        if(num_children > 2)
        {
            cout<<"More than one children: Invalid binary tree"<<endl;
            return false;
        }
        else
        {
            for(auto child: _graph[node])
            {
                stack.emplace_back(child);
            }
        }
    }
    
    for(auto& kv: _graph)
    {
        auto itr = visited.find(kv.first);
        if(itr == visited.end())
        {
            auto msg = "Node " + to_string(kv.first) + " not visited, Invalid binary tree";
            cout<<msg<<endl;
            return false;
        }
    }
    return true;
}

int main()
{
    Graph graph;
    graph.add_node(1);
    graph.add_node(2);
    graph.add_node(3);

    graph.add_edge(1,2);
    graph.add_edge(1,3);
    graph.add_edge(1,4);

    if(graph.is_valid_binary_tree())
    {
        cout<<"Graph is a valid binary tree"<<endl;
    }
    else
    {
        cout<<"Graph is invalid binary tree"<<endl;
    }
    
    return 0;
}