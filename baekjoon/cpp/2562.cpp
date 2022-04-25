#include <iostream>
#include <ios>
using namespace std;

int main(){
  int arr[9];
  int max = 0;
  int b;
  for(int i=0; i<9; i++){
    cin >> arr[i];
    if(arr[i] > max){
      max = arr[i];
      b = i+1;
    }
  }
  cout << max << "\n" << b;
}
