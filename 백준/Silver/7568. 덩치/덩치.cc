#include <iostream>
#include <vector>

class Info {
private:
	int people_num;
	std::vector<std::pair<int, int>> people_list;
public:
	void get_input(void) {
		std::cin >> people_num;
		people_list.resize(people_num);

		for (int i = 0; i < people_num; i++) {
			std::pair<int, int> people_info;
			std::cin >> people_info.first >> people_info.second;

			people_list[i] = people_info;
		}
	}
	void brute_force(void) {
		for (int i = 0; i < people_num; i++) {
			int rank = 1;
			for (int j = 0; j < people_num; j++) {
				if (people_list[j].first > people_list[i].first &&
					people_list[j].second > people_list[i].second) {
					rank += 1;
				}
			}
			std::cout << rank << " ";
		}
	}
};

int main(void) {
	Info problem_info;
	problem_info.get_input();
	problem_info.brute_force();
}