#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    string line;

    ifstream infile("input.txt");

    vector<int> nums;

    if (infile.is_open())
    {
        while (getline(infile, line))
        {
            int num = stoi(line);

            nums.emplace_back(num);
        }
        infile.close();
    }

    for (int i = 0; i < nums.size() - 2; i++)
    {
        for (int j = i + 1; j < nums.size() - 1; j++)
        {
            if (nums[i] + nums[j] == 2020)
            {
                cout << nums[i] * nums[j] << endl;
                return 0;
            }
        }
    }
    return 1;
}