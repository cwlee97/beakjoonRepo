#include <iostream>
#include <vector>

class Input {

public:
	int team1_score_list[9];
	int team2_score_list[9];
};

namespace Solution {
	template <typename T>
	T getInput() {
		T ret;

		for (int i = 0; i < 9; i++) {
			std::cin >> ret.team1_score_list[i];
		}

		std::cin.ignore();

		for (int j = 0; j < 9; j++) {
			std::cin >> ret.team2_score_list[j];
		}

		return ret;
	}

	template <typename T>
	void solution(T input) {
		int team1_score = 0;
		int team2_score = 0;
		bool reversed[2] = { false, false};

		for (int i = 0; i < 9; i++) {
			team1_score += input.team1_score_list[i];
			
			if (reversed[0] == false && team1_score > team2_score) {
				reversed[0] = true;
			}

			team2_score += input.team2_score_list[i];
			if (reversed[0] == true && team2_score > team1_score) {
				reversed[1] = true;
			}
		}

		if (reversed[0] == true && reversed[1] == true && team2_score > team1_score) {
			std::cout << "Yes";
		}
		else {
			std::cout << "No";
		}
	}
}

int main() {
	Input input = Solution::getInput<Input>();
	Solution::solution<Input>(input);
}