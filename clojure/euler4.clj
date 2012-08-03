(defn make-seq [item]
  (if (sequential? item)
    item
    (str item)))

(defn palindrome? [lst]
  (let [lst (make-seq lst)]
    (if (< (count lst) 2)
      true
      (if (= (first lst) (last lst))
        (recur (rest (butlast lst)))
        false))))

(defn products [topnum]
  (for [x (range topnum -1 -1) y (range topnum -1 -1)] (* x y)))

(defn find-max-palindrome [topnum]
  (reduce max (filter #(palindrome? %) (products topnum))))
