{-
 - Author: Matias Grioni
 - Created: 7/27/15
 -
 - Finds the sum of all primes below n
 -}

module Main where

-- Returns true if the number is prime and false otherwise
prime :: Int -> Bool
prime n = null [x | x <- [2..floor . sqrt . fromIntegral $ n], n `mod` x == 0]

main = do
    putStrLn "Finds the sum of all primes below n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ sum . takeWhile (<n) . filter prime $ [2..]
