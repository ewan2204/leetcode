class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Variables
        # Track the two types of fruit used.
        current_fruit_type = fruits[len(fruits)-1]
        alternative_fruit_type = fruits[len(fruits)-1]
        # Keep track of the current and overall fruit counts.
        current_fruit_count = 0
        currentFruitRun = 0

        # Keep track of the overall maximum fruit amount.
        overall_maximum_fruit_number = 0

        # Loop through back to front of the list and check if fruit is different from current
        for i in range(len(fruits)-1, -1, -1):
            if fruits[i] == current_fruit_type:
                ## If fruit is same as current just add to total.
                current_fruit_count +=1
                currentFruitRun     +=1
            else:
                # If not check if fruit is alternative fruit if so thjis run can contiue.
                if fruits[i] == alternative_fruit_type:
                    # If it is switch current and alternative.
                    alternative_fruit_type = current_fruit_type
                    current_fruit_type = fruits[i]
                    current_fruit_count = 1
                    currentFruitRun+=1
                else:
                    # If not we restart the run from the current count.
                    overall_maximum_fruit_number = max(overall_maximum_fruit_number, currentFruitRun)
                    alternative_fruit_type = current_fruit_type
                    current_fruit_type = fruits[i]
                    currentFruitRun = current_fruit_count + 1
                    current_fruit_count = 1
        overall_maximum_fruit_number = max(overall_maximum_fruit_number, currentFruitRun)
        return overall_maximum_fruit_number
