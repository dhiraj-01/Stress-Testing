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

#define FOR(i, a, b, s)     for(ll i = (a); i < (b); i += (s))
#define ROF(i, a, b, s)     for(ll i = (a); i > (b); i += (s))
#define FOR1(b)             FOR(_, 0, b, 1)
#define FOR2(i, b)          FOR(i, 0, b, 1)
#define FOR3(i, a, b)       FOR(i, a, b, 1)
#define FOR4(i, a, b, s)    FOR(i, a, b, s)
#define ROF1(i, b)          ROF(i, b, -1, -1)
#define ROF2(i, a, b)       ROF(i, a, b, -1)
#define ROF3(i, a, b, s)    ROF(i, a, b, s)
#define GETC(a, b, c, d, e, ...) e
#define FORC(...)           GETC(__VA_ARGS__, FOR4, FOR3, FOR2, FOR1)
#define ROFC(...)           GETC(__VA_ARGS__, ROF3, ROF2, ROF1)
#define loop(...)           FORC(__VA_ARGS__)(__VA_ARGS__)
#define rloop(...)          ROFC(__VA_ARGS__)(__VA_ARGS__)

// write on stdout
template <class... Args>
void w(Args ... args) {
    ((cout << args << " "), ...);
    cout << '\n';
}

// vector
void gvec(ll n = 5, ll lo = 1, ll hi = 10) {
    for(ll i = 0; i < n; i++) {
        cout << rnd(lo, hi) << " ";
    }
    cout << "\n";
}

// permutation
void gper(ll n = 5) {
    vector<ll> v(n);
    for(ll i = 0; i < n; i++) {
        v[i] = i + 1;
    }
    shuffle(v.begin(), v.end(), rng);
    for(ll x : v) {
        cout << x << " ";
    }
    cout << "\n";
}

// set
void gset(ll n = 5, ll lo = 1, ll hi = 10) {
    set<ll> s;
    while(s.size() != n) {
        s.insert(rnd(lo, hi));
    }
    vector<ll> a(s.begin(), s.end());
    shuffle(a.begin(), a.end(), rng);
    for(ll x : a) {
        cout << x << " ";
    }
    cout << "\n";
}

// string
void gstr(ll n = 5, string s = "01") {
    for(ll i = 0; i < n; i++) {
        ll id = rnd(0, s.size() - 1);
        cout << s[id];
    }
    cout << "\n";
}

void shuffle_edges(vector<pair<ll, ll>>& e, ll v)
{
    vector<ll> p(v + 1);
    for(int i = 1; i <= v; i++) {
        p[i] = i;
    }
    shuffle(e.begin(), e.end(), rng);
    shuffle(p.begin() + 1, p.end(), rng);

    for(auto &x : e) {
        if(rnd(0, 1)) { // undirected then swap
            swap(x.first, x.second);
        }
        x.first = p[x.first];
        x.second = p[x.second];
    }
}

void print_edges(vector<pair<ll, ll>>&, ll, bool is_graph = 0);

// 1 - 2 - 3 - 4 - 5
void grope_graph(ll v = 5)
{
    vector<pair<ll, ll>> edges(v - 1);
    for(int i = 1; i < v; i++) {
        edges[i - 1] = {i, i + 1};
    }
    shuffle_edges(edges, v);
    print_edges(edges, v);
}

void gstar_graph(ll v = 5)
{
    vector<pair<ll, ll>> edges(v - 1);
    for(int i = 2; i <= v; i++) {
        edges[i - 2] = {1, i};
    }
    shuffle_edges(edges, v);
    print_edges(edges, v);
}

/*
undirected graph
total edges : n * (n - 1) / 2
no self loop
*/
void gundirected_graph(ll v = 5)
{
    ll mx_edges = v * (v - 1) / 2;
    ll e = rnd(1, mx_edges);

    string s(mx_edges, '0');
    for(int i = 0; i < e; i++) {
        s[i] = '1';
    }
    shuffle(s.begin(), s.end(), rng);

    cout << v << " " << e << endl;
    ll id = 0;
    for(int i = 1; i <= v and e > 0; i++)
    {
        for(int j = i + 1; j <= v and e > 0; j++)
        {
            if(s[id] == '1')
            {
                e--;
                if(rnd(0, 1)) {
                    cout << i << " " << j << " ";
                }
                else {
                    cout << j << " " << i << " ";
                }
                cout << "\n";
            }
            id++;
        }
    }
}

/*
directed graph
total edges = n * n - n => n * (n - 1)
no self edge (i, i)
*/
void gdirected_graph(ll v = 5)
{
    ll mn_edges = v - 1;
    ll mx_edges = v * (v - 1);
    ll e = rnd(mn_edges, mx_edges);

    string s(mx_edges, '0');
    for(int i = 0; i < e; i++) {
        s[i] = '1';
    }
    shuffle(s.begin(), s.end(), rng);
    
    cout << v << " " << e << endl;
    ll id = 0;
    for(int i = 1; i <= v and e >= 0; i++)
    {
        for(int j = 1; j <= v and e >= 0; j++)        
        {
            if (i == j) continue; // no self loop
            if (s[id] == '1')
            {
                e--;
                cout << i << " " << j << " ";
                cout << "\n";
            }
            id++;
        }
    }
}

// generate tree + add random edges
void gconnected_graph(ll v = 5)
{
    ll mn_edges = v - 1;
    ll mx_edges = v * (v - 1) / 2;
    ll e = rnd(mn_edges, mx_edges);

    vector<pair<ll, ll>> edges;
    for(int i = 2; i <= v; ++i) {
        edges.emplace_back(rnd(1, i - 1), i);
    }

    for(ll rep = 0; rep < 10; rep++)
    {
        ll x = rnd(1, v);
        ll y = rnd(1, v);
        if(x > y) swap(x, y);
        if(x != y) {
            edges.emplace_back(x, y);
        }
    }
    sort(edges.begin(), edges.end());
    edges.erase(unique(edges.begin(), edges.end()), edges.end());

    shuffle_edges(edges, v);
    print_edges(edges, v);
}

void gtree(ll n = 5)
{
    vector<pair<ll, ll>> edges;
    for(int i = 2; i <= n; ++i) {
        edges.emplace_back(rnd(1, i - 1), i);
    }
    shuffle_edges(edges, n);
    print_edges(edges, n, 0);
}
