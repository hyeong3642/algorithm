#include <iostream>
using namespace std;

int main(){
  int num;
  cin >>num;
  int a[num];
  for(int i=0; i<num; i++){
    cin >> a[i];
  }
  int min = a[0];
  int max = a[0];
  for(int i=0; i<num; i++){
    if(a[i]<min){
      min = a[i];
    }
    if(a[i]>max){
      max = a[i];
    }
  }
  cout << min << " " << max;
}
