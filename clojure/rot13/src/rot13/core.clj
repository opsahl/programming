(ns rot13.core
    (:require [clojure.string :as cls]))

(defn wrap-around [number]
  (if (> number 122) 
    (- number 26)
    number))

(defn add13 [number]
  (+ 13 number))

(defn encode-char [in-char]
  (-> in-char
      Character/toLowerCase
      int 
      add13
      wrap-around
      char))

(defn encode [in-string]
  (apply str (map encode-char in-string)))

(defn -main [& args]
  (println (cls/join " " (map encode args))))
