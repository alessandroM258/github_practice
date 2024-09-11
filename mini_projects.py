total_count = {"aluminum": 135, "plastic": 102, "paper": 213}

def sortItems(itemString):
  for items in itemString:
    if items == "A":
      total_count["aluminum"] += 1 
    elif items == "P":
     total_count["plastic"] += 1
    elif items == "R":
      total_count["paper"] += 1
sortItems('AAPAARRRRPAAPPRRP')
print(total_count)
