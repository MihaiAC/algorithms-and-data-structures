struct Solution;
impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        words.iter().enumerate().filter_map(|(idx, word)| if word.contains(x) {Some(idx as i32)} else {None}).collect()
    }
}