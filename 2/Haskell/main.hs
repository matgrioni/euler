{-|
 - Author: Matias Grioni
 - Created: 7/2/2015
 -
 - Solution to Project Euler problem 2 using Haskell. Sums all even valued
 - terms of the Fibonacci sequence less than n, which is input by the user.
 - DOES NOT WORK.
 -}

module Main where

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
    print $ sum $ map head $ filter ((== 0) . (`mod` 2) . head) $ takeWhile ((< n) . head) [fibonacci n | n <- [1..]]

    --print $ sum $ filter ((==0) . (`mod` 2)) $ takeWhile (<n) . head $ [fibonacci n | n <- [1..]]
