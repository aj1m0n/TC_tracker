# Generated with SMOP  0.41
from libsmop import *
# getMergeCost.m

    
@function
def getMergeCost(track_id=None,tracklet_mat=None,track_interval=None,track_cluster=None,track_class=None,neighbor_track_idx=None,prev_cluster_cost=None,cluster_params=None,*args,**kwargs):
    varargin = getMergeCost.varargin
    nargin = getMergeCost.nargin

    intersect_ratio_thresh=cluster_params.intersect_ratio_thresh
# getMergeCost.m:6
    cluster1=track_cluster[track_class(track_id)]
# getMergeCost.m:8
    if length(cluster1) == 1:
        cost=copy(Inf)
# getMergeCost.m:10
        diff_cost=copy(Inf)
# getMergeCost.m:11
        new_cluster_cost=[]
# getMergeCost.m:12
        new_cluster_set=[]
# getMergeCost.m:13
        change_cluster_idx=[]
# getMergeCost.m:14
        f=[]
# getMergeCost.m:15
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    N_cluster=length(track_cluster)
# getMergeCost.m:19
    new_cluster_cost_vec=dot(Inf,ones(N_cluster,5))
# getMergeCost.m:20
    prev_cost_vec=zeros(N_cluster,5)
# getMergeCost.m:21
    for n in arange(1,N_cluster).reshape(-1):
        # the original cluster
        if track_class(track_id) == n:
            continue
        # no neighbor track
        neighbor_track=intersect(neighbor_track_idx[track_id],track_cluster[n])
# getMergeCost.m:29
        if isempty(neighbor_track):
            continue
        # check overlap
        cluster_size=length(track_cluster[n])
# getMergeCost.m:35
        if cluster_size == 0:
            continue
        for k1 in arange(1,length(cluster1)).reshape(-1):
            for k2 in arange(1,cluster_size).reshape(-1):
                overlap_ratio=overlapCheck(track_interval(track_cluster[n](k2),arange()),track_interval(cluster1(k1),arange()))
# getMergeCost.m:41
                if overlap_ratio > intersect_ratio_thresh:
                    break
            if overlap_ratio > intersect_ratio_thresh:
                break
        if overlap_ratio > intersect_ratio_thresh:
            continue
        # get cost
        new_cluster_cost_vec[n,arange()]=combCost(concat([cluster1,track_cluster[n]]),tracklet_mat,cluster_params)
# getMergeCost.m:55
        prev_cost_vec[n,arange()]=prev_cluster_cost(track_class(track_id),arange()) + prev_cluster_cost(n,arange())
# getMergeCost.m:56
    
    diff_cost_vec=dot((new_cluster_cost_vec - prev_cost_vec),concat([cluster_params.lambda_split,cluster_params.lambda_reg,cluster_params.lambda_color,cluster_params.lambda_grad,cluster_params.lambda_time]).T)
# getMergeCost.m:59
    __,min_idx=min(diff_cost_vec,nargout=2)
# getMergeCost.m:61
    cost=new_cluster_cost_vec(min_idx,arange())
# getMergeCost.m:62
    if cost == Inf:
        diff_cost=copy(Inf)
# getMergeCost.m:64
        new_cluster_cost=[]
# getMergeCost.m:65
        new_cluster_set=[]
# getMergeCost.m:66
        change_cluster_idx=[]
# getMergeCost.m:67
        f=[]
# getMergeCost.m:68
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    diff_cost=diff_cost_vec(min_idx)
# getMergeCost.m:71
    f=new_cluster_cost_vec(min_idx,arange()) - prev_cost_vec(min_idx,arange())
# getMergeCost.m:72
    new_cluster_cost=zeros(2,5)
# getMergeCost.m:73
    new_cluster_cost[1,arange()]=cost
# getMergeCost.m:74
    change_cluster_idx=concat([track_class(track_id),min_idx])
# getMergeCost.m:76
    new_cluster_set=cell(1,2)
# getMergeCost.m:77
    new_cluster_set[1]=concat([cluster1,track_cluster[min_idx]])
# getMergeCost.m:78