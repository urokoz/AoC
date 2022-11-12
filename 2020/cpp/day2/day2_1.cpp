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

            int count = 0;
            for (auto &ch : str)
            {
                if (ch == c)
                {
                    count++;
                }
            }

            if (count >= n1 and count <= n2)
            {
                n_valid++;
            }
        }
        infile.close();
        cout << n_valid << endl;
    }
}