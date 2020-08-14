# Generated with SMOP  0.41
from libsmop import *
# sameCheck.m

    
@function
def sameCheck(struct1=None,struct2=None,*args,**kwargs):
    varargin = sameCheck.varargin
    nargin = sameCheck.nargin

    if length(struct1) != length(struct2):
        flag=0
# sameCheck.m:4
        return flag
    
    for n in arange(1,length(struct1)).reshape(-1):
        temp_flag=isequal(struct1[n],struct2[n])
# sameCheck.m:8
        if logical_not(temp_flag):
            flag=0
# sameCheck.m:10
            return flag
    
    flag=1
# sameCheck.m:14