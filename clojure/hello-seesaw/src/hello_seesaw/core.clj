(ns hello-seesaw.core
    (:use seesaw.core))

(defn -main [& args]
  (-> (frame :title "Why swing, why?"
             :on-close :exit
             :content (label :text "Why!"
                             :border 5
                             ))
      pack!
      show!))
