# Generated with SMOP  0.41
from libsmop import *
# dataGroup.m

    
@function
def dataGroup(t1=None,t2=None,y1=None,y2=None,tr_size=None,*args,**kwargs):
    varargin = dataGroup.varargin
    nargin = dataGroup.nargin

    t_max=max(max(t1),max(t2))
# dataGroup.m:3
    t=arange(1,t_max)
# dataGroup.m:4
    flag_idx=dot(- 1,ones(size(t)))
# dataGroup.m:5
    flag_idx[t1]=1
# dataGroup.m:6
    flag_idx[t2]=2
# dataGroup.m:7
    t=t(flag_idx > 0)
# dataGroup.m:8
    flag_idx=flag_idx(flag_idx > 0)
# dataGroup.m:9
    y=copy(t)
# dataGroup.m:10
    y[flag_idx == 1]=y1
# dataGroup.m:11
    y[flag_idx == 2]=y2
# dataGroup.m:12
    change_flag=zeros(size(flag_idx))
# dataGroup.m:13
    change_flag[arange(1,end() - 1)]=abs(flag_idx(arange(2,end())) - flag_idx(arange(1,end() - 1)))
# dataGroup.m:14
    change_flag[arange(2,end())]=change_flag(arange(2,end())) + change_flag(arange(1,end() - 1))
# dataGroup.m:15
    change_flag=double(change_flag > 0)
# dataGroup.m:16
    change_idx=find(change_flag > 0.5)
# dataGroup.m:17
    # get training data
    if length(t) < tr_size:
        t_tr=t(change_flag < 0.5)
# dataGroup.m:21
        y_tr=y(change_flag < 0.5)
# dataGroup.m:22
    else:
        t_dist=pdist2(t.T,t(change_idx).T)
# dataGroup.m:24
        min_dist=min(t_dist,[],2)
# dataGroup.m:25
        sort_dist,sort_idx=sort(min_dist,'ascend',nargout=2)
# dataGroup.m:26
        sort_idx[sort_dist == 0]=[]
# dataGroup.m:27
        if length(sort_idx) > tr_size:
            t_tr=t(sort_idx(arange(1,tr_size)))
# dataGroup.m:29
            y_tr=y(sort_idx(arange(1,tr_size)))
# dataGroup.m:30
        else:
            t_tr=t(sort_idx)
# dataGroup.m:32
            y_tr=y(sort_idx)
# dataGroup.m:33
    
    t_interval=concat([min(min(t(change_idx)),min(t_tr)),max(max(t(change_idx)),max(t_tr))])
# dataGroup.m:36