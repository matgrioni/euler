{-
 - Author: Matias Grioni
 - Created: 7/7/15
 -
 - Finds the largest prime factor of a given number
 -}

module Main where

prime :: Integer -> Bool
prime n = null [x | x <- [2..floor . sqrt . fromIntegral $ n], n `mod` x == 0]

factors :: Integer -> [Integer]
factors n = [x | x <- reverse [2..floor . sqrt . fromIntegral $ n], n `mod` x == 0]

largestPrimeFactor :: Integer -> Integer
largestPrimeFactor n = head $ filter prime $ factors n

main = do
    putStrLn "Finds the largest prime factor of n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Integer

    print $ largestPrimeFactor n
