# Generated with SMOP  0.41
from libsmop import *
# max_mat.m

    
@function
def max_mat(A=None,*args,**kwargs):
    varargin = max_mat.varargin
    nargin = max_mat.nargin

    if size(A,1) > 1 and size(A,2) > 1:
        v1,idx1=max(A,nargout=2)
# max_mat.m:4
        v2,idx2=max(v1,nargout=2)
# max_mat.m:5
        idx=concat([idx1(idx2),idx2])
# max_mat.m:6
        max_v=copy(v2)
# max_mat.m:7
    else:
        if size(A,1) == 1:
            max_v,idx2=max(A,nargout=2)
# max_mat.m:9
            idx=concat([1,idx2])
# max_mat.m:10
        else:
            if size(A,2) == 1:
                max_v,idx1=max(A,nargout=2)
# max_mat.m:12
                idx=concat([idx1,1])
# max_mat.m:13
    