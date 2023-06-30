import torch
import numpy as np

test = np.array([
                [1,2,3],
                [4,5,6]
                ])

if __name__ == '__main__':
    t = torch.tensor(test)

    print(torch.max(t))

