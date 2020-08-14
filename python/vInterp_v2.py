# Generated with SMOP  0.41
from libsmop import *
# vInterp_v2.m

    
@function
def vInterp_v2(t=None,y=None,y_pred=None,v=None,t_tr=None,y_tr=None,*args,**kwargs):
    varargin = vInterp_v2.varargin
    nargin = vInterp_v2.nargin

    t_test=[]
# vInterp_v2.m:3
    interp_y=[]
# vInterp_v2.m:4
    pred_y=[]
# vInterp_v2.m:5
    t_min=t(1) - 1
# vInterp_v2.m:6
    t_max=t(end()) + 1
# vInterp_v2.m:7
    __,sort_idx=sort(t_tr,'ascend',nargout=2)
# vInterp_v2.m:8
    t_tr=t_tr(sort_idx)
# vInterp_v2.m:9
    y_tr=y_tr(sort_idx)
# vInterp_v2.m:10
    t_tr_add=copy(t_tr)
# vInterp_v2.m:11
    t_tr_add=concat([t_min,t_tr_add])
# vInterp_v2.m:12
    t_tr_add=concat([t_tr_add,t_max])
# vInterp_v2.m:13
    change_flag=double(t_tr_add(arange(2,end())) - t_tr_add(arange(1,end() - 1)) > 1.5)
# vInterp_v2.m:15
    change_idx=find(change_flag > 0.5)
# vInterp_v2.m:16
    for n in arange(1,length(change_idx)).reshape(-1):
        t_start=t_tr_add(change_idx(n))
# vInterp_v2.m:18
        t_end=t_tr_add(change_idx(n) + 1)
# vInterp_v2.m:19
        v1=v(t_start - t_min + 1)
# vInterp_v2.m:20
        v2=v(t_end - t_min + 2)
# vInterp_v2.m:21
        delta_t=t_end - t_start
# vInterp_v2.m:22
        v_interp=linspace(v1,v2,delta_t + 2)
# vInterp_v2.m:23
        temp_interp_y=cumsum(concat([0,v_interp(arange(2,end() - 1))]))
# vInterp_v2.m:24
        if ismember(t_start,t):
            y1=y(t == t_start)
# vInterp_v2.m:26
        else:
            y1=y_pred(t_start - t_min + 1)
# vInterp_v2.m:28
        if ismember(t_end,t):
            y2=y(t == t_end)
# vInterp_v2.m:31
        else:
            y2=y_pred(t_end - t_min + 1)
# vInterp_v2.m:33
        y_shift=(temp_interp_y(1) - y1 + temp_interp_y(end()) - y2) / 2
# vInterp_v2.m:35
        temp_interp_y=temp_interp_y - y_shift
# vInterp_v2.m:36
        t_test=concat([t_test,arange(t_start + 1,t_end - 1)])
# vInterp_v2.m:38
        interp_y=concat([interp_y,temp_interp_y(arange(2,end() - 1))])
# vInterp_v2.m:39
    
    for n in arange(1,length(t_test)).reshape(-1):
        if ismember(t_test(n),t):
            pred_y=concat([pred_y,y(t == t_test(n))])
# vInterp_v2.m:44
        else:
            pred_y=concat([pred_y,y_pred(t_test(n) - t_min + 1)])
# vInterp_v2.m:46
    