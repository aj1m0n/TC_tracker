# Generated with SMOP  0.41
from libsmop import *
# getSwitchCost.m

    
@function
def getSwitchCost(track_id=None,tracklet_mat=None,track_interval=None,track_cluster=None,track_class=None,neighbor_track_idx=None,prev_cluster_cost=None,cluster_params=None,*args,**kwargs):
    varargin = getSwitchCost.varargin
    nargin = getSwitchCost.nargin

    cluster1=track_cluster[track_class(track_id)]
# getSwitchCost.m:6
    S1=[]
# getSwitchCost.m:7
    S2=[]
# getSwitchCost.m:8
    for k in arange(1,length(cluster1)).reshape(-1):
        temp_id=cluster1(k)
# getSwitchCost.m:10
        if track_interval(temp_id,2) <= track_interval(track_id,2):
            S1=concat([S1,temp_id])
# getSwitchCost.m:12
        else:
            S2=concat([S2,temp_id])
# getSwitchCost.m:14
    
    N_cluster=length(track_cluster)
# getSwitchCost.m:19
    cost_vec=dot(Inf,ones(N_cluster,5))
# getSwitchCost.m:20
    prev_cost_vec=zeros(N_cluster,5)
# getSwitchCost.m:21
    new_cluster_cost_vec1=dot(Inf,ones(N_cluster,5))
# getSwitchCost.m:22
    new_cluster_cost_vec2=dot(Inf,ones(N_cluster,5))
# getSwitchCost.m:23
    track_id_set=cell(N_cluster,5)
# getSwitchCost.m:24
    t_max_fr=size(tracklet_mat.xmin_mat,2)
# getSwitchCost.m:25
    for n in arange(1,N_cluster).reshape(-1):
        # swich availability check
        stop_flag=1
# getSwitchCost.m:28
        cluster_size=length(track_cluster[n])
# getSwitchCost.m:29
        if cluster_size == 0:
            continue
        for k in arange(1,cluster_size).reshape(-1):
            if ismember(track_cluster[n](k),neighbor_track_idx[track_id]):
                stop_flag=0
# getSwitchCost.m:35
                break
        if stop_flag == 1:
            continue
        cand_track_invertal=track_interval(track_cluster[n],arange())
# getSwitchCost.m:43
        t_min=min(cand_track_invertal(arange(),1))
# getSwitchCost.m:44
        t_max=max(cand_track_invertal(arange(),2))
# getSwitchCost.m:45
        t_check=dot(- 1,ones(1,t_max_fr))
# getSwitchCost.m:46
        for k in arange(1,cluster_size).reshape(-1):
            t_check[arange(cand_track_invertal(k,1),cand_track_invertal(k,2))]=1
# getSwitchCost.m:48
        if t_check(track_interval(track_id,2)) == 1:
            continue
        ################
#     if (track_interval(track_id,2)<t_min || track_interval(track_id,2)>t_max) 
#         continue
#     end
        # get cost
        S3=[]
# getSwitchCost.m:59
        S4=[]
# getSwitchCost.m:60
        for k in arange(1,cluster_size).reshape(-1):
            temp_id=track_cluster[n](k)
# getSwitchCost.m:63
            if track_interval(temp_id,2) <= track_interval(track_id,2):
                S3=concat([S3,temp_id])
# getSwitchCost.m:65
            else:
                S4=concat([S4,temp_id])
# getSwitchCost.m:67
        S_1=concat([S1,S4])
# getSwitchCost.m:71
        S_2=concat([S3,S2])
# getSwitchCost.m:72
        neighbor_set1=[]
# getSwitchCost.m:74
        for k in arange(1,length(S1)).reshape(-1):
            neighbor_set1=concat([[neighbor_set1],[neighbor_track_idx[S1(k)]]])
# getSwitchCost.m:76
        neighbor_set1=unique(neighbor_set1)
# getSwitchCost.m:78
        if isempty(intersect(neighbor_set1,S4.T)):
            continue
        neighbor_set2=[]
# getSwitchCost.m:83
        for k in arange(1,length(S3)).reshape(-1):
            neighbor_set2=concat([[neighbor_set2],[neighbor_track_idx[S3(k)]]])
# getSwitchCost.m:85
        neighbor_set2=unique(neighbor_set2)
# getSwitchCost.m:87
        if isempty(intersect(neighbor_set2,S2.T)):
            continue
        new_cluster_cost_vec1[n,arange()]=combCost(S_1,tracklet_mat,cluster_params)
# getSwitchCost.m:93
        new_cluster_cost_vec2[n,arange()]=combCost(S_2,tracklet_mat,cluster_params)
# getSwitchCost.m:94
        cost_vec[n,arange()]=new_cluster_cost_vec1(n,arange()) + new_cluster_cost_vec2(n,arange())
# getSwitchCost.m:95
        track_id_set[n]=cell(1,2)
# getSwitchCost.m:97
        track_id_set[n][1]=S_1
# getSwitchCost.m:98
        track_id_set[n][2]=S_2
# getSwitchCost.m:99
        prev_cost_vec[n,arange()]=prev_cluster_cost(track_class(track_id),arange()) + prev_cluster_cost(n,arange())
# getSwitchCost.m:101
    
    diff_cost_vec=dot((cost_vec - prev_cost_vec),concat([cluster_params.lambda_split,cluster_params.lambda_reg,cluster_params.lambda_color,cluster_params.lambda_grad,cluster_params.lambda_time]).T)
# getSwitchCost.m:104
    __,min_idx=min(diff_cost_vec,nargout=2)
# getSwitchCost.m:106
    f=cost_vec(min_idx,arange()) - prev_cost_vec(min_idx,arange())
# getSwitchCost.m:107
    cost=cost_vec(min_idx)
# getSwitchCost.m:108
    if cost == Inf:
        diff_cost=copy(Inf)
# getSwitchCost.m:110
        new_cluster_cost=[]
# getSwitchCost.m:111
        new_cluster_set=[]
# getSwitchCost.m:112
        change_cluster_idx=[]
# getSwitchCost.m:113
        f=[]
# getSwitchCost.m:114
        return cost,diff_cost,new_cluster_cost,new_cluster_set,change_cluster_idx,f
    
    diff_cost=diff_cost_vec(min_idx)
# getSwitchCost.m:117
    new_cluster_cost=zeros(2,5)
# getSwitchCost.m:118
    new_cluster_cost[1,arange()]=new_cluster_cost_vec1(min_idx,arange())
# getSwitchCost.m:119
    new_cluster_cost[2,arange()]=new_cluster_cost_vec2(min_idx,arange())
# getSwitchCost.m:120
    # new_cluster_cost = new_cluster_cost_vec(:,min_idx);
    
    change_cluster_idx=concat([track_class(track_id),min_idx])
# getSwitchCost.m:123
    new_cluster_set=cell(1,2)
# getSwitchCost.m:124
    new_cluster_set[1]=track_id_set[min_idx][1]
# getSwitchCost.m:125
    new_cluster_set[2]=track_id_set[min_idx][2]
# getSwitchCost.m:126