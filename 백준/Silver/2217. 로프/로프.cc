#include <iostream>
#include <vector>
#include <algorithm>

class ropes {
private:
	std::vector<int> vtRopes;
	int iRopesCount;

public:
	ropes(int n) {
		vtRopes = std::vector<int>(n, 0);
		iRopesCount = n;
	}
	~ropes() {
		std::vector<int>().swap(vtRopes);
	}
	void insert(int index, int value) {
		vtRopes[index] = value;
	}
	void sort() {
		std::sort(vtRopes.begin(), vtRopes.end());
	}
	void getMaxAnswer() {
		int maxWeight = 0;
		for (auto i = 0; i < iRopesCount; i++) {
			int possibleToHold = (iRopesCount - i) * vtRopes[i];
			if (possibleToHold > maxWeight)  maxWeight = possibleToHold;
		}
		std::cout << maxWeight;
	}
};

int main() {
	int n;
	std::cin >> n;
	ropes cRopes(n);

	for (int i = 0; i < n; i++) {
		int rope;
		std::cin >> rope;
		cRopes.insert(i, rope);
	}
	cRopes.sort();
	cRopes.getMaxAnswer();

	return 0;
}