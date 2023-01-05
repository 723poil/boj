def solution(nums):
    answer = 0
    is_dict = dict()
    
    nums = sorted(nums)
    best_sum = nums[-1] + nums[-2] + nums[-3]
    is_prime = [True] * (best_sum + 1)
    checkPrime(best_sum, is_prime)
    
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i == j or i == k or j == k:
                    continue
                nlist = sorted([nums[i], nums[j], nums[k]])
                
                if is_dict.get(str(nlist)) is None:
                    list_sum = nums[i]+nums[j]+nums[k]
                    is_dict.update({str(nlist): 1})
                    
                    if is_prime[list_sum] == True:
                        answer += 1
    
    return answer
    
def checkPrime(n, primes):
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] == True:
            for j in range(i+i, n+1, i):
                primes[j] = False