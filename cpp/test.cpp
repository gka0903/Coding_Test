#include <vector>
#include <string>
#include <algorithm> // sort, reverse 등
#include <iostream>

// 벡터 내용을 출력하기 위한 보조 함수
template<typename T>
void printVector(const std::vector<T>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << (i == vec.size() - 1 ? "" : ", ");
    }
    std::cout << "]" << std::endl;
}

using namespace std;

int main(){

// (printVector 함수는 위에 정의되었다고 가정)

  std::vector<std::string> fruits = {"apple", "banana"};
  std::cout << "초기 리스트: "; printVector(fruits);

  fruits.push_back("cherry");
  std::cout << "push_back 후: "; printVector(fruits);

  fruits.insert(fruits.begin() + 1, "kiwi");
  std::cout << "insert 후: "; printVector(fruits);

  std::vector<std::string> more_fruits = {"orange", "grape"};
  fruits.insert(fruits.end(), more_fruits.begin(), more_fruits.end());
  std::cout << "insert(extend) 후: "; printVector(fruits);

  // remove "banana" (하나만)
  auto it_remove = std::find(fruits.begin(), fruits.end(), "banana");
  if (it_remove != fruits.end()) fruits.erase(it_remove);
  std::cout << "remove 후: "; printVector(fruits);

  std::string last_item = fruits.back();
  fruits.pop_back();
  std::cout << "pop_back 후: "; printVector(fruits);
  std::cout << "제거된 값: " << last_item << std::endl;

  auto it_find = std::find(fruits.begin(), fruits.end(), "kiwi");
  long kiwi_index = std::distance(fruits.begin(), it_find);
  std::cout << "kiwi의 인덱스: " << kiwi_index << std::endl;

  long apple_count = std::count(fruits.begin(), fruits.end(), "apple");
  std::cout << "apple의 개수: " << apple_count << std::endl;

  std::sort(fruits.begin(), fruits.end());
  std::cout << "sort 후: "; printVector(fruits);

  std::reverse(fruits.begin(), fruits.end());
  std::cout << "reverse 후: "; printVector(fruits);

  fruits.clear();
  std::cout << "clear 후: "; printVector(fruits);

  return 0;
}