#include <iostream>
using namespace std;

int main(){
  int a;
  cin >>a;
  int count =1;
  int minus =6;
  if(a==1){
    cout << "1";
  }
  else{
    a-=1;
    while(a>minus){
      count +=1;
      a -= minus;
      minus +=6;
    }
    count++;
    cout << count;
  }
}
