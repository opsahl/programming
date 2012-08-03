(defn fibo [] 
 (map first (iterate (fn [[a b]] [b (+ a b)]) [1 2]))) 

(defn solve [top]
  (reduce + (filter even? (for [x (fibo) :while (< x top)] x))))

(println (solve 4000000))
