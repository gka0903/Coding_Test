#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(int q, int r, string code) {
    string answer = "";

    // 이 부분에 로직을 구현하여 answer를 완성하세요.
    for (int i = 0; i < code.length(); i++) {
        if(i % q == r){
            answer += code[i];
        }

    }

    return answer;
}

int main() {
    // ---- 예제 1 실행 ----
    int q1 = 3;
    int r1 = 1;
    string code1 = "qjnwezgrpirldywt";
    
    // solution 함수를 호출하고 결과를 result1 변수에 저장
    string result1 = solution(q1, r1, code1);
    
    // 결과를 화면에 출력 (std::cout 사용)
    cout << "예제 1 결과: " << result1 << endl; // 예상 결과: "jerry"

    // ---- 예제 2 실행 ----
    int q2 = 1;
    int r2 = 0;
    string code2 = "programmers";
    
    string result2 = solution(q2, r2, code2);
    
    cout << "예제 2 결과: " << result2 << endl; // 예상 결과: "programmers"
    
    return 0; // 프로그램이 정상적으로 종료되었음을 의미
}
