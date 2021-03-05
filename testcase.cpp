#include "./generate testcase.cpp"
const vector<string> s = {
    "ABCDEFGDHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "()"
};

void testcase()
{
    ll a = rnd(2, 3);
    ll b = rnd(2, 3);
    w(a, b);
}

void printEdges(vector<pair<ll, ll>> &e, ll v, bool is_graph)
{
    cout << v << " ";
    if(is_graph) {
        cout << e.size();
    }
    cout << endl;
    for(auto &X : e) {
        cout << X.first << " " << X.second << " ";
        // cout << rnd(1, 5);
        cout << "\n";
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t = rnd(1, 10);
    t = 1;
    // cout << t << endl;
    while(t--) {
        testcase();
    }
}