class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        answer = []

        while i < j:
            if numbers[i] + numbers[j] == target:
                answer.append(i + 1)
                answer.append(j + 1)
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        
        return answer