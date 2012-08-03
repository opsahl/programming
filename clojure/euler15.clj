(defn factorial [n]
  (reduce *' (range 1 (inc n))))

(defn combinations [n k]
  (/ (factorial (+' n k)) (*' (factorial n) (factorial k))))

(println (combinations 20 20)) 
