#include <iostream>
#include <ios>
using namespace std;

int main(){
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  int a;
  cin >> a;
  for(int i=0; i<a; i++){
    for(int j=0; j<a-(i+1); j++){
      cout << " ";
    }
    for(int k=0; k<i+1; k++){
      cout << "*";
    }
    cout << "\n";
  }
}
