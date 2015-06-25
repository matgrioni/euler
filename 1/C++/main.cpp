/**
* @author Matias Grioni
* @date 03:16 17/3/15
* @desc First Project Euler problem. Finds the sum of all the
*       multiples of 3 and 5 below some inputtted upper bound.
*/

#include <iostream>

using namespace std;

/**
* Finds and sums all the multiples of 3 and 5 less than sum
* arbitrary number.
*
* @param limit - The upper limit for finding the sum
* @return - The sum of multiples of 3 and 5 less than the param.
*/
long sumMultiples(int limit) {
    long sum = 0;
    for(int i = 0; i < limit; i++) {
        if(i % 3 == 0 || i % 5 == 0)
            sum += i;
    }

    return sum;
}

int main() {
    int upperLimit;
    cout << "Sum multiples of 3 and 5 less than > ";
    cin >> upperLimit;

    long sum = sumMultiples(upperLimit);
    cout << endl << "The sum is " << sum;
}
