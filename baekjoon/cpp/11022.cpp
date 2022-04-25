#include <iostream>
#include <ios>
using namespace std;

int main(){
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  int numTestCases;
  cin >> numTestCases;
  for(int i=0; i<numTestCases; i++){
    int a,b;
    cin >> a >> b;
    cout << "Case #" << i+1 << ": " << a << " + " << b << " = " << a+b << "\n";
  }
}
