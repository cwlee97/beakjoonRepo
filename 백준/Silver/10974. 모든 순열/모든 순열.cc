#include <iostream>
#include <vector>
#include <cmath>

void solution(int input_num, std::vector<int> data, int cnt, int visited, int val) {
    if (cnt == input_num) {
        for (int i = input_num; i > 0; i--) {
            std::cout << val / (int)pow(10, i - 1) << " ";
            val %= (int)pow(10, i - 1);
        }
        std::cout << "\n";
        return;
    }

    for (int i = 0; i < input_num; ++i) {
        if (visited & (1 << i)) continue;

        solution(input_num, data, cnt + 1, visited | (1 << i), val * 10 + data[i]);
    }
}

int main() {
    int input_num;
    std::cin >> input_num;

    std::vector<int> data;
    
    for (int i = 1; i <= input_num; i++) {
        data.push_back(i);
    }

    solution(input_num, data, 0, 0, 0);

    return 0;
}
