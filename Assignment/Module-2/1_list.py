
def listfunction(list1=[]):
  
  unique_list = list(set(list1))

  unique_count = len(unique_list)

  result_dict = {
      "original_list": list1,
      "unique_values": unique_list,
      "count": unique_count,
  }

  return result_dict


user_input = input("Enter numbers for lists with Comma: ")

listA = list(map(int, user_input.split(","))) if user_input.strip() else []

final_result = listfunction(list1=listA)

print("\nDictionary:")
print(final_result)

print(f"\nOriginal List: {final_result['original_list']}")
print(f"Unique Values: {final_result['unique_values']}")
print(f"Count: {final_result['count']}")
