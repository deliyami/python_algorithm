# numpy의 배열 M, 반복 횟수 r, 감쇠율 d
import numpy as np

def page_rank(M, r: int = 100, d: float = 0.85):
    N = M.shape[1] # M은 5*5 구성. N은 5.
    v = np.random.rand(N, 1) # len() == 5짜리 1차원 배열로 반환
    v = v / np.linalg.norm(v, 1)  
    M_hat = (d * M + (1 - d) / N)
    for i in range(r):
        v = M_hat @ v
    return v

M = np.array([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])
v = page_rank(M, 100, 0.85)

print(v)