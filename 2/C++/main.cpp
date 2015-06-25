/**
* @author Matias Grioni
* @date 03:22 17/3/15
* @desc Second Project Euler problem. Finds the sum of all even
*       fibonacci terms lower than some limit.
*/

#include <iostream>

using namespace std;

/**
* Sums even terms of the fibonacci sequence less than the
* parameter passed in.
*
* @param upperLimit - The inclusive bound for the fibonacci terms.
* @return - The sum of even fibonacci terms less than the param.
*/
long sumEvenFib(int upperLimit) {
    // Start the counters assuming the first iteration has been done.
    // The state of these variables would be like this is if
    // a_n = fib(n) at n = 1, and sum is the sum of all even
    // terms, e_k, such that k < n.
    int a = 1;
    int nextA = 2;
    long sum = 2;

    while(nextA < upperLimit) {
        int tmp = nextA;
        nextA += a;
        a = tmp;

        if(nextA % 2 == 0)
            sum += nextA;
    }

    return sum;
}

int main() {
    int upperLimit;
    cout << "Sum even fibonnaci terms less than > ";
    cin >> upperLimit;

    cout << "The sum is " << sumEvenFib(upperLimit);
    return 0;
}
