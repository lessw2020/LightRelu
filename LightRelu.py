import torch  #need torch.tanh
import torch.nn as nn

class LightRelu(nn.Module):
    #.46 was found to shift the mean to 0 on a random distribution test
    # maxv of 7.5 was from initial testing on MNIST.  
    #Important - cut your learning rates in half with this...
    
    def __init__(self,sub=.46,maxv=7.5):
        super().__init__()
        self.sub=sub
        self.maxv=maxv
    
    def forward(self,x):
        #change to lisht
        
        x = x *torch.tanh(x)
        
        if self.sub is not None:
            x.sub_(self.sub)
        if self.maxv is not None: 
            x.clamp_max_(self.maxv)
        return x
