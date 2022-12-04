#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

class PassportCheck {
    private:
        int validCounter = 0;
        ifstream infile;

        // byr, iyr, eyr, hgt, hcl, ecl, pid
        bool arr[7] = {false};

    
    public:
        PassportCheck(string filename) {
            infile.open(filename);
        }

        void checkLine(string line) {
            if (line.find("byr") != -1) {
                arr[0] = 1;
            }
            if (line.find("iyr") != -1)
            {
                arr[1] = 1;
            }
            if (line.find("eyr") != -1)
            {
                arr[2] = 1;
            }
            if (line.find("hgt") != -1)
            {
                arr[3] = 1;
            }
            if (line.find("hcl") != -1)
            {
                arr[4] = 1;
            }
            if (line.find("ecl") != -1)
            {
                arr[5] = 1;
            }
            if (line.find("pid") != -1)
            {
                arr[6] = 1;
            }
        }

        void resetArr() {
            for (int i = 0; i < 7; i++) {
                arr[i] = 0;
            }
        }

        void checkEntry () {
            if (all_of(begin(arr), end(arr), [](bool i){return i;})) {
                validCounter++;
            }
        }

        int checkFile () {
            for (string line; getline(infile, line);) {
                if (line == "") {
                    checkEntry();
                    resetArr();
                } else {
                    checkLine(line);
                }

            }

            return validCounter;
        }
        
};

int main()
{
    PassportCheck machine("input.txt");

    cout << machine.checkFile() << endl;
}