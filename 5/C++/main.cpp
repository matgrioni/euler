/**
* @author Matias Grioni
* @date 01:10 20/3/15
* @desc Fifth Project Euler problem. Finds smallest number
*       that is divisible by all numbers less than some
*       inputed number.
*/

#include <iostream>

using namespace std;

int gcd(int a, int b) {
    int maxNum = (a > b) ? a : b;
    int result = 1;

    for(int i = 1; i <= maxNum; i++) {
        if(a % i == 0 && b % i == 0)
            result = i;
    }

    return result;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int lcmRange(int limit) {
    if(limit == 1) {
        return 1;
    } else {
        return lcm(limit, lcmRange(limit - 1));
    }
}

int main()
{
    int limit;
    cout << "Find number divisible by all numbers less than > ";
    cin >> limit;

    cout << "Answer is: " << lcmRange(limit);

    return 0;
}
