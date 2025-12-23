#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(NULL);
  vector<int> trees(5);
  vector<int> target = {1, 2, 3, 4, 5};

  for (int i = 0; i < 5; i++)
  {
    cin >> trees[i];
  }

  while (trees != target)
  {
    for (int i = 1; i < 5; i++)
    {
      if (trees[i - 1] > trees[i])
      {
        swap(trees[i - 1], trees[i]);

        for (int i = 0; i < 5; i++)
        {
          cout << trees[i] << " ";
        }

        cout << "\n";
      }
    }
  }

  return 0;
}