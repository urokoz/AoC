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
            for (int k = j + 1; k < nums.size(); k++)
            {
                if (nums[i] + nums[j] + nums[k] == 2020)
                {
                    cout << nums[i] * nums[j] * nums[k] << endl;
                    return 0;
                }
            }
        }
    }
    return 1;
}