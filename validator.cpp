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
        int n, m;
        cin >> n >> m;
        assert(n >= 1 and n <= 5);
        assert(m >= 1 and m <= 10);
    }
    return 0;
}