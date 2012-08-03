(defn listify [number]
  (let [strnum (str number)]
    (map #(Character/digit % 10) strnum)))

(defn lazy-selfpower [num times]
  (reduce *' (take times (repeat num))))

(defn solve []
  (reduce + (listify (lazy-selfpower 2 1000))))

(println  (solve)) 
