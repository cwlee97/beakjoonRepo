#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

struct Input {
	int fruit_count;
	int initial_length;
	std::vector<int> fruit_list;
};

namespace Solution {
	template <typename T>
	T getInput() {
		T ret;

		std::cin >> ret.fruit_count >> ret.initial_length;
		std::cin.ignore();

		ret.fruit_list.resize(ret.fruit_count);

		for (int i = 0; i < ret.fruit_count; i++) {
			int fruit_length;
			std::cin >> fruit_length;

			ret.fruit_list[i] = fruit_length;
		}

		std::sort(ret.fruit_list.begin(), ret.fruit_list.end());

		return ret;
	}

	template <typename T>
	T solution(const Input input) {
		T snakebird_length = input.initial_length;

		for (T fruit_length : input.fruit_list) {
			if (snakebird_length >= fruit_length) {
				snakebird_length += 1;
			}
			else {
				break;
			}
		}
		std::cout << snakebird_length;
		return 0;
	}
}

int main() {
	Input input = Solution::getInput<Input>();
	Solution::solution<int>(input);
}