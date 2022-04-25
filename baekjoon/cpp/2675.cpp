#include <iostream>
#include <string>
using namespace std;

int main(){
  string str;
  cin >> str;
  cout << str;
  int count = 1;
  for(int i=0; i<str.length(); i++){
    if(str.at(i) == ' '){
      count +=1;
    }
  }
  cout << count;
}
