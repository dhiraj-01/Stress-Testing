#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define endl '\n'

mt19937 rng(std::chrono::steady_clock::now().time_since_epoch().count());
inline ll rnd(ll l = 0, ll r = 1E9)
{
    if(l > r) swap(l, r);
    return std::uniform_int_distribution<ll>(l, r)(rng);
    // return std::uniform_real_distribution<long double>(l, r)(rng);
}

void testcase()
{
    ll t = rnd(1, 10);
    cout << t << endl;
    while(t--)
    {
        ll n = rnd(1, 10);
        ll m = rnd(1, 10);
        cout << n << " " << m << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    testcase();
    return 0;
}