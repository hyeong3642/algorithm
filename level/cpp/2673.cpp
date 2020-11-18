#include <iostream>
using namespace std;

int f(int a){
  int b = a;
  while(b!=0){
    a+= b%10;
    b =b/10;
  }
  return a;
}
int main(){
  int arr[10001] ={0};
  for(int i=1; i<10001; i++){
    int idx = f(i);
    if(idx<=10001){
      arr[idx] = true;
    }
  }
  for(int i=1; i<10001; i++){
    if(arr[i]==0){
      cout << i << endl;
    }
  }

}
