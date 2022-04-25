#include <iostream>
#include <string>
using namespace std;

int main(){
  string str;
  cin >> str;
  int arr[26] ={0,};
  int max =0;
  int idx =0;
  int count =0;
  for(int i=0; i<str.length(); i++){
    int j = str.at(i);
    if(j<97){
      arr[j-65] += 1;
    }
    else{
      arr[j-97] +=1;
      }
  }
  for(int k=0; k<26; k++){
    if(arr[k]>= max){
      max = arr[k];
      idx = k;
    }
  }
  for(int l=0; l<26; l++){
    if(arr[l]== max){
      count ++;
    }
  }
  if(count >=2){
    cout << "?";
  }
  else {
    cout << (char)(idx+65);
  }
}
