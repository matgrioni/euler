module Main where

main = do
    putStrLn "Sums digits from 1 to n divisible by 3 or 5"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ sum $ filter (\a -> a `mod` 3 == 0 || a `mod` 5 == 0) [1..n-1]
