#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int tc = 1;
    cin >> tc;
    assert(1 <= tc and tc <= 10);

    for(int i = 0; i < tc; i++)
    {
        int x, y;
        cin >> x >> y;
        assert(x >= 1 and x <= 10);
        assert(y >= 1 and y <= 10);
    }
    return 0;
}