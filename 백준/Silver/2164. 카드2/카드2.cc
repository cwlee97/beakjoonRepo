#include <iostream>
#include <queue>

class Info {
private:
	int card_num;
	std::queue<int> card_list;
public:
	void get_input(void) {
		std::cin >> card_num;
	}
	void make_queue(void) {
		for (int i = 1; i <= card_num; i++) {
			card_list.push(i);
		}
	}
	int get_queue_len(void) {
		return card_list.size();
	}
	void throw_card(void) {
		card_list.pop();
	}
	void move_card(void) {
		card_list.push(card_list.front());
		card_list.pop();
	}
	int get_queue_front() {
		return card_list.front();
	}
};

int main(void) {
	Info problem_info;
	problem_info.get_input();
	problem_info.make_queue();
	while (true) {
		if (problem_info.get_queue_len() == 1) {
			std::cout << problem_info.get_queue_front();
			break;
		}
		problem_info.throw_card();
		if (problem_info.get_queue_len() == 1) {
			std::cout << problem_info.get_queue_front();
			break;
		}
		problem_info.move_card();
	}
	return 0;
}