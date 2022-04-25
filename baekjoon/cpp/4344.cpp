#include <iostream>
#include <vector>
using namespace std;

int main(){
  int numTestCases;
  cin >> numTestCases;
  for(int i=0; i<numTestCases; i++){
    int num;
    float count =0;
    cin >> num;
    float avr =0;
    vector<float> v;
    for(int j=0; j<num; j++){
      int b;
      cin >>b;
      avr+=b;
      v.push_back(b);
    }
    avr= avr/num;
    for(int k=0; k<v.size(); k++){
      if(v[k]>avr){
        count +=1;
      }
    }
    cout.precision(3);
    cout << fixed << count/num*100<< "%" << endl;
  }
}
