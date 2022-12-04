#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string line;

    ifstream infile("input.txt");

    if (infile.is_open())
    {
        int step_x = 3;

        int trees = 0;
        int index = 0;
        while (getline(infile&, line))
        {
            if (line[index] == '#')
            {
                trees++;
            }
            index += step_x;
            if (index >= line.size())
            {
                index -= line.size();
            }
        }
        infile.close();
        cout << trees << endl;
    }
}