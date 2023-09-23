#pragma once
#include <iostream>
#include <cstdlib>
#include <map>
#include <vector>

using namespace std;

int x, y, lowBound, upBound, iterations;
float timeCount;
vector <std::pair<int, int>> matrix_direction;

std::map<std::string, std::vector<int, int>> direction_dict = {
	{"north", [0, 10]},
	{"south", [0, -10]},
	{"east", [10, 0]},
	{"west", [-10, 0]},
}

matrixInitiator(const MatrixDirection& matrix_directions) {
	matrix_directions.push_back(std::make_pair(0, 0));
}

addMovement() {

}

int main() {


	return 0;
}