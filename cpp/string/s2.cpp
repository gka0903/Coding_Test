#include <iostream>
#include <string>

using namespace std;

int solution(string t, string p){
  int answer = 0;
  int l = p.length();
  long long num_p = stoll(p);

  for (int i = 0; i <= t.length() - l; i++){
    string sub = t.substr(i, l);
    long long num_sub = stoll(sub);
    if (num_sub <= num_p){
      answer += 1;
    }
  }

  return answer;
}

int main() {

    string t = "3141592";
    string p = "271";
    string code1 = "qjnwezgrpirldywt";
    
    // solution 함수를 호출하고 결과를 result1 변수에 저장
    int result1 = solution(t, p);
    
    // 결과를 화면에 출력 (std::cout 사용)
    cout << "예제 1 결과: " << result1 << endl; 

  return 0;
}
