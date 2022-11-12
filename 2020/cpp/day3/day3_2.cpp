#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string line;

    int step_x_arr[] = {1, 3, 5, 7, 1};
    int step_y_arr[] = {1, 1, 1, 1, 2};

    unsigned int prod = 1;

    for (int i = 0; i < 5; i++)
    {
        int step_x = step_x_arr[i];
        int step_y = step_y_arr[i];
        int trees = 0;
        int index = 0;

        ifstream infile("input.txt");
        if (infile.is_open())
        {
            int n = 0;
            while (getline(infile, line))
            {
                if (n % step_y == 0)
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
                n++;
            }
            infile.close();
            prod *= trees;
        }
    }
    cout << prod << endl;
}