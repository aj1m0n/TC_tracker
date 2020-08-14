# Generated with SMOP  0.41
from libsmop import *
# getBreakCost.m

    
@function
def getBreakCost(track_id=None,track_cluster=None,track_class=None,tracklet_mat=None,prev_cost=None,cluster_params=None,*args,**kwargs):
    varargin = getBreakCost.varargin
    nargin = getBreakCost.nargin

    new_cluster_cost=zeros(2,5)
# getBreakCost.m:5
    if length(track_cluster[track_class(track_id)]) <= 2:
        cost=copy(Inf)
# getBreakCost.m:7
        diff_cost=copy(Inf)
# getBreakCost.m:8
        new_cluster_cost=[]
# getBreakCost.m:9
        new_cluster_set=[]
# getBreakCost.m:10
        change_cluster_idx=[]
# getBreakCost.m:11
        f=[]
# getBreakCost.m:12
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    # get cost
    track_ids=track_cluster[track_class(track_id)]
# getBreakCost.m:17
    track_interval=tracklet_mat.track_interval
# getBreakCost.m:18
    after_ids=track_ids(track_interval(track_ids,2) > track_interval(track_id,2))
# getBreakCost.m:19
    if isempty(after_ids):
        cost=copy(Inf)
# getBreakCost.m:21
        diff_cost=copy(Inf)
# getBreakCost.m:22
        new_cluster_cost=[]
# getBreakCost.m:23
        new_cluster_set=[]
# getBreakCost.m:24
        change_cluster_idx=[]
# getBreakCost.m:25
        f=[]
# getBreakCost.m:26
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    else:
        before_ids=setdiff(track_ids,after_ids)
# getBreakCost.m:29
        if length(before_ids) <= 1:
            cost=copy(Inf)
# getBreakCost.m:31
            diff_cost=copy(Inf)
# getBreakCost.m:32
            new_cluster_cost=[]
# getBreakCost.m:33
            new_cluster_set=[]
# getBreakCost.m:34
            change_cluster_idx=[]
# getBreakCost.m:35
            f=[]
# getBreakCost.m:36
            return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
        change_cluster_idx=concat([length(track_cluster) + 1,track_class(track_id)])
# getBreakCost.m:39
        new_cluster_set=cell(1,2)
# getBreakCost.m:40
        new_cluster_set[1]=before_ids
# getBreakCost.m:41
        remain_tracks=copy(after_ids)
# getBreakCost.m:42
        new_cluster_set[2]=remain_tracks
# getBreakCost.m:43
        new_cluster_cost[1,arange()]=combCost(new_cluster_set[1],tracklet_mat,cluster_params)
# getBreakCost.m:44
        new_cluster_cost[2,arange()]=combCost(new_cluster_set[2],tracklet_mat,cluster_params)
# getBreakCost.m:45
        cost=sum(new_cluster_cost)
# getBreakCost.m:46
        f=cost - prev_cost
# getBreakCost.m:47
        diff_cost=dot(f,concat([cluster_params.lambda_split,cluster_params.lambda_reg,cluster_params.lambda_color,cluster_params.lambda_grad,cluster_params.lambda_time]).T)
# getBreakCost.m:48
    