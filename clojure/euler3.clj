(defn prime-candidates
  ([upto] (cond
            (< upto 2) '()
            (< upto 3) '(2)
            (< upto 5) '(3 2)
            :default (prime-candidates upto '() 2)))
  ([upto candidates addnum]
   (if (empty? candidates) 
     (recur upto (conj candidates 2 3 5) 2)
     (if (> (first candidates) upto)
       (rest candidates)
       (if (= addnum 2)
         (recur upto (conj candidates (+ 2 (first candidates))) 4)
         (recur upto (conj candidates (+ 4 (first candidates))) 2))))))

(defn prime? [num]
  (every? #(not (=(rem num %) 0)) (prime-candidates (Math/sqrt num))))

(defn primes-upto [upto]
  (filter prime? (prime-candidates upto)))

(defn factors [num]
  (filter #(= (rem num %) 0) (primes-upto (Math/sqrt num))))
