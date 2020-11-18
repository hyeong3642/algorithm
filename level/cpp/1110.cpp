#include <iostream>
using namespace std;

int main(){
  int num, tmp, front, back;
  int count = 0;
  cin >> num;
  tmp = num;

  while(true){
    front = num/10;
    back = num%10;
    num = back *10 +((front+back)%10);
    count += 1;
    if(num == tmp){
      cout << count << endl;
      break;
    }
  }
}
