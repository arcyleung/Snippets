g++ -g -O2 ../cpp/2darray.cpp -o cpp-O2.out && ./cpp-O2.out
g++ -g -O3 ../cpp/2darray.cpp -o cpp-O3.out && ./cpp-O3.out

gfortran ../fortran/2darray.f90 -o ft.out && ./ft.out

objdump -S cpp-O2.out > cpp-O2.dump
objdump -S cpp-O3.out > cpp-O3.dump
objdump -S ft.out > ft.dump