#include <bits/stdc++.h>
using namespace std;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

bool fire()
{
  int w, h;
  cin >> w >> h;
  int time;
  time = 0;
  vector<vector<char>> map_(h, vector<char>(w));
  queue<pair<int, int>> fq;
  queue<pair<int, int>> sq;

  for (int i = 0; i < h; i++)
  {
    for (int j = 0; j < w; j++)
    {
      char cur_char;
      cin >> cur_char;
      map_[i][j] = cur_char;

      if (cur_char == '@')
      {
        sq.push({i, j});
      }
      else if (cur_char == '*')
      {
        fq.push({i, j});
      }
    }
  }

  while (!sq.empty())
  {
    int size_sq, size_fq;
    size_sq = sq.size();
    size_fq = fq.size();
    time = time + 1;

    for (int i = 0; i < size_fq; i++)
    {
      pair<int, int> cur_place = fq.front();
      fq.pop();
      int fy = cur_place.first, fx = cur_place.second;

      for (int j = 0; j < 4; j++)
      {
        int nfy = dy[j] + fy, nfx = dx[j] + fx;

        if (0 <= nfy && nfy < h && 0 <= nfx && nfx < w)
        {
          if (map_[nfy][nfx] != '#' and map_[nfy][nfx] != '*')
          {
            map_[nfy][nfx] = '*';
            fq.push({nfy, nfx});
          }
        }
      }
    }

    for (int i = 0; i < size_sq; i++)
    {
      pair<int, int> cur_place = sq.front();
      sq.pop();
      int sy = cur_place.first, sx = cur_place.second;

      if (sy == 0 || sy == h - 1 || sx == 0 || sx == w - 1)
      {
        cout << time << '\n';
        return true;
      }

      for (int j = 0; j < 4; j++)
      {
        int nsy = dy[j] + sy, nsx = dx[j] + sx;

        if (0 <= nsy && nsy < h && 0 <= nsx && nsx < w)
        {
          if (map_[nsy][nsx] == '.')
          {
            map_[nsy][nsx] = '@';
            sq.push({nsy, nsx});
          }
        }
      }
    }
  }

  return false;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    if (!fire())
    {
      cout << "IMPOSSIBLE" << '\n';
    }
  }
  return 0;
}