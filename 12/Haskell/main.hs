{-
 - Author: Matias Grioni
 - Created: 7/27/15
 -
 - Finds the first triangular number with over n divisors.
 -}

module Main where

-- Returns whether n can be expressed in terms of an integer x as x * x
perfectSquare :: Int -> Bool
perfectSquare n = (floor . sqrt . fromIntegral $ n) ^ 2 == n

-- To get the number of factors of a number, go up to but don't include the
-- floor of the square root when checking. This prevents it from being counted
-- twice. If the number is a perfect square, add one to include the sqrt.
numFactors :: Int -> Int
numFactors n
    | perfectSquare n = factors + 1
    | otherwise = factors
    where lim = (-) (floor . sqrt . fromIntegral $ n) 1
          factors = length [x | x <- [1..lim], n `mod` x == 0] * 2

main = do
    putStrLn "Finds the first triangular number with over n divisors"
    putStrLn "Enter n > "
    input <- getLine
    let n = read input :: Int

    print $ head . filter ((>n) . numFactors) $ [(x*x+x) `div` 2 | x <- [1..]]
