{-
 - Author: Matias Grioni
 - Created: 7/7/15
 -
 - Finds the largest prime factor of a given number
 -}

module Main where

sqrt' :: Integer -> Integer
sqrt' n
    | n == 1    = 1
    | otherwise = (k + (n-1) `div` k) `div` 2
    where k = sqrt'(n-1)

isPrime :: Integer -> Bool
isPrime n = length (factors n) == 0

factors :: Integer -> [Integer]
factors n = filter ((== 0) . (n `mod`)) [2..sqrt' n]

largestPrimeFactor :: Integer -> Integer
largestPrimeFactor n = last $ filter isPrime $ factors n

main = do
    putStrLn "Finds the largest prime factor of n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Integer

    print $ largestPrimeFactor n
