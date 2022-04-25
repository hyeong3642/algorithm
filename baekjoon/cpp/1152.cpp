#include <iostream>
using namespace std;

int main(){
  string a;
  getline(cin, a);
  int count =0;
  for(int i=0; i<a.length(); i++){
    if(a[i]==' '){
      count +=1;
    }
  }
  if(a[0]==' '){
    count -=1;
  }
  if(a[a.length()-1]==' '){
    count -=1;
  }
  cout << count+1;
}
