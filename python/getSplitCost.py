# Generated with SMOP  0.41
from libsmop import *
# getSplitCost.m

    
@function
def getSplitCost(track_id=None,track_cluster=None,track_class=None,tracklet_mat=None,prev_cost=None,cluster_params=None,*args,**kwargs):
    varargin = getSplitCost.varargin
    nargin = getSplitCost.nargin

    new_cluster_cost=zeros(2,5)
# getSplitCost.m:5
    if length(track_cluster[track_class(track_id)]) == 1:
        cost=copy(Inf)
# getSplitCost.m:7
        diff_cost=copy(Inf)
# getSplitCost.m:8
        new_cluster_cost=[]
# getSplitCost.m:9
        new_cluster_set=[]
# getSplitCost.m:10
        change_cluster_idx=[]
# getSplitCost.m:11
        f=[]
# getSplitCost.m:12
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    change_cluster_idx=concat([length(track_cluster) + 1,track_class(track_id)])
# getSplitCost.m:16
    new_cluster_set=cell(1,2)
# getSplitCost.m:17
    new_cluster_set[1]=track_id
# getSplitCost.m:18
    remain_tracks=track_cluster[track_class(track_id)]
# getSplitCost.m:19
    remain_tracks[remain_tracks == track_id]=[]
# getSplitCost.m:20
    new_cluster_set[2]=remain_tracks
# getSplitCost.m:21
    # get cost
    new_cluster_cost[1,arange()]=combCost(new_cluster_set[1],tracklet_mat,cluster_params)
# getSplitCost.m:24
    if logical_not(isempty(new_cluster_set[2])):
        new_cluster_cost[2,arange()]=combCost(new_cluster_set[2],tracklet_mat,cluster_params)
# getSplitCost.m:27
    
    cost=sum(new_cluster_cost)
# getSplitCost.m:30
    f=cost - prev_cost
# getSplitCost.m:31
    diff_cost=dot(f,concat([cluster_params.lambda_split,cluster_params.lambda_reg,cluster_params.lambda_color,cluster_params.lambda_grad,cluster_params.lambda_time]).T)
# getSplitCost.m:32