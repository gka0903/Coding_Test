#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <unordered_set>
#include <algorithm> // std::find를 사용하기 위함

using namespace std;

// 두 단어가 한 글자 차이인지 판별하는 헬퍼 함수
bool can_transform(const std::string& word1, const std::string& word2);

int solution(std::string begin, std::string target, std::vector<std::string> words) {
    // 1. 예외 처리: target이 words 리스트에 없으면 변환이 불가능하므로 0을 반환.
    //    std::find를 사용하여 words 벡터 내에 target이 있는지 확인.
    if (find(words.begin(), words.end(), target) == words.end()){
      return 0;
    }
    
    // 2. BFS를 위한 큐(queue)를 생성.
    //    C++에서는 std::queue를 사용.
    //    큐에는 {현재 단어, 현재까지의 변환 단계}를 std::pair 형태로 저장.
    queue<pair<string, int>> q;

    // 3. 방문 여부를 기록할 해시 집합(hash set)을 생성.
    //    C++에서는 std::unordered_set을 사용하여 O(1) 시간 복잡도로 조회가 가능.
    unordered_set<string> visited;

    // 4. BFS 시작점 초기화:
    //    - 큐에 시작 단어와 초기 단계(0)를 추가: {begin, 0}.
    //    - 방문 기록에 시작 단어를 추가.
    q.push({begin, 0});
    visited.insert(begin);

    // 5. 큐가 비어있지 않은 동안 반복.
    while (!q.empty()) {
        // 5-1. 큐에서 가장 앞에 있는 요소를 꺼낸다.
        //      - 현재 단어(current_word)와 현재 단계(count)를 변수에 저장.
        //      - 큐에서 해당 요소를 제거.
        pair<string, int> current = q.front();
        string current_word = current.first;
        int count = current.second;
        q.pop();

        // 5-2. 종료 조건: 만약 현재 단어가 target과 일치하면,
        //      - 현재 단계(count)가 최단 거리이므로 즉시 반환하고 함수를 종료.
        if (current_word == target){
            return count;
        }

        // 5-3. 다음 변환 단어 탐색: words 벡터의 모든 단어를 순회.
        for (const auto& next_word : words) {
            // 5-3-1. 아직 방문하지 않았고(visited set에 없고),
            //         변환이 가능한 단어(can_transform 호출)라면
            if (visited.find(next_word) == visited.end()){
                if (can_transform(current_word, next_word)){
                    // 5-3-2. 해당 단어를 방문 처리(visited set에 추가).
                    visited.insert(next_word);

                    // 5-3-3. 큐에 다음 탐색 대상을 추가: {next_word, count + 1}.
                    q.push({next_word, count + 1});
                }
            }
        }
    }

    // 6. 큐가 모두 비워질 때까지 target에 도달하지 못했다면 변환 불가. 0을 반환.
    return 0;
}


bool can_transform(const string& word1, const string& word2) {
    // 1. 다른 글자의 개수를 세기 위한 카운터 변수를 초기화.
    int diff = 0;
    
    // 2. 두 단어의 길이만큼 반복하면서 각 자리의 글자를 비교.
    //    - 글자가 다르면 카운터를 1 증가.
    for (int i = 0; i < word1.length(); i++){
        if (word1[i] != word2[i])
            diff++;
    }

    if (diff == 1){
        return true;
    }

    // 3. 반복이 끝난 후, 카운터의 값이 정확히 1이면 true, 아니면 false를 반환.
    return false;
}

// 프로그램을 실행하기 위한 main 함수
int main() {
    // 문제의 예시 입력
    string begin = "hit";
    string target = "cog";
    vector<string> words = {"hot", "dot", "dog", "lot", "log", "cog"};

    // solution 함수 호출 및 결과 출력
    int result = solution(begin, target, words);
    cout << "최소 변환 단계: " << result << endl; // 예상 출력: 4

    return 0;
}
