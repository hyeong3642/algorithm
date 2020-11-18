#include <iostream>
#include <string>
using namespace std;

int main(){
  int numTestCases;
  cin >> numTestCases;
  for(int i=0; i<numTestCases; i++){
    string a;
    cin >> a;
    int ans=0;
    int count=0;
    for(int j=0; j<a.size(); j++){
      if(a[j]=='O'){
        count ++;
        ans += count;
      }
      if(a[j]=='X'){
        count =0;
      }
    }
    cout << ans << endl;
  }
}
