;Finding Nth element of a list

(princ "Finding Nth element of a list")
(terpri)

(princ "Enter N (from 0-9): ")
(setq N (read))
(setq x N)
(defun list-nth (N L)
  "Return the N'th member of a list L."
  (if (null L)
      nil
    (if (zerop N) 
	(first L)
      (list-nth (1- N) (rest L)))))
(format t "(N = ~d)th element is : ~d" x (list-nth x '(2 4 6 8 10 12 14 16 18 20)))

