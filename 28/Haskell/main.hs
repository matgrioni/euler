{-
 - Author: Matias Grioni
 - Created: 7/16/15
 -
 - Sums the diagonals in an n x n spiral as defined by problem 28 in
 - project euler.
 -}

module Main where

main = do
    putStrLn "Sum diagonals in an n x n spiral"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int


    print $ 1 + sum [4*(4*n*n - 7*n + 4) | n <- [2..(n + 1) `div` 2]]
