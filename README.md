# LightRelu
Customized PyTorch implementation of LiSHT (linear scaled hyperbolic tangent) activation function for deep learning

Original paper here:
https://arxiv.org/abs/1901.05894

I implemented using Pytorch and wrapped it with a clamp and mean shift.  (.46 and 7.5).  
More testing in progress, but so far looks very promising!  
Note - cut your learning rates in half vs ReLU, it learns very rapidly.
