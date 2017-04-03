#include <vector>
#include <iostream>
using namespace std;


template<typename T>
std::ostream& operator<<(std::ostream& s, const std::vector<T>& v) {
    s.put('[');
    char comma[3] = {'\0', ' ', '\0'};
    for (const auto& e : v) {
        s << comma << e;
        comma[0] = ',';
    }
    return s << ']';
}

int main()
{
    vector<int> hello(20,0);
    hello.resize(25);
    for(int i = 0; i < 20; i++)
    {
        hello[i] = 1;
    }

    cout<<hello<<endl;
    return 0;
}

