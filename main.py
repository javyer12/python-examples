def check_list():
    item_list = []
    item = input("Insert your list, use (,) to separate numbers: ")
    # num variable keep integer item(number from the list)
    num = item.split(",")
    # loop to add each number to the list
    for i in num:
        int_index = int(i)
        item_list.append(int_index)
    # get the first number of the list to make a dynamic comparison
    first_num = item_list[0]
    # loop to check the index and comparing index and number
    for i in item_list:
        item_index = item_list.index(i)
        index_value = item_index + first_num
        if index_value != i:
            print(
                f"oop!!,❌ Error,list is not consecutive: wrong value: {i}, index: {item_index}, fix your list.")
            break
        if i == item_list[-1]:
            print("Congratulation ⭐️ List is Consecutive")

    print(" ")
    print("The list you inserted:")
    # print list inserted by the user
    print(item_list)
    return item_list


def run():
    check_list()


if __name__ == "__main__":
    run()


# To add:
  #function to solve problem when wrong value is less than last right value
  # input to sort the list
  # if the list has values repeated, remove them from the list
  # sort the list by number
  #if the list is missing a value, add the value on that index
  #sum 
