#include <iostream>
using namespace std;

int main(){
  int arr[10] = {0};
  int a,b,c,d;
  cin >> a >> b >> c;
  d = a * b * c;
  while(d !=0){
    arr[d%10] +=1;
    d /=10;
  }
  for(int i=0; i<10; i++){
    cout << arr[i] << endl;
  }

}
