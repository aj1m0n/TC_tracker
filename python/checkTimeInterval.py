# Generated with SMOP  0.41
from libsmop import *
# checkTimeInterval.m

    
@function
def checkTimeInterval(tracklet_mat=None,*args,**kwargs):
    varargin = checkTimeInterval.varargin
    nargin = checkTimeInterval.nargin

    track_interval=tracklet_mat.track_interval
# checkTimeInterval.m:3
    N_tracklet=length(tracklet_mat.track_cluster)
# checkTimeInterval.m:4
    T=zeros(1,N_tracklet)
# checkTimeInterval.m:5
    for n in arange(1,N_tracklet).reshape(-1):
        if isempty(tracklet_mat.track_cluster[n]):
            continue
        temp_interval=track_interval(tracklet_mat.track_cluster[n],arange())
# checkTimeInterval.m:10
        t_min=min(temp_interval(arange(),1))
# checkTimeInterval.m:11
        t_max=max(temp_interval(arange(),2))
# checkTimeInterval.m:12
        T[n]=t_max - t_min + 1
# checkTimeInterval.m:13
    