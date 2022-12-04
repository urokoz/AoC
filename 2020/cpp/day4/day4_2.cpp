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
            line += " ";
            size_t byr_idx = line.find("byr");
            if (byr_idx != -1)
            {
                size_t space_idx = line.find(' ', byr_idx + 4);
                int byr = stoi(line.substr(byr_idx + 4, space_idx - byr_idx - 4));

                if (byr >= 1920 & byr <= 2002) {
                    arr[0] = 1;
                }
            }
            size_t iyr_idx = line.find("iyr");
            if (iyr_idx != -1)
            {
                size_t space_idx = line.find(' ', iyr_idx + 4);
                int iyr = stoi(line.substr(iyr_idx + 4, space_idx - iyr_idx - 4));

                if (iyr >= 2010 & iyr <= 2020)
                {
                    arr[0] = 1;
                }
            }
            size_t eyr_idx = line.find("eyr");
            if (eyr_idx != -1)
            {
                size_t space_idx = line.find(' ', eyr_idx + 4);
                int eyr = stoi(line.substr(eyr_idx + 4, space_idx - eyr_idx - 4));

                if (eyr >= 2020 & eyr <= 2030)
                {
                    arr[0] = 1;
                }
            }
            size_t hgt_idx = line.find("hgt");
            if (hgt_idx != -1)
            {
                size_t space_idx = line.find(' ', hgt_idx + 4);
                string hgt = line.substr(hgt_idx + 4, space_idx - hgt_idx - 4);

                if (hgt.find("in") != -1)
                {
                    
                    arr[0] = 1;
                }
            }
            size_t byr_idx = line.find("byr");
            if (byr_idx != -1)
            {
                size_t space_idx = line.find(' ', byr_idx + 4);
                int byr = stoi(line.substr(byr_idx + 4, space_idx - byr_idx - 4));

                if (byr >= 1920 & byr <= 2002)
                {
                    arr[0] = 1;
                }
            }
            // int iyr_idx = line.find("iyr");
            // if (iyr_idx != -1)
            // {
            //     int iyr = stoi(line.substr(iyr_idx, line.find(" ", iyr_idx)));
            //     arr[0] = 1;
            // }
            // int eyr_idx = line.find("eyr");
            // if (eyr_idx != -1)
            // {
            //     int eyr = stoi(line.substr(eyr_idx, line.find(" ", eyr_idx)));
            //     arr[0] = 1;
            // }
            // int hgt_idx = line.find("hgt");
            // if (hgt_idx != -1)
            // {
            //     int hgt = stoi(line.substr(hgt_idx, line.find(" ", hgt_idx)));
            //     arr[0] = 1;
            // }
            // int hcl_idx = line.find("hcl");
            // if (hcl_idx != -1)
            // {
            //     int hcl = stoi(line.substr(hcl_idx, line.find(" ", hcl_idx)));
            //     arr[0] = 1;
            // }
            // int pid_idx = line.find("pid");
            // if (pid_idx != -1)
            // {
            //     int pid = stoi(line.substr(pid_idx, line.find(" ", pid_idx)));
            //     arr[0] = 1;
            // }
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