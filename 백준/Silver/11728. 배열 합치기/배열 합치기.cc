#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
	std::ios::sync_with_stdio(false); std::cin.tie(NULL); std::cout.tie(NULL);

	int size_a = 0, size_b = 0;
	std::cin >> size_a >> size_b;
	std::cin.ignore();

	std::vector<int> arr_a(size_a), arr_b(size_b);

	for (int i = 0; i < size_a; i++) {
		std::cin >> arr_a[i];
	}
	std::cin.ignore();
	
	for (int j = 0; j < size_b; j++) {
		std::cin >> arr_b[j];
	}
	std::cin.ignore();

	int idx_a = 0, idx_b = 0;

	while (idx_a < size_a && idx_b < size_b) {
		if (arr_a[idx_a] <= arr_b[idx_b]) {
			std::cout << arr_a[idx_a];
			idx_a++;
		}
		else if (arr_a[idx_a] > arr_b[idx_b]) {
			std::cout << arr_b[idx_b];
			idx_b++;
		}
		if (idx_a < size_a || idx_b < size_b) {
			std::cout << " ";
		}
	}
	
	if (idx_a != size_a) {
		for (size_t i = idx_a; i < size_a; ++i) {
			std::cout << arr_a[i];
			if (i < size_a - 1) {
				std::cout << " ";
			}
		}
	}
	else if (idx_b != size_b) {
		for (size_t i = idx_b; i < size_b; ++i) {
			std::cout << arr_b[i];
			if (i < size_b - 1) {
				std::cout << " ";
			}
		}
	}
}