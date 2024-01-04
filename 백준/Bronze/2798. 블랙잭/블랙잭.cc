#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int input_cases, limit_sum;
    int res = 0;

    std::cin >> input_cases >> limit_sum;
    
    std::vector<int> input_nums(input_cases);
    for (int i = 0; i < input_cases; i++) 
        std::cin >> input_nums[i];
    
    for (int i = 0; i < input_cases-2; i++) {
        for (int j = i+1; j < input_cases-1; j++) {
            for (int k = j+1; k < input_cases; k++) {
                int add_res = input_nums[i] + input_nums[j] + input_nums[k];
                if (add_res <= limit_sum && add_res > res)
                    res = add_res;
            }
        }
    }

    std::cout << res << std::endl;

    return 0;
}