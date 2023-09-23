//#include "anthill_c++.cpp"

#include <iostream>
#include <cmath>
#include <cstdlib>

double myFunction(double x);
void monteCarloEstimateStDev(double lowBound, double upBound, int iterations, double mcStats[]);
// using namespace std;

int main() {
    double lowerBound, upperBound;
    int iterations;

    lowerBound = 1;
    upperBound = 5;

    double mcStats[2]; // position 0 holds the estimate, position 1 holds the STD

    for(int i = 1; i < 6; i++) {
        iterations = 2 * pow(4, i);
        monteCarloEstimateStDev(lowerBound, upperBound, iterations, mcStats);

        printf("Output for %.1f -> %.1f is %.3f, StDev = %.4f, (%i iterations) \n",
        lowerBound, upperBound, mcStats[0], mcStats[1], iterations);

    }
    return 0;
}

//    double estimate = monteCarloEstimate(lowerBound, upperBound, iterations);

double myFunction(double x) {
// function to run monte carlo on, i.e., to integrate
// todo: need to make this in the header, so that it can take other functions, change return
    return pow(x, 4) * exp(-x);
}

void monteCarloEstimate(double lowBound, double upBound, int iterations, double statsArray []) {
// function to execute Monte carlo integration on predefined function

    double totalSum = 0;
    double totalSumSquared = 0;
//    double randNum, functionVal;

    int iter = 0;

    while (iter < iterations - 1) {
        // select a random number within the limits of integration
        double randNum = lowBound + (float(rand()) / RAND_MAX) * (upBound - lowBound);

        // Sample the function's values
        double functionVal = myFunction(randNum);

        // add the f(x) value to the running sum
        totalSum += functionVal;
        totalSumSquared += pow(functionVal, 2);

        iter++;

    }

    double estimate = (upBound - lowBound) * totalSum / iterations;
	double expected = totalSum / iterations;

	double expectedSquare = totalSumSquared / iterations;

	double stddev = (upBound - lowBound) * pow ((expectedSquare - pow(expected, 2)) / (iterations - 1), 0.5);

    statsArray[0] = estimate;
    statsArray[1] = stddev;

}