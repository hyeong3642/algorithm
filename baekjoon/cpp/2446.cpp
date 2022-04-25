#include <iostream>
using namespace std;

int main(){
  int num,n;
  cin >> num;
  n = num;
  for(int i=0; i<num; i++){
    for(int j=0; j<i; j++){
      cout << " ";
    }
    for(int k=1; k<2*n; k++){
      cout << "*";
    }
    cout << endl;
    n -=1;
  }
  n=1;
  for(int m=num-2; m>=0; m--){
    for(int o=0; o<m; o++){
      cout << " ";
    }
    for(int p=0; p<2*n+1; p++){
      cout << "*";
    }
    cout << endl;
    n+=1;
  }
}
