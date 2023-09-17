from itertools import accumulate
def flightBooking(bookings, n):
    diff = [0] * (n+1)
    for i,j,d in bookings:
        diff[i-1] += d
        diff[j] -= d
    print(diff)
    return list(accumulate(diff[:-1]))

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(flightBooking(bookings, n))