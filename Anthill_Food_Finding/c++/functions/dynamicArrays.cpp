//
// Created by Victoria on 24/09/2023.
// Outline and process:
/* Create a const array pointed to by *start, this initial array, arr[2], for x, y coords (0, 0),
    another pointer variable, *moves, gets assigned the variable of *start, but not the address,
    this pointer variable is then used within the movements loops.
        1) takes the initial coords
        2) based on a random walk, decides which direction to go towards (in Cartesian coords)
        3) extend the variable pointed to by *moves with the new coords ((2x2) matrix by second move),
        4) condition check: to move to the next random walk value or to exit loop, return count, and delete *moves
        5) need to store the values at a third place (pointer maybe; the outcome of each iteration, for monte carlo)

 Starting with creating the two pointers, *start, *moves, and ensuring that the arrays are used properly.
    Potentially create *moves to be assigned to a 'new' nameless type so that it can be deleted when going out of scope
 Then, switch case for what direction to move given the random walk
 test with printf()
 then create the loop with a conditional break (loop, not program) point, ensure delete is added if new is used
 in the loop, for each move,
 */
//
#pragma once

#include <random>

using namespace std;

int arr[] = {0, 0};
typedef int*IntPtr;

int RandomWalk (int lowerBound, int upperBound, int length);

int RandomWalk (int lowerBound, int upperBound, int length = 50) {
    
    std::random_device rand;
    std::mt19937 rng (rand ());
    std::uniform_int_distribution <std::mt19937::result_type> dist (lowerBound, upperBound);
    random_numbers . push_back (dist (rng));
    return 0;
}

int main () {
    IntPtr a;
    int x, y;
    
}