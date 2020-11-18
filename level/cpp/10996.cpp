#include <iostream>
using namespace std;

int main(){
  int num;
  cin >> num;
  if(num ==1){
    cout <<"*";
  }
  else{
    for(int i=1; i<2*num+1; i++){
      for(int j=1; j<num+1; j++){
        if(i%2==1){
          if(j%2==1){
            cout << "*";
          }
          else{
            cout << " ";
          }
        }
        else{
          if(j%2==1){
            cout << " ";
          }
          else{
            cout << "*";
          }
        }
      }
      cout << endl;
    }
  }
}
