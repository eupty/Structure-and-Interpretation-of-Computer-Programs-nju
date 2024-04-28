;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
        (if (f (car s))
            (cons-stream (car s) (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s)))))


(define (slice s start end)
  (define (slice-nest s start end lst)
    (if (null? s)
      lst
      (cond ((and (= start 0) (> end 0) (not (null? s))) (slice-nest (cdr-stream s) start (- end 1) (append lst (list (car s)))))
        ((and (= start 0) (= end 0)) lst)
        ((> start 0) (slice-nest (cdr-stream s) (- start 1) (- end 1) lst))
        ((null? s) lst))
      ))
  (slice-nest s start end nil)
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)

(define (fib x y) (cons-stream x (fib y (+ x y))))
(define fibs
  (fib 0 1)
)


(define (exp x)
  (begin (define help (combine-with (lambda (a b) (/ (expt x a) b)) (cdr-stream (naturals 0)) (cdr-stream factorials)))
  (cons-stream 1 (combine-with + help (exp x)))))


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (cond ((null? s) nil)
    ((null? (cdr-stream s)) (list-to-stream (cons (list (car s)) nil)))
    ((> (car s) (car (cdr-stream s))) (cons-stream (list (car s)) (nondecrease (cdr-stream s))))
    ((<= (car s) (car (cdr-stream s))) (cons-stream (cons (car s) (car (nondecrease (cdr-stream s)))) (cdr-stream (nondecrease (cdr-stream s))))))
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
