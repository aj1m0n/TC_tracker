# Generated with SMOP  0.41
from libsmop import *
# getAssignCost.m

    
@function
def getAssignCost(track_id=None,tracklet_mat=None,track_interval=None,track_cluster=None,track_class=None,neighbor_track_idx=None,prev_cluster_cost=None,cluster_params=None,cluster_flag=None,*args,**kwargs):
    varargin = getAssignCost.varargin
    nargin = getAssignCost.nargin

    intersect_ratio_thresh=cluster_params.intersect_ratio_thresh
# getAssignCost.m:6
    cluster1=track_cluster[track_class(track_id)]
# getAssignCost.m:8
    new_cluster_cost=zeros(2,5)
# getAssignCost.m:9
    new_cluster_set=cell(1,2)
# getAssignCost.m:10
    new_cluster_set[1]=cluster1
# getAssignCost.m:11
    new_cluster_set[1][new_cluster_set[1] == track_id]=[]
# getAssignCost.m:12
    # get cost
    if logical_not(isempty(new_cluster_set[1])):
        new_cluster_cost[1,arange()]=combCost(new_cluster_set[1],tracklet_mat,cluster_params)
# getAssignCost.m:16
    
    N_cluster=length(track_cluster)
# getAssignCost.m:19
    if isempty(cluster_flag):
        N_cand=length(track_cluster)
# getAssignCost.m:21
    else:
        N_cand=round(sum(cluster_flag))
# getAssignCost.m:23
    
    temp_new_cluster_cost=dot(Inf,ones(N_cluster,5))
# getAssignCost.m:25
    prev_cost_vec=zeros(N_cluster,5)
# getAssignCost.m:26
    for n in arange(1,N_cand).reshape(-1):
        # the original cluster
        if track_class(track_id) == n:
            continue
        # no neighbor track
        neighbor_track=intersect(neighbor_track_idx[track_id],track_cluster[n])
# getAssignCost.m:34
        if isempty(neighbor_track):
            continue
        # check overlap
        cluster_size=length(track_cluster[n])
# getAssignCost.m:40
        if cluster_size == 0:
            continue
        for k in arange(1,cluster_size).reshape(-1):
            overlap_ratio=overlapCheck(track_interval(track_cluster[n](k),arange()),track_interval(track_id,arange()))
# getAssignCost.m:45
            if overlap_ratio > intersect_ratio_thresh:
                break
        if overlap_ratio > intersect_ratio_thresh:
            continue
        # get cost
        temp_set=concat([track_id,track_cluster[n]])
# getAssignCost.m:55
        temp_new_cluster_cost[n,arange()]=combCost(temp_set,tracklet_mat,cluster_params)
# getAssignCost.m:56
        prev_cost_vec[n,arange()]=prev_cluster_cost(track_class(track_id),arange()) + prev_cluster_cost(n,arange())
# getAssignCost.m:57
    
    cost_vec=bsxfun(plus,temp_new_cluster_cost,new_cluster_cost(1,arange()))
# getAssignCost.m:59
    diff_cost_vec=dot((cost_vec - prev_cost_vec),concat([cluster_params.lambda_split,cluster_params.lambda_reg,cluster_params.lambda_color,cluster_params.lambda_grad,cluster_params.lambda_time]).T)
# getAssignCost.m:60
    __,min_idx=min(diff_cost_vec,nargout=2)
# getAssignCost.m:62
    cost=cost_vec(min_idx)
# getAssignCost.m:63
    if cost == Inf:
        diff_cost=copy(Inf)
# getAssignCost.m:65
        new_cluster_cost=[]
# getAssignCost.m:66
        new_cluster_set=[]
# getAssignCost.m:67
        change_cluster_idx=[]
# getAssignCost.m:68
        f=[]
# getAssignCost.m:69
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    diff_cost=diff_cost_vec(min_idx)
# getAssignCost.m:72
    f=cost_vec(min_idx,arange()) - prev_cost_vec(min_idx,arange())
# getAssignCost.m:73
    new_cluster_cost[2,arange()]=temp_new_cluster_cost(min_idx,arange())
# getAssignCost.m:74
    change_cluster_idx=concat([track_class(track_id),min_idx])
# getAssignCost.m:76
    new_cluster_set[2]=concat([track_id,track_cluster[min_idx]])
# getAssignCost.m:77