use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {

        let mut current : (i32, i32)= (0, 0);

        let mut visited : HashSet< (i32, i32)> = HashSet::new();

        visited.insert(current);

        for c in path.chars() {
            match c {
                'N' => current.0 += 1,
                'S' => current.0 -= 1,
                'E' => current.1 += 1,
                'W' => current.1 -= 1,
                _ => {}
            }

            if visited.contains(&current){
                return true;
            }
            visited.insert(current);
        }

        false

    }
}