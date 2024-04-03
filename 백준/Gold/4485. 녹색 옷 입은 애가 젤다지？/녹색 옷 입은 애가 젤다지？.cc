#include <iostream>
#include <vector>
#include <queue>
#include <climits>

class Solution {
private:
	int dx[4] = { 0, 0, 1, -1 };
	int dy[4] = { 1, -1, 0, 0 };
	int cave_size;
	std::vector<std::vector<int>> graph;
	std::vector<std::vector<int>> dist;

public:
	void set_cave_size() {
		std::cin >> cave_size;
	}
	int get_cave_size() {
		return cave_size;
	}
	void resize_graph_and_dist() {
		graph.resize(cave_size, std::vector<int>(cave_size));
		dist.resize(cave_size, std::vector<int>(cave_size, INT_MAX));
	}
	void set_graph() {
		for (int i = 0; i < cave_size; i++) {
			for (int j = 0; j < cave_size; j++) {
				std::cin >> graph[i][j];
			}
		}
	}
	int dijkstra() {
		std::priority_queue < std::pair<int, std::pair<int, int>>> priority_q;
		priority_q.push(std::make_pair(-graph[0][0], std::make_pair(0, 0)));
		dist[0][0] = graph[0][0];

		while (!priority_q.empty()) {
			int cost = -priority_q.top().first;
			int x = priority_q.top().second.first;
			int y = priority_q.top().second.second;
			priority_q.pop();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
			
				if (nx >= 0 && ny >= 0 && nx < cave_size && ny < cave_size) {
					int current_cost = cost + graph[nx][ny];
					if (dist[nx][ny] > current_cost) {
						dist[nx][ny] = current_cost;
						priority_q.push(std::make_pair(-dist[nx][ny], std::make_pair(nx, ny)));
					}
				}
			}
		}
		return dist[cave_size - 1][cave_size - 1];
	}
};

int main() {
	int case_num = 1;
	while (true) {
		Solution solution;

		solution.set_cave_size();
		if (solution.get_cave_size() == 0) { break; }

		solution.resize_graph_and_dist();
		solution.set_graph();
		std::cout << "Problem " << case_num << ": " << solution.dijkstra() << "\n";
		case_num++;
	}
	return 0;
}