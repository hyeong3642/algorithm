#include <iostream>
#include <ios>
using namespace std;

int main(){
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  int a;
  cin >> a;
  for(int i=1; i<a+1; i++){
    cout << i << "\n";
  }
}
