#pragma once
#include <map>
#include <vector>

std::map<std::string, std::vector<int, int>> direction_dict = {
	{"north", [0, 10]},
	{"south", [0, -10]},
	{"east", [10, 0]},
	{"west", [-10, 0]},
}

class Anthill {
//	private:
    public:
		std::map<std::int, std::string> nsew_dict = {

        	{1, direction_dict["north"]},
        	{2, direction_dict["south"]},
        	{3, direction_dict["east"]},
        	{4, direction_dict["west"]},
        }
        int iterations;
		int x, y;
		Point(): x(0), y(0)

        void defineDirection(const Directions& nsew_dict);
        void createMovements(const std::vector<int>& movements) {
            if
        }; // create empty frame with 2 columns (x_moves, y_moves)
        void trackCoords(const CoordsTrack& coordsMove); // track the coords of the randnum by adding to the movements frame
        void checkConditions(std::string question_num); // check if the conditions were met based on question ref
        // add sth to return the final moves counter
};