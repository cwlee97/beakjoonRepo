#define  _CRT_SECURE_NO_WARNINGS

#include <iostream>

int main()
{
	int input_num = 0;
	std::cin >> input_num;

	if (input_num <= 1) {
		return 0;
	}

	for (int i=2; input_num!=1; i++) {
		while (input_num % i == 0) {
			input_num /= i;
			std::cout << i << std::endl;
		}
	}

	return 0;
}