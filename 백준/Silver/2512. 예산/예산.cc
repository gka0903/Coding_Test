#include <bits/stdc++.h>
using namespace std;

bool check(int total, vector<int> &budgets_, int mid)
{
  int sum_budget = 0;
  for (int b : budgets_)
  {
    if (b < mid)
    {
      sum_budget = b + sum_budget;
    }
    else
    {
      sum_budget = mid + sum_budget;
    }
  }

  return total >= sum_budget;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, total_budget, r;

  cin >> N;

  int s = 0, e = 0;
  vector<int> budgets_(N);

  for (int i = 0; i < N; i++)
  {
    cin >> budgets_[i];

    if (budgets_[i] > e)
    {
      e = budgets_[i];
    }
  }

  cin >> total_budget;

  while (s <= e)
  {
    int m;
    m = (s + e) / 2;

    if (check(total_budget, budgets_, m))
    {
      s = m + 1;
      r = m;
    }
    else
    {
      e = m - 1;
    }
  }

  cout << r << '\n';

  return 0;
}