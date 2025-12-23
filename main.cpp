#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dx[] = {0, -1, -1, -1, 0, 1, 1, 1};
int result = 0;

struct Fish
{
  int id;
  int dir;
};

void dfs(vector<vector<Fish>> board, int sy, int sx, int sum)
{
  if (result < sum)
  {
    result = sum;
  }

  for (int k = 1; k <= 16; k++)
  {
    int fish_y = -1;
    int fish_x = -1;

    for (int i = 0; i < 4; i++)
    {
      for (int j = 0; j < 4; j++)
      {
        if (board[i][j].id == k)
        {
          fish_y = i;
          fish_x = j;
          break;
        }
      }

      if (fish_y != -1)
      {
        break;
      }
    }

    if (fish_y == -1)
    {
      continue;
    }

    int fish_dir = board[fish_y][fish_x].dir;

    for (int i = 0; i < 8; i++)
    {
      int nd = (fish_dir + i) % 8;
      int ny = fish_y + dy[nd];
      int nx = fish_x + dx[nd];

      if (ny >= 0 and ny < 4 and nx >= 0 and nx < 4)
      {
        if (board[ny][nx].id != -1)
        {
          board[fish_y][fish_x].dir = nd;
          swap(board[ny][nx], board[fish_y][fish_x]);
          break;
        }
      }
    }
  }

  int shark_dir = board[sy][sx].dir;

  for (int i = 1; i <= 3; i++)
  {
    int ny = sy + dy[shark_dir] * i;
    int nx = sx + dx[shark_dir] * i;

    if (ny >= 0 and ny < 4 and nx >= 0 and nx < 4)
    {
      if (board[ny][nx].id > 0)
      {
        vector<vector<Fish>> new_board = board;

        int new_fish = board[ny][nx].id;
        new_board[sy][sx].id = 0;
        new_board[ny][nx].id = -1;

        dfs(new_board, ny, nx, sum + new_fish);
      }
    }
  }

  return;
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  vector<vector<Fish>> board(4, vector<Fish>(4));

  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 4; j++)
    {
      int a, b;
      cin >> a >> b;
      board[i][j] = {a, b - 1};
    }
  }

  int shark_sum = board[0][0].id;
  board[0][0].id = -1;
  dfs(board, 0, 0, shark_sum);
  cout << result;

  return 0;
}