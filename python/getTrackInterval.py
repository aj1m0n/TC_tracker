# Generated with SMOP  0.41
from libsmop import *
# getTrackInterval.m

    
@function
def getTrackInterval(tracklet_mat=None,*args,**kwargs):
    varargin = getTrackInterval.varargin
    nargin = getTrackInterval.nargin

    N_tracklet=size(tracklet_mat.xmin_mat,1)
# getTrackInterval.m:3
    track_interval=zeros(N_tracklet,2)
# getTrackInterval.m:4
    cand_idx=find(tracklet_mat.xmin_mat >= 0)
# getTrackInterval.m:5
    min_mask=dot(Inf,ones(size(tracklet_mat.xmin_mat)))
# getTrackInterval.m:6
    min_mask[cand_idx]=cand_idx
# getTrackInterval.m:7
    min_v,track_interval(arange(),1)=min(min_mask,[],2,nargout=2)
# getTrackInterval.m:8
    track_interval[min_v == Inf,1]=- 1
# getTrackInterval.m:9
    max_mask=dot(- 1,ones(size(tracklet_mat.xmin_mat)))
# getTrackInterval.m:10
    max_mask[cand_idx]=cand_idx
# getTrackInterval.m:11
    max_v,track_interval(arange(),2)=max(max_mask,[],2,nargout=2)
# getTrackInterval.m:12
    track_interval[max_v == 0,2]=- 1
# getTrackInterval.m:13