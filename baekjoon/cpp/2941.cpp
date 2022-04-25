#include <iostream>
using namespace std;

int main(){
  string a;
  cin >> a;
  int count = a.length();
  for(int i=0; i<a.length(); i++){
      if(a[i]== 'c'){
        if(a[i+1]=='='||a[i+1]=='-'){
          count--;
        }
      }
      if(a[i]== 'j'){
        if(a[i-1]=='l'||a[i-1]=='n'){
          count--;
        }
      }
      if(a[i]== '='){
        if(a[i-1]=='s'){
          count--;
        }
        else if(a[i-1]=='z'&&a[i-2]!='d'){
          count --;
        }
      }
      if(a[i]== 'd'){
        if(a[i+1]=='-'){
          count--;
        }
        else if(a[i+1]=='z'&&a[i+2]=='='){
          count-=2;
        }
      }
  }
  cout << count;
}
