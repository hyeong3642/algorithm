#include <iostream>
using namespace std;

int main(){
  int a,b,c;
  cin >> a >> b >>c;
  int tmp = 0;
  if(b>=c){
    tmp = -1;
  }
  else{
    tmp = a/(c-b) +1;
  }
  cout << tmp;
}
