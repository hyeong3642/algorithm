#include <iostream>
#include <string>
using namespace std;

int main(){
  string str;
  cin >> str;
  int count;
  for(char i = 'a'; i<='z'; i++){
    count = str.find(i);
    cout << count << " ";
  }
}
