#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

struct Input {
	int cases;
	std::vector<long long int> buildings;
};

namespace Solution {
	template <typename T>
	T getInput() {
		T ret;

		std::string cases;

		std::cin >> cases;
		ret.cases = std::stoi(cases);

		std::cin.ignore();

		std::string input_buildings;
		std::getline(std::cin, input_buildings);
		
		std::istringstream iss(input_buildings);

		std::string token;

		while (iss >> token) {
			ret.buildings.push_back(std::stol(token));
		}

		return ret;
	}

	template <typename T>
	int solution(const Input input) {
		std::vector<T> visible(input.cases, 0);

		for (auto i = 0; i < input.cases-1; i++) {
			double higher_gradient = -9999999999;
			for (auto j = i + 1; j < input.cases; j++) {
				double current_gradient = (double)(input.buildings[j] - input.buildings[i]) / (j - i);
				if (current_gradient > higher_gradient) {
					visible[i]++;
					visible[j]++;
					higher_gradient = current_gradient;
				}
			}
		}

		int res = *std::max_element(visible.begin(), visible.end());
		std::cout << res << "\n";

		return 0;
	}
}


int main() {
	Input input = Solution::getInput<Input>();
	Solution::solution<int>(input);
}