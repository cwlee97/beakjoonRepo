#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class RemoteControler {
private:
	std::vector<int> availableButton;
	int minTimes;
	int goal;

public:
	RemoteControler(int n) {
		goal = n;
		availableButton = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		minTimes = abs(n-100);
	}
	~RemoteControler() {
		std::vector<int>().swap(availableButton);
	}
	void disableButton(int n) {
		availableButton[n] = -1;
	}
	bool validationCheck(int n) {
		if (n == 0) {
			if (availableButton[0] == 0) return true;
			return false;
		}
		while (n) {
			if (availableButton[n % 10] == -1) return false;
			n /= 10;
		}
		return true;
	}
	void bruteForce() {
		for (int i = 0; i <= 1000000; i++) {
			if (validationCheck(i)) {
				int times = std::to_string(i).length();
				times += abs(i - goal);
				if (times < minTimes) {
					minTimes = times;
				}
			}
		}
		std::cout << minTimes;
	}
};

int main() {
	int goal;
	std::cin >> goal;

	RemoteControler cRemoteColtroler(goal);

	int disableButtonCount;
	std::cin >> disableButtonCount;
	for (int i = 0; i < disableButtonCount; i++) {
		int button;
		std::cin >> button;
		cRemoteColtroler.disableButton(button);
	}

	cRemoteColtroler.bruteForce();

	return 0;
}