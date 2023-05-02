program twodee

    integer :: N = 16000
    integer :: row, col
    integer :: beginning, end, rate

    integer, allocatable :: A(:,:)

    allocate(A(N,N))

    do row = 1, N
        do col = 1, N
            call random_number(u)
            A(row, col) = u * 2E32
        end do
    end do

    call system_clock(beginning, rate)
    do row = 1, N
        do col = 1, N
            A(row, col) = A(row, col) * 5
        end do
    end do
    call system_clock(end)
    print *, "Row Maj took: ", real(end - beginning) / real(rate)

    call system_clock(beginning, rate)
    do col = 1, N
        do row = 1, N
            A(row, col) = A(row, col) * 5
        end do
    end do
    call system_clock(end)
    print *, "Col Maj took: ", real(end - beginning) / real(rate)
end program twodee