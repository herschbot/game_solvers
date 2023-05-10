import operator

START_LIST = [7,9,11,13,20,25]
TARGET = 422
OPERATIONS = {
  operator.add: '+', 
  operator.sub: '-', 
  operator.mul: '*', 
  operator.truediv: '/'}

def try_operations(avail_nums, operations_performed=[]):
  for i in range(len(avail_nums)):
    for j in range(i+1, len(avail_nums)):
      pop_list = avail_nums.copy()
      # pop higher index first
      nums = [pop_list.pop(j), pop_list.pop(i)]
      nums.sort()
      for opp in OPERATIONS:
        new_num = run_opp(nums[1], nums[0], opp)
        if new_num != int(new_num):
          continue
        opp_str = str(nums[1]) + OPERATIONS[opp] + str(nums[0])
        if new_num == TARGET:
          return operations_performed + [opp_str]
        elif len(pop_list) == 0:
          continue
        new_list = pop_list.copy()
        new_list.append(int(new_num))
        next_step = try_operations(new_list, operations_performed + [opp_str])
        if next_step != []:
          return next_step        
  return []

def run_opp(a, b, operation):
  try:
    return operation(a,b)
  except ZeroDivisionError:
    return 0

def main():
  print(try_operations(START_LIST))

if __name__ == "__main__":
  main()