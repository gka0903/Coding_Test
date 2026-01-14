#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M, K, X;

  cin >> N >> M >> K >> X;
  vector<vector<int>> graph(N + 1);
  vector<int> dist(N + 1, -1);

  for (int i = 0; i < M; i++)
  {
    int from, to;
    cin >> from >> to;
    graph[from].push_back(to);
  }

  deque<int> q;
  dist[X] = 0;
  q.push_back(X);

  while (!q.empty())
  {
    int cur_graph = q.front();
    q.pop_front();

    for (int next : graph[cur_graph])
    {
      if (dist[next] == -1)
      {
        dist[next] = dist[cur_graph] + 1;
        q.push_back(next);
      }
    }
  }

  bool check = false;

  for (int i = 1; i <= N; i++)
  {
    if (dist[i] == K)
    {
      check = true;
      cout << i << endl;
    }
  }

  if (!check)
  {
    cout << -1 << endl;
  }

  return 0;
}