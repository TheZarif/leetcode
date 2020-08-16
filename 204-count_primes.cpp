#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if(n==0){
            return 0;
        }
        int counter=0;
        bool* notPrimes=new bool[n]{0};

        for(long int i=2;i<n;i++){
            if (!notPrimes[i])
            {
                for(long int j=i;i*j<n;j++){
                    notPrimes[j*i]=true;
                }
            }
        }

        for(long int i=2;i<n;i++){
            if (!notPrimes[i])
            {
                //cout << "Prime: " << i << endl;
                counter++;
            }
        }
        delete [] notPrimes;
        return counter;
    }
};

int main(){
    Solution solution;
    cout << solution.countPrimes(0)<<endl;
    cout << solution.countPrimes(10)<<endl;
    cout << solution.countPrimes(499979)<<endl;
}
