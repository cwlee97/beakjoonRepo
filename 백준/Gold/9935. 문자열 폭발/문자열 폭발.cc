#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <deque>

int main() {
    std::string input_str, bomb_str;

    std::cin >> input_str;
    std::cin.ignore();
    std::cin >> bomb_str;

    std::deque<char> dq;
    std::vector<int> idx_vec;

    for (int j = 0; j < input_str.size(); j++) {
        if (idx_vec.empty()) {
            if (input_str[j] == bomb_str[0]) {
                if (bomb_str.size() != 1) {
                    dq.push_back(input_str[j]);
                    idx_vec.push_back(1);
                }
            }
            else {
                dq.push_back(input_str[j]);
                idx_vec.push_back(0);
            }
        }
        else {
            if (input_str[j] == bomb_str[idx_vec.back()]) {
                idx_vec.push_back(idx_vec.back() + 1);
            }
            else if (input_str[j] == bomb_str[0]) {
                idx_vec.push_back(1);
            }
            else {
                idx_vec.push_back(0);
            }
            dq.push_back(input_str[j]);

            if (idx_vec.back() == bomb_str.size()) {
                for (int i = 0; i < bomb_str.size(); i++) {
                    idx_vec.pop_back();
                    dq.pop_back();
                }
            }
        }
    }

    if (dq.empty()) {
        std::cout << "FRULA";
    }

    while (!dq.empty()) {
        std::cout << dq.front();
        dq.pop_front();
    }

    return 0;
}
