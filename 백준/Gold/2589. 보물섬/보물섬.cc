#include <bits/stdc++.h>
using namespace std;

int H, W;
char graph[51][51];
int visited[51][51];
vector<int> dy = {0, 1, 0, -1};
vector<int> dx = {1, 0, -1, 0};

int bfs(int y, int x)
{
  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      visited[i][j] = -1;
    }
  }

  int max_distance = 0;
  deque<pair<int, int>> q;

  visited[y][x] = 0;
  q.push_back({y, x});

  while (!q.empty())
  {
    pair<int, int> current = q.front();
    q.pop_front();
    int qy = current.first;
    int qx = current.second;

    for (int i = 0; i < 4; i++)
    {
      int ny, nx;
      ny = dy[i] + qy;
      nx = dx[i] + qx;

      if ((0 <= ny && ny < H) && (0 <= nx && nx < W))
      {
        if (graph[ny][nx] == 'L')
        {
          if (visited[ny][nx] == -1)
          {
            int dist = visited[qy][qx] + 1;
            visited[ny][nx] = dist;
            max_distance = max(max_distance, dist);
            q.push_back({ny, nx});
          }
        }
      }
    }
  }

  return max_distance;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> H >> W;

  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      char cur;
      cin >> cur;
      graph[i][j] = cur;
    }
  }

  int result = 0;
  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      if (0 < i && i < H - 1 && graph[i - 1][j] == 'L' && graph[i + 1][j] == 'L')
      {
        continue;
      }
      if (0 < j && j < W - 1 && graph[i][j - 1] == 'L' && graph[i][j + 1] == 'L')
      {
        continue;
      }
      if (graph[i][j] == 'W')
      {
        continue;
      }
      result = max(result, bfs(i, j));
    }
  }

  cout << result << endl;

  return 0;
}