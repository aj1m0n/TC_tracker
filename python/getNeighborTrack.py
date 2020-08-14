# Generated with SMOP  0.41
from libsmop import *
# getNeighborTrack.m

    
@function
def getNeighborTrack(track_interval=None,t_dist_thresh=None,intersect_ratio=None,*args,**kwargs):
    varargin = getNeighborTrack.varargin
    nargin = getNeighborTrack.nargin

    N_tracklet=size(track_interval,1)
# getNeighborTrack.m:3
    neighbor_idx=cell(1,N_tracklet)
# getNeighborTrack.m:4
    for n in arange(1,N_tracklet).reshape(-1):
        cand_idx=find(track_interval(n,1) - track_interval(arange(),2) < logical_and(t_dist_thresh,track_interval(arange(),1) - track_interval(n,2)) < t_dist_thresh)
# getNeighborTrack.m:6
        if isempty(cand_idx):
            continue
        remove_idx=[]
# getNeighborTrack.m:10
        vec_idx1=arange(track_interval(n,1),track_interval(n,2))
# getNeighborTrack.m:11
        for k in arange(1,length(cand_idx)).reshape(-1):
            vec_idx2=arange(track_interval(cand_idx(k),1),track_interval(cand_idx(k),2))
# getNeighborTrack.m:13
            vec_idx3=intersect(vec_idx1,vec_idx2)
# getNeighborTrack.m:14
            if length(vec_idx3) / min(length(vec_idx1),length(vec_idx3)) > intersect_ratio:
                remove_idx=concat([remove_idx,k])
# getNeighborTrack.m:16
        cand_idx[remove_idx]=[]
# getNeighborTrack.m:19
        if isempty(cand_idx):
            continue
        neighbor_idx[n]=cand_idx
# getNeighborTrack.m:23
    