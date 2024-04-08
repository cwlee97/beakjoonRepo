#include <iostream>
#include <vector>
#include <queue>
#include <utility>

struct Point {
    int x, y, dist;
};

class Solution {
private:
    int n, m;
    std::vector<std::vector<int>> map;
    std::vector<std::vector<int>> distance;

    int dx[4] = { 0, 0, -1, 1 };
    int dy[4] = { -1, 1, 0, 0 };

public:
    Solution(int n, int m) : n(n), m(m) {
        map.resize(n, std::vector<int>(m, 0));
        distance.resize(n, std::vector<int>(m, -1));
    }

    void inputMap() {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                std::cin >> map[i][j];
            }
        }
    }

    void calculateDistance() {
        std::queue<Point> q;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (map[i][j] == 2) {
                    q.push({ i, j, 0 });
                    distance[i][j] = 0;
                }
                else if (map[i][j] == 0) {
                    distance[i][j] = 0;
                }
            }
        }

        while (!q.empty()) {
            Point cur = q.front();
            q.pop();

            for (int i = 0; i < 4; ++i) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 1 && distance[nx][ny] == -1) {
                    q.push({ nx, ny, cur.dist + 1 });
                    distance[nx][ny] = cur.dist + 1;
                }
                else if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 0 && distance[nx][ny] == -1) {
                    distance[nx][ny] = 0;
                }
            }
        }
    }

    void printResult() {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                std::cout << distance[i][j] << " ";
            }
            std::cout << "\n";
        }
    }
};

int main() {
    int n, m;
    std::cin >> n >> m;

    Solution sol(n, m);
    sol.inputMap();
    sol.calculateDistance();
    sol.printResult();

    return 0;
}
