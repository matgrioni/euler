{-
 - Author: Matias Grioni
 - Created: 7/7/2015
 -
 - Finds the nth prime number.
 -}

module Main where

isPrime :: Int -> Bool
isPrime n = length [x | x <- [2..n `div` 2], n `mod` x == 0] == 0

nextPrime :: Int -> Int
nextPrime n = head [x | x <- [n+1..], isPrime x]

getPrime :: Int -> Int
getPrime 1 = 2
getPrime n = nextPrime $ getPrime (n - 1)

main = do
    putStrLn "Finds the nth prime number"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ getPrime n
