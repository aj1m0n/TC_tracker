# Generated with SMOP  0.41
from libsmop import *
# trackletClusterInit.m

    
@function
def trackletClusterInit(tracklet_mat=None,param=None,*args,**kwargs):
    varargin = trackletClusterInit.varargin
    nargin = trackletClusterInit.nargin

    cluster_params.t_dist_thresh = copy(20)
# trackletClusterInit.m:3
    cluster_params.lambda_time = copy(param.lambda_time)
# trackletClusterInit.m:4
    cluster_params.intersect_ratio_thresh = copy(0.2)
# trackletClusterInit.m:5
    cluster_params.len_tracklet_thresh = copy(2)
# trackletClusterInit.m:6
    cluster_params.lambda_split = copy(param.lambda_split)
# trackletClusterInit.m:7
    cluster_params.small_track_cost = copy(0.1)
# trackletClusterInit.m:8
    cluster_params.sigma = copy(8)
# trackletClusterInit.m:9
    cluster_params.track_len = copy(25)
# trackletClusterInit.m:10
    cluster_params.lambda_reg = copy(param.lambda_reg)
# trackletClusterInit.m:11
    cluster_params.lambda_color = copy(param.lambda_color)
# trackletClusterInit.m:12
    cluster_params.color_sample_size = copy(5)
# trackletClusterInit.m:13
    cluster_params.lambda_grad = copy(param.lambda_grad)
# trackletClusterInit.m:14
    new_tracklet_mat=copy(tracklet_mat)
# trackletClusterInit.m:16
    if logical_not(isfield(new_tracklet_mat,'cluster_params')):
        new_tracklet_mat.cluster_params = copy(cluster_params)
# trackletClusterInit.m:19
    
    if logical_not(isfield(new_tracklet_mat,'track_interval')):
        new_tracklet_mat.track_interval = copy(getTrackInterval(new_tracklet_mat))
# trackletClusterInit.m:23
    
    if logical_not(isfield(new_tracklet_mat,'track_class')):
        new_tracklet_mat.track_class = copy(round(cumsum(new_tracklet_mat.mask_flag)))
# trackletClusterInit.m:27
        new_tracklet_mat.track_class[new_tracklet_mat.mask_flag < 0.5]=- 1
# trackletClusterInit.m:28
    
    if logical_not(isfield(new_tracklet_mat,'track_cluster')):
        N_cluster=max(new_tracklet_mat.track_class)
# trackletClusterInit.m:32
        new_tracklet_mat.track_cluster = copy(cell(1,N_cluster))
# trackletClusterInit.m:33
        for n in arange(1,N_cluster).reshape(-1):
            new_tracklet_mat.track_cluster[n]=find(new_tracklet_mat.track_class == n,1)
# trackletClusterInit.m:35
    
    if logical_not(isfield(new_tracklet_mat,'neighbor_track_idx')):
        new_tracklet_mat.neighbor_track_idx = copy(getNeighborTrack(new_tracklet_mat.track_interval,cluster_params.t_dist_thresh,cluster_params.intersect_ratio_thresh))
# trackletClusterInit.m:40
    
    if logical_not(isfield(new_tracklet_mat,'det_x')) or logical_not(isfield(new_tracklet_mat,'det_y')):
        new_tracklet_mat=bboxToPoint(new_tracklet_mat)
# trackletClusterInit.m:45
    
    if logical_not(isfield(new_tracklet_mat,'cluster_cost')):
        N_cluster=max(new_tracklet_mat.track_class)
# trackletClusterInit.m:49
        new_tracklet_mat.cluster_cost = copy(zeros(N_cluster,5))
# trackletClusterInit.m:50
        new_tracklet_mat.cluster_cost[arange(),1]=1
# trackletClusterInit.m:51
    
    if logical_not(isfield(new_tracklet_mat,'f_mat')):
        new_tracklet_mat.f_mat = copy(zeros(1000,6))
# trackletClusterInit.m:55
    
    if logical_not(isfield(new_tracklet_mat,'track_change_set')):
        new_tracklet_mat.track_change_set = copy([])
# trackletClusterInit.m:59
    
    prev_track_cluster=new_tracklet_mat.track_cluster
# trackletClusterInit.m:62
    new_tracklet_mat.track_cluster,new_tracklet_mat.track_class,new_tracklet_mat.cluster_cost,new_tracklet_mat.f_mat,new_tracklet_mat.track_change_set=trackletCluster(new_tracklet_mat,new_tracklet_mat.track_interval,new_tracklet_mat.track_cluster,new_tracklet_mat.track_class,new_tracklet_mat.cluster_cost,new_tracklet_mat.neighbor_track_idx,cluster_params,new_tracklet_mat.f_mat,new_tracklet_mat.track_change_set,nargout=5)
# trackletClusterInit.m:64
    flag=sameCheck(prev_track_cluster,new_tracklet_mat.track_cluster)
# trackletClusterInit.m:69
    cnt=0
# trackletClusterInit.m:71
    for n in arange(1,length(new_tracklet_mat.track_cluster)).reshape(-1):
        if length(new_tracklet_mat.track_cluster[n]) >= 1:
            cnt=cnt + 1
# trackletClusterInit.m:74
    