{-
 - Author: Matias Grioni
 - Created: 7/7/15
 -
 - Finds the largest palindrome of the product of 2 n digit numbers.
 -}

module Main where

isPalindrome :: Int -> Bool
isPalindrome n = str == reverse str
    where str = show n

main = do
    putStrLn "Finds the largest palindrome of the product of 2 n digit nums."
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ maximum $ filter isPalindrome [i * j | i <- [1..10^n], j <- [1..10^n]]
