// Write a C++ Program to find prime number 1 to 100
#include <iostream>
using namespace std;

int main() {
    int n = 100;

    for (int i = 1; i <= n; i++) {
        int count = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                count++;
            }
        }
        if (count == 2) {
            cout << i << " ";
        }
    }

    return 0;
}

// --------------------------------------------------------------------------------------------------------------------------------
// Tower of Hanoi Solution using recursive function
#include <iostream>
using namespace std;

void TOH(int n,char BEG, char AUX, char END){
    if(n>0){
        TOH(n-1,BEG, END, AUX);
        cout<<"Move disk "<<n<<" from rod :"<<BEG<<" to rod:"<<END<<endl;
        TOH(n-1,AUX, BEG, END);
    }
}

int main()
{
    TOH(3,'A','B','C');
    return 0;
}


