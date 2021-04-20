#include <iostream>
#include <ctime>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <bitset>         // std::bitset
#include "murmur.h"
#include "bloom.h"

#define rounds 3 // Hashing rounds

std::bitset<BSL> filter;

unsigned int seed = (unsigned int)time(NULL);

void BloomFilter::insert ( char* key ) {
    for (int r = 0; r < rounds; r++) {
        int position = MurmurHash64A( (const void*)key, 64, seed + r ) % BSL;
        filter[position] = true;
    }
    printf("==> Inserted:%s \n", key);
}

bool BloomFilter::lookup ( char* key ) {
    for (int r = 0; r < rounds; r++) {
        int position = MurmurHash64A( (const void*)key, 64, seed + r ) % BSL;
        if (!filter[position]) return false;
    }
    return true;
}

void BloomFilter::reset() {
    filter.reset();
    std::cout << "Bloom filter is reset!" << std::endl;
}
