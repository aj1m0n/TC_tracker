# Generated with SMOP  0.41
from libsmop import *
# fileName.m

    
@function
def fileName(idx=None,num_digit=None,*args,**kwargs):
    varargin = fileName.varargin
    nargin = fileName.nargin

    file_name=[]
# fileName.m:3
    for n in arange(1,num_digit).reshape(-1):
        num=10 ** n
# fileName.m:5
        r=idx / num
# fileName.m:6
        if r >= 0.1 and r < 1:
            for m in arange(1,num_digit - n).reshape(-1):
                file_name=concat([file_name,'0'])
# fileName.m:9
            file_name=concat([file_name,num2str(idx)])
# fileName.m:11
    