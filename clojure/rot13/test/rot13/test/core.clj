(ns rot13.test.core
  (:use [rot13.core])
  (:use [clojure.test]))

(deftest rot-13-abc
         (is (= "nop" (encode "abc"))) "abc doesn't equal nop")

;(deftest replace-me ;; FIXME: write
;  (is false "No tests have been written."))
