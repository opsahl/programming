(defn pythagorian-triplets []
  (for [a (range 1 1000) b (range 1 1000) :when (and (< a b) (< b (Math/sqrt (+ (* a a) (* b b)))) (= (Math/floor (Math/sqrt (+ (* a a) (* b b)))) (Math/sqrt (+ (* a a) (* b b)))))] [a b (long (Math/sqrt (+ (* a a) (* b b))))]))

(defn find-with-sum [sum]
    (first (drop-while #(not (= sum (reduce + %))) (pythagorian-triplets))))

(defn solve [sum]
  (let [lst (find-with-sum sum)]
    (reduce * lst)))
