#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  int a[99999], b[99999], sum[99999], c;
  c = 0;
  int max;
  string A, B;
  cin >> A >> B;
  for(int i=0; i<A.length(); i++){
    char tmp = A.at(i);
    a[A.length()-i] = atoi(&tmp);
  }
  for(int i=0; i<B.length(); i++){
    char tmp = B.at(i);
    b[B.length()-i] = atoi(&tmp);
  }
  if(A.length()>=B.length()){
    max = A.length();
  }
  else{
    max = B.length();
  }
  for(int i=1; i<=max; i++){
    sum[i] = a[i] + b[i] + c;
    if(sum[i]>=10){
      sum[i] -= 10;
      c = 1;
    }
    else{
      c =0;
    }
  }
  if(c==1){
    cout << c;
  }
  for(int i=0; i<max; i++){
    cout << sum[max-i];
  }
  return 0;

}
