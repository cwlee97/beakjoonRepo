#include <iostream>
#include <deque>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string input_str;
    std::cin >> input_str;
    std::deque<char> input_deque(input_str.begin(), input_str.end());

    int input_cases;
    std::cin >> input_cases;
    std::cin.ignore();

    std::deque<char> dq;

    for (int i = 0; i < input_cases; i++) {
        char method;
        std::cin >> method;

        switch (method) {
        case 'L':
            if (!input_deque.empty()) {
                dq.push_front(input_deque.back());
                input_deque.pop_back();
            }
            break;
        case 'P': {
            char input_char;
            std::cin >> input_char;
            input_deque.push_back(input_char);
            break;
        }
        case 'B':
            if (!input_deque.empty()) {
                input_deque.pop_back();
            }
            break;
        case 'D':
            if (!dq.empty()) {
                input_deque.push_back(dq.front());
                dq.pop_front();
            }
            break;
        }
    }

    for (auto i : input_deque) {
        std::cout << i;
    }
    for (auto i : dq) {
        std::cout << i;
    }

    return 0;
}