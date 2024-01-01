def findRestaurant(list1, list2):
    arr = []
    answer = []
    for index, string in enumerate(list1):
        if string in list2:
            arr.append((index + list2.index(string), string))
    m_arr = min(arr)[0]
    for i in arr:
        if i[0] == m_arr:
            answer.append(i[1])
    return answer


print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
