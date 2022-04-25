#include <iostream>
using namespace std;

bool f(int a){
  if(a<100){
    return true;
  }
  int one,ten,hun;
  one = a%10;
  ten = a%100/10;
  hun = a/100;
  if(ten-one == hun-ten){
    return true;
  }
  return false;
}

int main(void){
  int num;
  int count =0;
  cin >> num;
  for(int i=1; i<num+1; i++){
    if(f(i)){
      count +=1;
    }
  }
  cout << count;
}
