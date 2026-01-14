#include <bits/stdc++.h>
using namespace std;

struct Pos
{
  int y, x, k;
};

const int INF = 1e9;

int dy[4] = {1, 0, -1, 0};
int dx[4] = {0, 1, 0, -1};

int hy[8] = {2, 2, -2, -2, 1, 1, -1, -1};
int hx[8] = {1, -1, 1, -1, 2, -2, 2, -2};

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int K;
  int W, H;

  cin >> K;
  cin >> W >> H;
  int graph[H][W];

  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      cin >> graph[i][j];
    }
  }

  int visited[H][W][K + 1];
  memset(visited, -1, sizeof(visited));

  queue<Pos> q;
  q.push({0, 0, K});
  visited[0][0][K] = 0;

  while (!q.empty())
  {
    Pos p = q.front();
    int y, x, k;
    y = p.y;
    x = p.x;
    k = p.k;
    q.pop();

    if (y == H - 1 && x == W - 1)
    {
      break;
    }

    for (int i = 0; i < 12; i++)
    {
      int ny, nx, nk = k;
      if (i <= 3)
      {
        ny = y + dy[i];
        nx = x + dx[i];
      }
      else
      {
        if (k > 0)
        {
          nk = k - 1;
          ny = y + hy[i - 4];
          nx = x + hx[i - 4];
        }
        else
        {
          break;
        }
      }

      if (0 <= ny && ny < H && 0 <= nx && nx < W)
      {
        if (graph[ny][nx] != 1)
        {
          if (visited[ny][nx][nk] == -1)
          {
            visited[ny][nx][nk] = visited[y][x][k] + 1;
            q.push({ny, nx, nk});
          }
        }
      }
    }
  }

  int result = INF;

  for (int x : visited[H - 1][W - 1])
  {
    if (x == -1)
    {
      continue;
    }

    result = min(result, x);
  }

  if (result == INF)
  {
    cout << -1 << '\n';
  }
  else
  {
    cout << result << '\n';
  }

  return 0;
}