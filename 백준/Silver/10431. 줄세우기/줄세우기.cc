#include <iostream>
#include <vector>

namespace Solution {
    class LineUp {
    private:
        int case_num;
        std::vector<int> students;
        int res = 0;
    public:
        void sort() {
            std::cin >> case_num;

            for (int i = 0; i < 20; i++) {
                int student;
                std::cin >> student;

                students.push_back(student);
                int idx = students.size() - 1;

                while (idx > 0) {
                    if (students[idx] < students[idx - 1]) {
                        int temp = students[idx];
                        students[idx] = students[idx - 1];
                        students[idx - 1] = temp;
                        res++;
                        idx--;
                    }
                    else { break; }
                }
            }
        }
        void print_res() {
            std::cout << case_num << " " << res << "\n";
        }
    };
}

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        Solution::LineUp line_up;
        line_up.sort();
        line_up.print_res();
    }

    return 0;
}
