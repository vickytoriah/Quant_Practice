//#include "anthill_c++.cpp"
#pragma once
#include <iostream>
#include <cmath>
#include <cstdlib>

double myFunction(double x);
double monteCarloEstimate(double lowBound, double upBound, int iterations);
// using namespace std;

int main() {
    double lowerBound, upperBound;
    int iterations;

    lowerBound = 1;
    upperBound = 5;
    iterations = 100;

    double estimate = monteCarloEstimate(lowerBound, upperBound, iterations);

    printf("Output for %.1f -> %.1f is %.2f, (%i iterations) \n",
    lowerBound, upperBound, estimate, iterations);

    return 0;

}

double myFunction(double x) {
// function to run monte carlo on, i.e., to integrate
// todo: need to make this in the header, so that it can take other functions, change return
    return pow(x, 4) * exp(-x);
}

double monteCarloEstimate(double lowBound, double upBound, int iterations) {
// function to execute Monte carlo integration on predefined function

    double totalSum = 0;
    double randNum, functionVal;

    int iter = 0;

    while (iter < iterations - 1) {
        // select a random number within the limits of integration
        randNum = lowBound + (float(rand()) / RAND_MAX) * (upBound - lowBound);

        // Sample the function's values
        functionVal = myFunction(randNum);

        // add the f(x) value to the running sum
        totalSum += functionVal;

        iter++;

    }

    double estimate = (upBound - lowBound) * totalSum / iterations;

    return estimate;

}