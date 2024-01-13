#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);

	int user_cards, all_cards;
	
	std::cin >> user_cards;

	std::vector<int> bitmap;
	std::map<int, int> user_card_map;

	for (int i = 0; i < user_cards; i++) {
		int input_num;
		std::cin >> input_num;
		user_card_map.insert(std::make_pair(input_num, 1));
	}

	std::cin >> all_cards;

	std::vector<int> all_card_list;
	all_card_list.reserve(all_cards);

	for (int i = 0; i < all_cards; i++) {
		int input_num;
		std::cin >> input_num;
		all_card_list.push_back(input_num);
	}

	
	for (int i = 0; i < all_cards; i++) {
		auto item = user_card_map.find(all_card_list[i]);
		if (item != user_card_map.end()) {
			std::cout << "1 ";
		}
		else
			std::cout << "0 ";;
	}
}