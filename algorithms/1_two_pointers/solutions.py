def three_sum(nums, target):
    output = []
    for i in range(len(nums) -1):
        start_idx = i
        second_idx = i+1
        third_idx = second_idx

        third_num = 0 - (nums[start_idx] + nums[second_idx])

        while True:
            if third_idx < len(nums) -1:
                third_idx +=  1
                if nums[third_idx] == third_num:
                    output.append([start_idx, second_idx, third_idx])
                    break
            else:
                break

    return output

def two_sum(nums, target):
    for i in range(len(nums) -1):
        start = i
        end = i+1
        if nums[start] + nums[end] == target:
            print(start, end)
            return start, end

        else:
            while True:
                if end < len(nums) -1:
                    end += 1
                    if nums[start] + nums[end] == target:
                        return start, end
                    elif nums[start] + nums[end] > target:
                        break
                    else:
                        continue

def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
