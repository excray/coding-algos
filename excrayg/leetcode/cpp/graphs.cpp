

// 1->2 2->1 1->3
// 1 -> 2,3
// 2 -> 1

//Implement DFS and BFS


typedef unordered_map<int, unique_ptr<Node>> Graph;
typedef vector<unique_ptr<Node>> Edges;
struct Node
{
  int id;
  Edges edges;
};

void add_edge(unique_ptr<Node> from, unique_ptr<Node> to)
{
  from->edges.emplace_back(to);
}

int main()
{
  
}
