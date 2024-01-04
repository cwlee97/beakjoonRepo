#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string input_str;
    std::cin >> input_str;

    int input_num = stoi(input_str);
    int res = 1;

    while (res <= input_num) {
        int sum = res;
        int add_num = res;
        while (add_num > 0) {
            sum += add_num % 10;
            add_num /= 10;
        }


        if (sum == input_num) {
            std::cout << res << std::endl;
            return 0;
        }
        else
            res += 1;
    }
    std::cout << 0 << std::endl;
    return 0;
}