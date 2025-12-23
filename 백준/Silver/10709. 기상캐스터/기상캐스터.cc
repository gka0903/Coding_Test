#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  ll H;
  ll W;
  cin >> H >> W;
  vector<vector<ll>> JOI(H, vector<ll>(W, -1));

  for (int i = 0; i < H; i++)
  {
    ll cloud = -1;

    for (int j = 0; j < W; j++)
    {
      char s;
      cin >> s;

      if (s == 'c')
      {
        cloud = 0;
      }
      else if (cloud != -1)
      {
        cloud++;
      }

      JOI[i][j] = cloud;
    }
  }

  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      cout << JOI[i][j] << " ";
    }
    cout << "\n";
  }
}
