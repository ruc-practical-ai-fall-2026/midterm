# Run this script to ensure that you can import required libraries to take
# the exam.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import torch
import torchvision
import sklearn
import pandas as pd
import seaborn as sns
import scipy
from exam.my_module import hello

print(np.__version__)
print(matplotlib.__version__)
print(torch.__version__)
print(torchvision.__version__)
print(sklearn.__version__)
print(pd.__version__)
print(sns.__version__)
print(scipy.__version__)

hello()