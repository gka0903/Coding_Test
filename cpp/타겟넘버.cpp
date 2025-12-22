#include <string>
#include <vector>
#include <iostream>

using namespace std;

void dfs(const vector<int>& numbers, int target, int index, int sum, int& answer){
    // 1. 탈출 조건(마지막 숫자까지 모두 확인한 후)
    if (index == numbers.size()) {
        if (sum == target) {
          answer++;
        }
        return;
    }
    
    // 2. 현재 숫자를 더하고 빼고 두 가지 경우로 dfs 재귀호출
    dfs(numbers, target, index + 1, sum + numbers[index], answer);
    dfs(numbers, target, index + 1, sum - numbers[index], answer);  
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers, target, 0, 0, answer);
    return answer;
}

// 로컬에서 테스트를 위한 main 함수
int main() {
    vector<int> numbers = {1, 1, 1, 1, 1};
    int target = 3;
    int result = solution(numbers, target);
    
    // 결과 출력
    cout << "결과: " << result << endl; // 예상 결과: 5
  
    return 0;
}
