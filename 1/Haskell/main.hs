module Main where

main = do
    print (sum  (filter ((== 0) . (`mod` 3 || `mod` 5)) [1..999]))
