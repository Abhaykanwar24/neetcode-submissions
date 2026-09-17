class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_cost = []
        for i in range(len(gas)):
            gas_cost.append(gas[i] - cost[i])

        total = 0
        cur_sum = 0
        start_index = 0

        for i in range(len(gas_cost)):
            total += gas_cost[i]
            cur_sum += gas_cost[i]

            if cur_sum < 0:
                start_index = i + 1
                cur_sum = 0

        return start_index if total >= 0 else -1