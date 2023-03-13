from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for i in range(len(energy)):
            initialEnergy -= energy[i]
            if initialExperience <= experience[i]:
                ans += experience[i] - initialExperience + 1
                initialExperience = 2 * experience[i] + 1
            else:
                initialExperience += experience[i]
        if initialEnergy <= 0:
            ans -= initialEnergy - 1
        return ans