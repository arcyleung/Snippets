#ifndef BLOOMFILTER_H
#define BLOOMFILTER_H

#include <iostream>
#include <bitset>         // std::bitset

#define BSL 8 // Bitset length; bigger = less false positives

class BloomFilter
{

private:
    std::bitset<BSL> filter;

public:
    BloomFilter () {
        
    };
    void insert( char* key );
    bool lookup( char* key );
    void reset();
};

#endif