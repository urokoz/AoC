#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

int main()
{
    // Open the input file for reading
    ifstream infile("day3/input.txt");

    // Initialize the total and the "new_f" flag
    int tot = 0;
    bool new_f = true;

    // Initialize the "common" set
    set<char> common;

    // Read the lines from the input file
    string line;
    int i = 1;
    while (getline(infile, line))
    {
        // If this is a new file, add all the characters from the line to the "common" set
        if (new_f)
        {
            for (char c : line)
            {
                common.insert(c);
            }
            new_f = false;
        }
        // Otherwise, only keep the characters that are in the "common" set
        else
        {
            set<char> temp;
            for (char c : line)
            {
                if (common.count(c) > 0)
                {
                    temp.insert(c);
                }
            }
            common = temp;
        }

        // If this is the third line in the file, process the "common" set
        if (i % 3 == 0)
        {
            // Get the first character in the "common" set
            char badge = *common.begin();

            // Reset the "new_f" flag and the "common" set
            new_f = true;
            common.clear();

            // Update the total based on the value of the badge character
            if (islower(badge))
            {
                tot += badge - 'a' + 1;
            }
            else
            {
                tot += badge - 'A' + 27;
            }
        }

        // Increment the line counter
        i++;
    }

    // Print the total
    cout << tot << endl;

    return 0;
}
