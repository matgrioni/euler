module Main where

import Text.Printf
import System.CPUTime

main = do
    putStrLn "Sums digits from 1 to n divisible by 3 or 5"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    start <- getCPUTime
    let r = sum $ filter (\a -> a `mod` 3 == 0 || a `mod` 5 == 0) [1..n-1]
    end <- getCPUTime
    let time = (fromIntegral(end - start)) / (10 ^ 12)

    printf "%0.5f s\n" (time :: Double)
    printf "Result: %d\n" (r :: Int)
