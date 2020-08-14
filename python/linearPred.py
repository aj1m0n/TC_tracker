# Generated with SMOP  0.41
from libsmop import *
# linearPred.m

    
@function
def linearPred(train_t=None,train_x=None,t=None,*args,**kwargs):
    varargin = linearPred.varargin
    nargin = linearPred.nargin

    if length(train_t) <= 2:
        pred_x=train_x(end())
# linearPred.m:4
        return pred_x
    
    A=concat([train_t.T,ones(size(train_t.T))])
# linearPred.m:8
    b=train_x.T
# linearPred.m:9
    p=dot(pinv(A),b)
# linearPred.m:10
    pred_x=dot(p(1),t) + p(2)
# linearPred.m:11