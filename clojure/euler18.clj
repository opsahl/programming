(defn read-from-file-safely [filename]
  (with-open
    [r (java.io.PushbackReader.
         (clojure.java.io/reader filename))]
      (binding [*read-eval* false]
        (read r))))

(defn get-pairs ([in-list] (get-pairs in-list '())) 
  ([in-list new-list]
  (if (= 1 (count in-list))
    (reverse new-list) 
    (recur (rest in-list) (cons (cons (first in-list) (list (second in-list))) new-list)))))
    
    
    ;(cons (cons (first in-list) (list (second in-list))) (get-pairs (rest in-list)))))

(defn reduce-line [in-list]
  (doall (map #(reduce max %) (get-pairs in-list)))) 

(defn add-lists [list1 list2]
  (doall (map + list1 list2)))

(defn reduce-triangle [triangle]
  (if (= 1 (count triangle))
    (first triangle)
    (recur (conj (butlast (butlast triangle)) (add-lists (last (butlast triangle)) (reduce-line (last triangle)))))))

(defn solve [filename]
(let [triangle (read-from-file-safely filename)]
    (reduce-triangle triangle)))

(solve "euler18.txt")
