#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  // 초기화
  int N;
  cin >> N;
  deque<pair<string, int>> q;

  for (int i = 0; i < N; i++)
  {
    string name;
    int number;
    cin >> name >> number;
    q.push_back({name, number});
  }

  // 팀결성 루프
  while (q.size() > 1)
  {
    pair<string, int> current = q.front();
    q.pop_front();
    string name = current.first;
    int number = (current.second - 1) % q.size();

    for (int i = 0; i < number; i++)
    {
      pair<string, int> pass = q.front();
      q.pop_front();
      q.push_back(pass);
    }

    q.pop_front();
  }

  // 결과 출력
  cout << q[0].first;

  return 0;
}