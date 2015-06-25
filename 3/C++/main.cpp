/**
* @author Matias Grioni
* @date 23:49 19/3/15
* @desc Third Project Euler problem. Finds largest prime
        factor of inputted number.
*/

#include <iostream>

using namespace std;

unsigned long largestPrimeFactor(unsigned long num) {
    unsigned long largest = 1;
    unsigned long limit = num;

    unsigned long i = 1;
    while(i < limit) {
        if(num % i == 0) {
            // If the largest prime factor of some number is 1, it is prime.
            // Woops no just got lucky, that's if the largest factor overall is.
            // The number can still have composite factors other than 1.
            if(largestPrimeFactor(i) == 1) {
                largest = i;
                limit = num / largest;
            }
        }

        i++;
    }

    return largest;
}

int main() {
    unsigned long input;
    cout << "Find largest prime factor > ";
    cin >> input;

    unsigned long factor = largestPrimeFactor(input);
    cout << endl << "Answer is: " << factor;

    return 0;
}
