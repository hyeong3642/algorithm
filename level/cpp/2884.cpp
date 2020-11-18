#include <iostream>
using namespace std;

int main(){
  int a,b;
  cin >> a >> b;
  if(b>=45){
    cout << a << " " << b-45;
  }
  else{
    if(a==0){
      cout << "23" << " " <<60+(b-45);
    }
    else{
      cout << a-1 << " " << 60+(b-45);
    }
  }
}
