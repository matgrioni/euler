{-
 - Author: Matias Grioni
 - Created: 7/2/2015
 -
 - Solution to Project Euler problem 2 using Haskell. Sums all even valued
 - terms of the Fibonacci sequence less than n, which is input by the user.
 -}

module Main where

-- Fibonacci sequence up to n, assuming n is a natural number.
fibonacci :: Int -> [Int]
fibonacci 1 = [1]
fibonacci 2 = [2, 1]
fibonacci n
    | n < 1 = error "Parameter must be a natural number"
    | otherwise = (head p + (head $ tail p)):p
    where p = fibonacci (n-1)

main = do
    putStrLn "Sums even Fibonacci sequence terms less than n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    -- Finds the sum of all fibonacci terms less than n that are even
    -- Very inefficient as for each term, the entire fibonacci sequence is
    -- generated and the head of the list is taken. Come back later once
    -- I'm more familiar with the language.
    print $ sum $ filter ((== 0) . (`mod` 2)) $ takeWhile (< n) [head (fibonacci n) | n <- [1..]]
