#include <bits/stdc++.h>
using namespace std;

int main()
{
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);

  vector<queue<int>> wait_list(200001);

  int N, M;
  cin >> N >> M;

  vector<int> eat_dishes(N + 1, 0);

  for (int i = 1; i <= N; i++)
  {
    int k;
    cin >> k;
    vector<int> want_list(k);

    for (int j = 0; j < k; j++)
    {
      int want_fish;
      cin >> want_fish;
      wait_list[want_fish].push(i);
    }
  }

  for (int i = 0; i < M; i++)
  {
    int fish;
    cin >> fish;

    if (!wait_list[fish].empty())
    {
      int person = wait_list[fish].front();
      wait_list[fish].pop();
      eat_dishes[person] += 1;
    }
  }

  for (int i = 1; i <= N; i++)
  {
    cout << eat_dishes[i] << " ";
  }
  return 0;
}