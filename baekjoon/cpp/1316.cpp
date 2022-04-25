#include <iostream>
using namespace std;

int main(){
  int numTestCases;
  cin >> numTestCases;
  int count =0;
  for(int i=0; i<numTestCases; i++){
    string a;
    cin >> a;
    bool flag =0;
    for(int j=0; j<a.length(); j++){
      for(int k=j+1; k<a.length(); k++){
        if(a[j]!=a[j+1]&&a[j]==a[k]){
          flag = 1;
        }
      }
    }
    if(flag ==0){
      count +=1;
    }
  }
  cout << count;
}
