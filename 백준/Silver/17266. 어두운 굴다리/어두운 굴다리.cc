#include <iostream>
#include <cmath>
#include <vector>

class Lamp {
private:
	int height;

public:
	void getHeight() {
		std::cout << height;
	}
	void setHeight(const std::vector<int> input, const int tunnel_length, const int lamp_count) {
		int max_height = input[0] > tunnel_length - input[lamp_count - 1] ? input[0] : tunnel_length - input[lamp_count - 1];
		
		for (int i = 1; i < lamp_count; i++) {
			double diff = input[i] - input[i - 1];
			double half_diff = diff / 2.0;
			if (half_diff > max_height) {
				max_height = std::ceil(half_diff);
			}
		}

		height = max_height;
	}
};

int main() {
	int tunnel_length;
	std::cin >> tunnel_length;

	int lamp_count;
	std::cin >> lamp_count;

	std::vector<int> lamp_location(lamp_count);
	for (int i = 0; i < lamp_count; i++) {
		std::cin >> lamp_location[i];
	}

	Lamp lamp;
	lamp.setHeight(lamp_location, tunnel_length, lamp_count);
	lamp.getHeight();
}