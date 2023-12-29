#define  _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <sstream>

int main()
{
	int length;
	std::cin >> length;
	int buf = 0;
	long long result = 0;

	std::string input_str;
	std::cin >> input_str;

	const char* start = input_str.c_str();

	for (int i = 0; i < length; i++) {

		int ascii = static_cast<int>(*start);

		if (48 <= ascii && ascii <= 57) {
			if (buf < 100000)
				buf = buf * 10 + (ascii - 48);

			if (i == length - 1)
				result += buf;
		}

		else {
			result += buf;
			buf = 0;
		}

		start += 1;
	}

	std::cout << result << std::endl;
}