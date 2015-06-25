/**
* @author Matias Grioni
* @date 00:30 20/3/15
* @desc Fourth Project Euler problem. Finds largest palindrome
*       of two 3 digit numbers.
*/

#include <iostream>
#include <math.h>

using namespace std;

int power(int num, int exp) {
    int result = 1;

    for(int i = 0; i < exp; i++) {
        result *= num;
    }

    return result;
}

int reverseNum(int num) {
    if(num < 10)
        return num;
    else {
        int magnitude = (int) log10(num);

        int rem = num % 10;
        num /= 10;

        return rem * power(10, magnitude) + reverseNum(num);
    }
}

int main()
{
    int largest = 1;

    for(int i = 10; i < 1000; i++) {
        for(int j = i; j < 1000; j++) {
            int product = j * i;
            if(product == reverseNum(product)) {
                if(product > largest)
                    largest = product;
            }
        }
    }

    cout << "Answer is: " << largest;
}
