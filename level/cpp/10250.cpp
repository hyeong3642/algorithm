#include <iostream>
using namespace std;

int main(){
  int numTestCases;
  cin >> numTestCases;
  for(int i=0; i<numTestCases; i++){
    int H, W, N;
    cin >> H >>W >>N;
    int YY, XX;
    YY = N%H;
    XX = N/H;
    if(YY>0){
      XX++;
    }
    else{
      YY = H;
    }
    cout << YY*100 + XX << endl;
  }
}
