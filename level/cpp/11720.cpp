#include <iostream>
#include <string>
using namespace std;

int main(){
  int num;
  cin >> num;
  string a;
  int ans =0;
  cin >> a;
  for(int i=0; i<num; i++){
    ans += (a[i]-'0');
  }
  cout << ans;

}
