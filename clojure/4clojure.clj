; check palindromes
(fn [seq]
    (if (> 2 (count seq))
      true
      (if (= (first seq) (last seq))
        (recur (rest (butlast seq)))
        false)))

; flatten sequence
(fn [seq]
    (let [newseq '()]
      (if (not (seq? (first seq)))
        (if (not (empty? seq))
          (do
            (conj newseq (first seq))
            (recur (rest seq)))
          newseq)
        (recur (ffirst seq)))))
