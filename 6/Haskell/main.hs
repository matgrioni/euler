{-
 - Author: Matias Grioni
 - Created: 7/7/15
 -
 - Finds the difference between the square of the sum and the sum of the
 - squares of numbers between 1 to n.
 -}

module Main where

main = do
    putStrLn "Finds the difference between the square of the sum and the sum"
    putStrLn "of the squares fo numbers between 1 to n"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ (sum [1..n]) ^ 2 - (sum $ map (^2) [1..n])
