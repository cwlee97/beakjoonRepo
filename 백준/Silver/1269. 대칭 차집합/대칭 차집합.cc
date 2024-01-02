#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
	int size_a, size_b;
	std::cin >> size_a >> size_b;

    std::cin.ignore();

	std::vector<int> set_a(size_a);
	std::vector<int> set_b(size_b);

    for (int i = 0; i < size_a; ++i) {
        std::cin >> set_a[i];
    }

    std::cin.ignore();

    for (int i = 0; i < size_b; ++i) {
        std::cin >> set_b[i];
    }

    std::cin.ignore();

    std::sort(set_a.begin(), set_a.end());
    std::sort(set_b.begin(), set_b.end());

    std::vector<int> symmetric_difference;
    std::set_difference(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(), std::back_inserter(symmetric_difference));
    std::set_difference(set_b.begin(), set_b.end(), set_a.begin(), set_a.end(), std::back_inserter(symmetric_difference));

    std::cout << symmetric_difference.size() << std::endl;

    return 0;
}