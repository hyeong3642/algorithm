#include <iostream>
using namespace std;

int main(){
  int numTestCases;
  cin >> numTestCases;
  for (int i=0; i<numTestCases; i++){
    int k, n;
    cin >> k >> n;
    int apt[15][15] ={0,};
    for(int j=1; j<15; j++){
      apt[0][j] = j;
    }
    for(int l=1; l<15; l++){
      for(int m=1; m<15; m++){
        apt[l][m] = apt[l-1][m] + apt[l][m-1];
      }
    }
    cout << apt[k][n] << endl;
  }
}
