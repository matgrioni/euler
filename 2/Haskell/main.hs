{-
 - Author: Matias Grioni
 - Created: 7/2/2015
 -
 - Solution to Project Euler problem 2 using Haskell. Sums all even valued
 - terms of the Fibonacci sequence less than n, which is input by the user.
 - DOES NOT WORK
 -}

module Main where

fibonacci :: Int -> [Int]
fibonacci 1 = [1]
fibonacci 2 = [1, 2]
fibonacci n = (head prior + head (tail prior)):prior
    where prior = fibonacci (n-1)
    where next = head prior + head $ tail prior

main = do
    putStrLn "Sums even Fibonacci sequence terms less than n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print (sum (filter ((== 0) . (`mod` 2)) (fibonacci n)))
