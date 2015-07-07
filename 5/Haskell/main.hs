{-
 - Author: Matias Grioni
 - Created: 7/7/2015
 -
 - Finds the least common multiple of all numbers between 1 and n.
 -}

module Main where

gcd' :: Int -> Int -> Int
gcd' a 0 = a
gcd' a b = gcd b $ a `div` b

lcm' :: Int -> Int -> Int
lcm' a b = a * b `div` gcd a b

main = do
    putStrLn "Find the least common multiple for all numbers between 1 and n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ foldr lcm' 1 [1..n]
