#include <algorithm>
#include <iostream>
#include <vector>
#include <chrono>
#include <random>

auto start = std::chrono::high_resolution_clock::now();
auto end = std::chrono::high_resolution_clock::now();

const int N = 16000;
int M1[N][N];
int M2[N][N];

int main()
{
    // Let M be some matrix of NxN, fill it with random values
    for (auto i = 0; i < N; i++)
    {
        for (auto j = 0; i < N; i++)
        {
            int rv = rand();
            M1[i][j] = rv;
            M2[i][j] = rv;
        }
    }

    // We wish to perform elementwise operation ie multiply each element by 5, check if iterating row or col major is faster

    // Row Major
    start = std::chrono::high_resolution_clock::now();
    for (auto row = 0; row < N; row++)
    {
        for (auto col = 0; col < N; col++)
        {
            M1[row][col] *= 5;
        }
    }
    end = std::chrono::high_resolution_clock::now();
    
    std::cout << "Row Maj took: " << (end - start).count() << " ns" << std::endl;

    // Col Major
    start = std::chrono::high_resolution_clock::now();
    for (auto col = 0; col < N; col++)
    {
        for (auto row = 0; row < N; row++)
        {
            M1[row][col] *= 5;
        }
    }
    end = std::chrono::high_resolution_clock::now();
    
    std::cout << "Col Maj took: " << (end - start).count() << " ns" << std::endl;
}