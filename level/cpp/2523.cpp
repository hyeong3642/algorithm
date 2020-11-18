#include <iostream>
using namespace std;

int main(){
  int num;
  cin >> num;
  for(int i=1; i<num+1; i++){
    for(int j=0; j<i; j++){
    cout << "*";
    }
    cout << endl;
  }
  for(int k=num-1; k>0; k--){
    for(int l=0; l<k; l++){
      cout << "*";
    }
    cout << endl;
  }
}
