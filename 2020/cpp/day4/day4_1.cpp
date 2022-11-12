#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string line;

    ifstream infile("input.txt");

    if (infile.is_open())
    {
        while (getline(infile, line))
        {
            if (line == "") {
                
            }
        }
        infile.close();
    }
}