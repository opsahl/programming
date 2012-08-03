(defn solve [max]
  (reduce + (for [x (range 1, max) :when (or (zero? (rem x 3)) (zero? (rem x 5)))] x)))

(println (solve 10))
(println (solve 1000))
