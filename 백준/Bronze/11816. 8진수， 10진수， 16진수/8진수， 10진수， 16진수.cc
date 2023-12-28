#include <iostream>
#include <sstream>

int main()
{
	std::string input_str;
	std::cin >> input_str;

	int result;

	std::istringstream buf(input_str);
	if (input_str.substr(0, 2) == "0x") {
		buf >> std::hex >> result;
	}
	else if (input_str[0] == '0') {
		buf >> std::oct >> result;
	}
	else {
		buf >> result;
	}

	std::cout << result << std::endl;

	return 0;
}