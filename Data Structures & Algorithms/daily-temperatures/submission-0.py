class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol_days = [0 for i in range(len(temperatures))]
        stack_temp_days = []
        for ind, temp in enumerate(temperatures):
            if len(stack_temp_days) == 0:
                stack_temp_days.append((temp,ind))
            else:
                while(len(stack_temp_days)>0 and stack_temp_days[-1][0]<temp):
                    curr_tem, days = stack_temp_days.pop()
                    sol_days[days] = ind - days
                stack_temp_days.append((temp,ind))
        return sol_days