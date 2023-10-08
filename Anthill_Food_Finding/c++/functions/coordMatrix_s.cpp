#pragma once

#include "anthill.h"
//#include <vector>


class CoordMatrix {
private:
    std::vector <std::pair <int, int>> matrix_direction;
    std::vector <std::vector < int> random_numbers;
    std::vector <nsew_dict> Anthill::nsew_dict;

public:
    CoordMatrix(const MatrixDirection &matrix_direction);

//		const std::map<anthill::nsew_dict
    RandomWalk(const random_numbers &random_numbers);

    void randomNumber(int lowerBound, int upperBound, int length = 50);

    void randomWalkMethod2(int lowerBound = 1, int upperBound, int length = 50);

    void addCoord(int x, int y, const NSEW &nsew_dict);

    void printMatrix() const;

};


CoordMatrix::CoordMatrix(const MatrixDirection &matrix_direction) {
    matrix_direction.push_back(std::make_pair(0, 0));
}

CoordMatrix::RandomWalk(
        const random_numbers &random_numbers
) { // i need to create an array of random integers within a lower and upper bound
// should return (when called) an array-like list of 100 integers (enough for now, should be easily changed)
    random_numbers.push_back(std::vector < int > );
}


// need to generate random walk and then in the add coord define how the random walk is used in addCoord
vector CoordMatrix::addCoord(int x, int y, const NSEW &nsew_dict) {


/*	for <= here I add a function that: 1) takes the vector of random integers, iterates through each with a for loop
2) for each integer, finds the direction in nsew_dict, gets the vector x, y,
3) assigns the x, y values
4) push back
4.1) does sth with this new coords added,
4.2) decides whether to continue or to exit and return the count (number of rows)
4.1 and 4.2 should be anthill, and in that, the conditions are checked.
5) next iteration
*/
    matrix_direction.push_back(std::make_pair(x, y));
}

void CoordMatrix::printMatrix() const {
    for (const auto &coordinate: matrix_direction) {
        std::cout << "for random numbers ranging from " << lowerBound << " to " << upperBound << std::endl;
        std::cout << "[" << coordinate.first << ", " << coordinate.second << "]" << std::endl;
    }
}

// these are the random number generators, 2 types, where do I put them.
void CoordMatrix::randomNumber(int lowerBound, int upperBound, int length = 50) {
    std::random_device rand;
    std::mt19937 rng(rand());
    std::uniform_int_distribution <std::mt19937::result_type> dist(lowerBound, upperBound);
    random_numbers.push_back(dist(rng));

}

void CoordMatrix::randomWalkMethod2(int lowerBound = 1, int upperBound, int length = 50) {
    for (int i = 0; i < length, i++)
        random_numbers.push_back((rand() % (upperBound - lowerBound + 1)) + lowerBound));

}

// is int main still needed? anthill.cpp or anthill.h will be runner of these functions.
// todo: need to add the monte carlo over all of these later on.
int main() {
    MatrixDirection matrix_direction;
    nsew_dict Anthill::nsew_dict


    lowerBound = 1
    upperBound = 4
    randomWalkMethod2()
    random_numbers.randomWalkMethod2(lowerBound, upperBound)


    matrix_direction.addCoord()
    printMatrix()

}