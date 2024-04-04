#include <iostream>

class Solution {
private:
	int input_num;
public:
	void get_input() {
		std::cin >> input_num;
	}

	void solution() {
		if (input_num % 2 == 0) {
			std::cout << "CY" << "\n";
		}
		else {
			std::cout << "SK" << "\n";
		}
	}
};

int main() {
	Solution solution;
	solution.get_input();
	solution.solution();
	return 0;
}