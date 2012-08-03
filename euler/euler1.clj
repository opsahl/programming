(defn multi3or5? [num]
  (if (or (zero? (rest num 3)) (zero? (rest num 5)))
    true
    false))

(reduce + (for [x in (range 10) :when (multi3or5? num)]))
