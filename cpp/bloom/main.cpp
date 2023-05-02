#include <iostream>
#include <string>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <bitset>         // std::bitset
#include "murmur.h"
#include "bloom.h"

#define DELIM " " // Input delimiter

int main(int argc, char **argv)
{
    // printf("Num args = %d, args: %d \n", argc, atoi(argv[1]));
    // int filterSize = argc > 1 ? atoi(argv[1]) : 4096;
    // printf("Filter size: %d \n", filterSize);

    // Initialize a bit array of filer size
    BloomFilter bf = BloomFilter();

    // wait for commands from stdin
    // insert <key>
    // lookup <key>
    std::string line;
    while (std::getline(std::cin, line))
    {
        int wsIdx = line.find(" ");
        int lineSize = line.size();
        std::string cmd = line.substr(0, wsIdx > 0 ? wsIdx : lineSize);
        std::string operand; 
        if (wsIdx != line.size() && wsIdx != -1) {
            operand = line.substr(wsIdx, lineSize);
        }
        if (cmd == "insert") {
            bf.insert((char*)operand.c_str());
        }
        if (cmd == "lookup") {
            if (bf.lookup((char*)operand.c_str())) {
                printf("==> Maybe \n");
            } else {
                printf("==> Nope \n");
            }
        }
        if (cmd == "reset") {
            bf.reset();
        }
        if (cmd == "exit") {
            exit(0);
        }
    }
}