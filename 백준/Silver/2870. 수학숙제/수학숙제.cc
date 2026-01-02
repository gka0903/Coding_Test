#include <bits/stdc++.h>
using namespace std;

vector<string> numbers;

bool commpare(string a, string b)
{
  if (a.length() != b.length())
  {
    return a.length() < b.length();
  }
  return a < b;
}

string processZero(string s)
{
  while (s.length() >= 2 && s[0] == '0')
  {
    s.erase(0, 1);
  }

  return s;
}

void solve()
{
  int n;
  cin >> n;

  for (int i = 0; i < n; i++)
  {
    string tmp = "";
    string s;
    cin >> s;

    for (int j = 0; j < s.length(); j++)
    {
      if (isdigit(s[j]))
      {
        tmp += s[j];
      }
      else
      {
        if (tmp != "")
        {
          numbers.push_back(processZero(tmp));
          tmp = "";
        }
      }
    }

    if (tmp != "")
    {
      numbers.push_back(processZero(tmp));
      tmp = "";
    }
  }

  sort(numbers.begin(), numbers.end(), commpare);

  for (int i = 0; i < numbers.size(); i++)
  {
    cout << numbers[i] << endl;
  }
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  solve();

  return 0;
}