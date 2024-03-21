impl Solution {
    pub fn minimum_operations(mut nums: Vec<i32>) -> i32 {

        // sort the numbers
        nums.sort();

        // ope = 0
        let mut ope : i32 = 0;

        // count = 0
        let mut count : i32 = 0;

        // for each element
        for element in nums{

            if element == 0{
                continue;
            }

            let result = element - ope;

            if result > 0{
                count += 1;
                ope += result;
            }
        }
            
        return count;

    }
}
