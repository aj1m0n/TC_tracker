# Generated with SMOP  0.41
from libsmop import *
# associateDetToTrack.m

    
@function
def associateDetToTrack(tracklet_mat=None,road_track=None,max_dist_thresh=None,*args,**kwargs):
    varargin = associateDetToTrack.varargin
    nargin = associateDetToTrack.nargin

    N_road_track=length(road_track)
# associateDetToTrack.m:3
    near_track_mat=cell(1,N_road_track)
# associateDetToTrack.m:4
    for n in arange(1,N_road_track).reshape(-1):
        near_track_mat[n]=dot(- 1,ones(size(tracklet_mat.xmin_mat)))
# associateDetToTrack.m:6
    
    det_idx=find(tracklet_mat.xmin_mat >= logical_and(0,tracklet_mat.xmax_mat) >= logical_and(0,tracklet_mat.ymin_mat) >= logical_and(0,tracklet_mat.ymax_mat) >= 0)
# associateDetToTrack.m:9
    det_pts=concat([dot(0.5,(tracklet_mat.xmin_mat(det_idx) + tracklet_mat.xmax_mat(det_idx))),tracklet_mat.ymax_mat(det_idx)])
# associateDetToTrack.m:11
    for n in arange(1,N_road_track).reshape(-1):
        D=pdist2(det_pts,road_track[n])
# associateDetToTrack.m:15
        min_dist,min_idx=min(D,[],2,nargout=2)
# associateDetToTrack.m:16
        near_track_mat[n][det_idx(min_dist < max_dist_thresh)]=min_idx(min_dist < max_dist_thresh)
# associateDetToTrack.m:17
    
    # make near_idx non-decreasing
    N_tracklet=size(near_track_mat[1],1)
# associateDetToTrack.m:21
    for n in arange(1,N_road_track).reshape(-1):
        for k in arange(1,N_tracklet).reshape(-1):
            row_mask=near_track_mat[n](k,arange()) > 0
# associateDetToTrack.m:24
            near_idx=near_track_mat[n](k,row_mask)
# associateDetToTrack.m:25
            for kk in arange(2,length(near_idx)).reshape(-1):
                near_idx[kk]=max(near_idx(kk),near_idx(kk - 1))
# associateDetToTrack.m:27
            near_track_mat[n][k,row_mask]=near_idx
# associateDetToTrack.m:29
    