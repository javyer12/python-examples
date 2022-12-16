def checkList():
  itemList = []
  item = input("Insert your list, use (,) to separate items: ")
  # num variable keep integer item(number from the list)
  num = item.split(",")
  # loop to add each number to the list
  for i in num:
    e = int(i)
    itemList.append(e)
  # get the first number of the list to make a dynamic comparison
  firstNum = itemList[0]
  # loop to check the index and comparing index and number
  for i in itemList:
    itemIndex = itemList.index(i)
    indexValue = itemIndex + firstNum
    if (indexValue != i):
      print(f"oop!!, Error,list is not consecutive: wrong value: {i}, index: {itemIndex}")
      break;

  print(" ")
  print("The list you inserted:")
  # print list inserted by the user
  print(itemList)
  return itemList

checkList()