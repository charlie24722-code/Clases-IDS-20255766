num_DUI = input()

print(len(num_DUI) == 10 
      and (num_DUI[-2]) == "-" 
      and float(num_DUI[-1]) == int(num_DUI[-1]))