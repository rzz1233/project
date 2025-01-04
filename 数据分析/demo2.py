import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.use("TkAgg")

res = plt.imread("./1.jpg")
# print(res.shape)
# print(res)
# res = res[::-1,::-1]
res =res[170:320,250:350]
res = np.concatenate((res,res),axis=0) #级联(列)

res2 = res[:,::-1]
plt.imshow(np.concatenate((res,res2),axis=1)) #级联（行)
plt.show()
# plt.savefig("./1.svg")
