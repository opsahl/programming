main :: IO ()

let solve max = sum[x | x <- [1..max], x `mod` 3 == 0 || x `mod` 5 == 0]

putStrLn(solve 10)
print(solve 1000)
