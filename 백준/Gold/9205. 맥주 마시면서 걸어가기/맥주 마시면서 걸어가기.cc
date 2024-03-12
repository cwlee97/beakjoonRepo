#include <iostream>
#include <algorithm>
#include <vector>

struct point {
	int x, y;
};

struct input {
	point house;
	std::vector<point> convs;
	int conv_count;
	point fest;
};

namespace Solution {
	template <typename PREC>
	input getInput() {
		input ret;
		std::cin >> ret.conv_count;
		
		std::cin >> ret.house.x >> ret.house.y;

		std::vector<PREC> input_convs(ret.conv_count);
		for (int i = 0; i < ret.conv_count; i++) {
			std::cin >> input_convs[i].x >> input_convs[i].y;
		}
		ret.convs = input_convs;

		std::cin >> ret.fest.x >> ret.fest.y;

		return ret;
	}

	template <typename PREC>
	int calcDistance(PREC p1, PREC p2) {
		return std::abs(p1.x - p2.x) + std::abs(p1.y - p2.y);
	}

	template <typename PREC>
	bool solution(const input input) {
		std::vector<bool> visited(input.conv_count, false);

		std::vector<point> queue;
		queue.push_back(input.house);

		while (!queue.empty()) {
			point current = queue[0];
			queue.erase(queue.begin());

			if (calcDistance<point>(current, input.fest) <= 1000) return true;

			for (int i = 0; i < input.conv_count; i++) {
				if (!visited[i] && calcDistance<point>(current, input.convs[i]) <= 1000) {
					queue.push_back(input.convs[i]);
					visited[i] = true;
				}
			}
		}
		return false;
	}
}


int main() {
	int cases;
	std::cin >> cases;

	for (int i = 0; i < cases; i++) {
		input input = Solution::getInput<point>();
		bool res = Solution::solution<point>(input);
		std::cout << (res ? "happy" : "sad") << "\n";
	}
}