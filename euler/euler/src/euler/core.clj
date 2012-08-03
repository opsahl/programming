(ns euler.core)

(defn solve1 [limit]
  (reduce + (for [x (range 1 limit) :when (or (zero? (rem x 3)) (zero? (rem x 5)))] x)))
