{-
 - Author: Matias Grioni
 - Created: 7/27/15
 -
 - Finds a pythagorean triplet where a + b + c = 1000 and provides a*b*c
 -}

module Main where

main = do
    putStrLn "Finds a pythagorean triplet where a + b + c = 1000 and provides a*b*c"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print [a*b*c | a <- [1..998], b <- [1..(1000-a-1)], c <- [1..(1000-a-b)], a*a+b*b == c*c, a+b+c == n]
