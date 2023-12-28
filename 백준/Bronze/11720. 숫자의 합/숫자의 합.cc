#define  _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>

int main()
{
	int cases = 0;
	int sum = 0;
	
	std::cin >> cases;

	char input_str[101];

	std::cin >> input_str;

	for (int i = 0; i < cases; i++) {
		char num[2];
		strncpy(num, input_str + i, 1);
		num[1] = '\0';
		sum += atoi(num);
	}
	std::cout << sum << std::endl;

	return 0;
}