# Generated with SMOP  0.41
from libsmop import *
# vInterp.m

    
@function
def vInterp(flag_idx=None,change_idx=None,vx_pred=None,t=None,y=None,*args,**kwargs):
    varargin = vInterp.varargin
    nargin = vInterp.nargin

    t_min=t(1) - 1
# vInterp.m:3
    interp_y=[]
# vInterp.m:4
    pred_y=[]
# vInterp.m:5
    t_test=[]
# vInterp.m:6
    for n in arange(1,length(change_idx) - 1).reshape(-1):
        if flag_idx(change_idx(n)) == flag_idx(change_idx(n + 1)):
            continue
        t1=t(change_idx(n))
# vInterp.m:11
        t2=t(change_idx(n + 1))
# vInterp.m:12
        v1=vx_pred(t1 - t_min)
# vInterp.m:13
        v2=vx_pred(t2 - t_min + 1)
# vInterp.m:14
        delta_t=t2 - t1
# vInterp.m:16
        v_interp=linspace(v1,v2,delta_t + 2)
# vInterp.m:17
        temp_interp_y=cumsum(concat([0,v_interp(arange(2,end() - 1))]))
# vInterp.m:18
        temp_pred_y=y(arange(t1 - t_min,t2 - t_min))
# vInterp.m:19
        y_shift=(temp_interp_y(1) - temp_pred_y(1) + temp_interp_y(end()) - temp_pred_y(end())) / 2
# vInterp.m:20
        temp_interp_y=temp_interp_y - y_shift
# vInterp.m:21
        interp_y=concat([interp_y,temp_interp_y])
# vInterp.m:22
        pred_y=concat([pred_y,temp_pred_y.T])
# vInterp.m:23
        t_test=concat([t_test,arange(t1,t2)])
# vInterp.m:24
    