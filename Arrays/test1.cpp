#include<iostream>
#include<string>
#include <sstream>
using namespace std;
int countBits( int b)
{
int a=0;

    // To store the required count
    int count = 0;

    // Loop until both of them become zero
    while (a || b) {

        // Store the last bits in a
        // as well as b
        int last_bit_a = a & 1;
        int last_bit_b = b & 1;

        // If the current bit is not same
        // in both the integers
        if (last_bit_a != last_bit_b)
            count++;

        // Right shift both the integers by 1
        a = a >> 1;
        b = b >> 1;
    }

    // Return the count
    return count;
}

// Driver code
int main()
{
    std::string s;
    getline(cin,s);
    stringstream geek(s);
    int n = 0;
    geek >> n;

     int b = n;

     if(countBits(b)-3==0)
    {  cout<<1;
      return 0;
    }
    else
    cout << countBits(b)-3;

    return 0;
}
