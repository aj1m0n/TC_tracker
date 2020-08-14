# Generated with SMOP  0.41
from libsmop import *
# uniformSample.m

    
@function
def uniformSample(t=None,len_=None,*args,**kwargs):
    varargin = uniformSample.varargin
    nargin = uniformSample.nargin

    if length(t) <= len_:
        t_sample=copy(t)
# uniformSample.m:4
        idx=arange(1,length(t))
# uniformSample.m:5
        return t_sample,idx
    
    t_min=min(t)
# uniformSample.m:8
    t_max=max(t)
# uniformSample.m:9
    idx=round(linspace(1,length(t),len_))
# uniformSample.m:10
    t_sample=t(idx)
# uniformSample.m:11