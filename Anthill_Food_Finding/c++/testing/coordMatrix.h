#pragma once

#include "anthill.h"

class CoordMatrix {
private:
    std::vector <std::pair <int, int>> matrix_direction;
    std::vector <std::vector <int> random_numbers;
    std::vector <nsew_dict> nsew_dict;

public:
    CoordMatrix(const MatrixDirection &matrix_direction);

//		const std::map<anthill::nsew_dict
    RandomWalk(const random_numbers &random_numbers);

    void randomNumber(int lowerBound, int upperBound, int length = 50);

    void randomWalkMethod2(int lowerBound = 1, int upperBound, int length = 50);

    void addCoord(int x, int y, const NSEW &nsew_dict);

    void printMatrix() const;

};
