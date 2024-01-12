#include <iostream>
#include <cmath>

int main() {
	int input_cases;

	std::cin >> input_cases;

	for (int i = 0; i < input_cases; i++) {
		int x1, y1, r1;
		int x2, y2, r2;

		std::cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		float distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

		if (distance > r1 && distance > r2) {
			if (distance < r1 + r2) {
				std::cout << "2" << std::endl;
			}
			else if (distance == r1 + r2) {
				std::cout << "1" << std::endl;
			}

			else {
				std::cout << "0" << std::endl;
			}
		}

		else if (distance == 0 && r1 == r2) {
			std::cout << "-1" << std::endl;
		}
		
		else {
			if (distance + std::min(r1, r2) > std::max(r1, r2)) {
				std::cout << "2" << std::endl;
			}
			else if (distance + std::min(r1, r2) == std::max(r1, r2)) {
				std::cout << "1" << std::endl;
			}
			else {
				std::cout << "0" << std::endl;
			}
		}
	}
	
}