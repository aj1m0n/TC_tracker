# Generated with SMOP  0.41
from libsmop import *
# min_mat.m

    
@function
def min_mat(A=None,*args,**kwargs):
    varargin = min_mat.varargin
    nargin = min_mat.nargin

    if size(A,1) > 1 and size(A,2) > 1:
        v1,idx1=min(A,nargout=2)
# min_mat.m:4
        v2,idx2=min(v1,nargout=2)
# min_mat.m:5
        idx=concat([idx1(idx2),idx2])
# min_mat.m:6
        min_v=copy(v2)
# min_mat.m:7
    else:
        if size(A,1) == 1:
            min_v,idx2=min(A,nargout=2)
# min_mat.m:9
            idx=concat([1,idx2])
# min_mat.m:10
        else:
            if size(A,2) == 1:
                min_v,idx1=min(A,nargout=2)
# min_mat.m:12
                idx=concat([idx1,1])
# min_mat.m:13
    