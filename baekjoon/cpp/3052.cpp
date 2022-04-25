#include <iostream>
using namespace std;

int main(){
  int arr[42] = {0};
  int a;
  for(int i=0; i<10; i++){
    cin >> a;
    arr[a%42] +=1;
  }
  int count =0;
  for(int i=0; i<42; i++){
    if(arr[i]!=0){
      count +=1;
    }
  }
  cout << count;
}
