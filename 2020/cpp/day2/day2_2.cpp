#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string line;

    ifstream infile("input.txt");

    if (infile.is_open())
    {
        int n_valid = 0;
        while (getline(infile, line))
        {
            int n1 = stoi(line.substr(0, line.find("-")));
            int n2 = stoi(line.substr(line.find("-") + 1, line.find(" ")));
            char c = line[line.find(" ") + 1];
            string str = line.substr(line.rfind(" ") + 1);

            if ((str[n1 - 1] == c) != (str[n2 - 1] == c))
            {
                n_valid++;
            }
        }
        infile.close();
        cout << n_valid << endl;
    }
}