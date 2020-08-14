# Generated with SMOP  0.41
from libsmop import *
# trackFit.m

    
@function
def trackFit(tracklet_mat=None,road_track=None,max_dist_thresh=None,*args,**kwargs):
    varargin = trackFit.varargin
    nargin = trackFit.nargin

    N_road_track=length(road_track)
# trackFit.m:3
    near_track_mat=associateDetToTrack(tracklet_mat,road_track,max_dist_thresh)
# trackFit.m:4
    N_tracklet=size(near_track_mat[1],1)
# trackFit.m:5
    mask=tracklet_mat.xmin_mat >= 0
# trackFit.m:7
    tracklet_center_x=zeros(size(mask))
# trackFit.m:8
    tracklet_center_y=zeros(size(mask))
# trackFit.m:9
    tracklet_center_x[mask]=dot(0.5,(tracklet_mat.xmin_mat(mask) + tracklet_mat.xmax_mat(mask)))
# trackFit.m:10
    tracklet_center_y[mask]=tracklet_mat.ymax_mat(mask)
# trackFit.m:11
    Dx=cell(1,N_road_track)
# trackFit.m:12
    Dy=cell(1,N_road_track)
# trackFit.m:13
    fit_cost=dot(- 1,ones(N_tracklet,N_road_track))
# trackFit.m:14
    for n in arange(1,N_road_track).reshape(-1):
        temp_mask=near_track_mat[n] > 0
# trackFit.m:16
        track_fr_num=sum(temp_mask,2)
# trackFit.m:17
        cand_idx=track_fr_num > 0
# trackFit.m:18
        Dx[n]=zeros(size(near_track_mat[n]))
# trackFit.m:20
        Dy[n]=zeros(size(near_track_mat[n]))
# trackFit.m:21
        Dx[n][temp_mask]=tracklet_center_x(temp_mask) - road_track[n](near_track_mat[n](temp_mask),1)
# trackFit.m:22
        Dy[n][temp_mask]=tracklet_center_y(temp_mask) - road_track[n](near_track_mat[n](temp_mask),2)
# trackFit.m:23
        mean_x=sum(Dx[n](cand_idx,arange()),2) / track_fr_num(cand_idx)
# trackFit.m:25
        mean_y=sum(Dy[n](cand_idx,arange()),2) / track_fr_num(cand_idx)
# trackFit.m:26
        mean_x=min(max(mean_x,- 100),100)
# trackFit.m:27
        mean_y=min(max(mean_y,- 100),100)
# trackFit.m:28
        Dx[n][cand_idx,arange()]=bsxfun(minus,Dx[n](cand_idx,arange()),mean_x)
# trackFit.m:29
        Dy[n][cand_idx,arange()]=bsxfun(minus,Dy[n](cand_idx,arange()),mean_y)
# trackFit.m:30
        Dx[n][logical_not(temp_mask)]=0
# trackFit.m:32
        Dy[n][logical_not(temp_mask)]=0
# trackFit.m:33
        fit_cost[cand_idx,n]=sum(sqrt(Dx[n](cand_idx,arange()) ** 2 + Dy[n](cand_idx,arange()) ** 2),2)
# trackFit.m:34
    
    fit_cost[fit_cost < 0]=Inf
# trackFit.m:36