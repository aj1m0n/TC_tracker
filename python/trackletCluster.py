# Generated with SMOP  0.41
from libsmop import *
# trackletCluster.m

    
@function
def trackletCluster(tracklet_mat=None,track_interval=None,track_cluster=None,track_class=None,prev_cluster_cost=None,neighbor_track_idx=None,cluster_params=None,f_mat=None,track_change_set=None,*args,**kwargs):
    varargin = trackletCluster.varargin
    nargin = trackletCluster.nargin

    new_track_cluster=copy(track_cluster)
# trackletCluster.m:5
    new_track_class=copy(track_class)
# trackletCluster.m:6
    new_prev_cluster_cost=copy(prev_cluster_cost)
# trackletCluster.m:7
    new_f_mat=copy(f_mat)
# trackletCluster.m:8
    new_track_change_set=copy(track_change_set)
# trackletCluster.m:9
    __,sort_track_idx=sort(track_interval(arange(),2),'ascend',nargout=2)
# trackletCluster.m:12
    for n in arange(1,length(sort_track_idx)).reshape(-1):
        #     tic
        track_id=sort_track_idx(n)
# trackletCluster.m:15
        if new_track_class(track_id) < 0:
            continue
        diff_cost=zeros(5,1)
# trackletCluster.m:20
        new_C=cell(5,1)
# trackletCluster.m:21
        new_set=cell(5,1)
# trackletCluster.m:22
        change_idx=cell(5,1)
# trackletCluster.m:23
        f=cell(1,5)
# trackletCluster.m:24
        __,diff_cost(1),new_C[1],new_set[1],change_idx[1],f[1]=getSplitCost(track_id,new_track_cluster,new_track_class,tracklet_mat,new_prev_cluster_cost(new_track_class(track_id),arange()),cluster_params,nargout=6)
# trackletCluster.m:25
        __,diff_cost(2),new_C[2],new_set[2],change_idx[2],f[2]=getAssignCost(track_id,tracklet_mat,track_interval,new_track_cluster,new_track_class,neighbor_track_idx,new_prev_cluster_cost,cluster_params,[],nargout=6)
# trackletCluster.m:29
        __,diff_cost(3),new_C[3],new_set[3],change_idx[3],f[3]=getMergeCost(track_id,tracklet_mat,track_interval,new_track_cluster,new_track_class,neighbor_track_idx,new_prev_cluster_cost,cluster_params,nargout=6)
# trackletCluster.m:34
        __,diff_cost(4),new_C[4],new_set[4],change_idx[4],f[4]=getSwitchCost(track_id,tracklet_mat,track_interval,new_track_cluster,new_track_class,neighbor_track_idx,new_prev_cluster_cost,cluster_params,nargout=6)
# trackletCluster.m:39
        __,diff_cost(5),new_C[5],new_set[5],change_idx[5],f[5]=getBreakCost(track_id,new_track_cluster,new_track_class,tracklet_mat,new_prev_cluster_cost(new_track_class(track_id),arange()),cluster_params,nargout=6)
# trackletCluster.m:44
        for k in arange(1,length(f)).reshape(-1):
            if diff_cost(k) == Inf:
                continue
            cnt_id=length(new_track_change_set) + 1
# trackletCluster.m:52
            if cnt_id > size(new_f_mat,1):
                temp_f=zeros(dot(size(new_f_mat,1),2),6)
# trackletCluster.m:54
                temp_f[arange(1,size(new_f_mat,1)),arange()]=new_f_mat
# trackletCluster.m:55
                new_f_mat=copy(temp_f)
# trackletCluster.m:56
            temp_f=f[k]
# trackletCluster.m:59
            min_diff=min(sum(abs(bsxfun(minus,new_f_mat(arange(),arange(1,5)),temp_f)),2))
# trackletCluster.m:60
            if min_diff < 1e-06:
                continue
            if diff_cost(k) < 0:
                new_f_mat[cnt_id,arange(1,5)]=f[k]
# trackletCluster.m:65
                new_f_mat[cnt_id,6]=- 1
# trackletCluster.m:66
                if change_idx[k](1) > length(new_track_cluster):
                    new_track_change_set[cnt_id][1][1]=[]
# trackletCluster.m:68
                else:
                    new_track_change_set[cnt_id][1][1]=new_track_cluster[change_idx[k](1)]
# trackletCluster.m:70
                if change_idx[k](2) > length(new_track_cluster):
                    new_track_change_set[cnt_id][1][2]=[]
# trackletCluster.m:73
                else:
                    new_track_change_set[cnt_id][1][2]=new_track_cluster[change_idx[k](2)]
# trackletCluster.m:75
                new_track_change_set[cnt_id][2][1]=new_set[k][1]
# trackletCluster.m:77
                new_track_change_set[cnt_id][2][2]=new_set[k][2]
# trackletCluster.m:78
            if diff_cost(k) > 0:
                new_f_mat[cnt_id,arange(1,5)]=f[k]
# trackletCluster.m:81
                new_f_mat[cnt_id,6]=1
# trackletCluster.m:82
                if change_idx[k](1) > length(new_track_cluster):
                    new_track_change_set[cnt_id][1][1]=[]
# trackletCluster.m:84
                else:
                    new_track_change_set[cnt_id][1][1]=new_track_cluster[change_idx[k](1)]
# trackletCluster.m:86
                if change_idx[k](2) > length(new_track_cluster):
                    new_track_change_set[cnt_id][1][2]=[]
# trackletCluster.m:89
                else:
                    new_track_change_set[cnt_id][1][2]=new_track_cluster[change_idx[k](2)]
# trackletCluster.m:91
                new_track_change_set[cnt_id][2][1]=new_set[k][1]
# trackletCluster.m:93
                new_track_change_set[cnt_id][2][2]=new_set[k][2]
# trackletCluster.m:94
        min_cost,min_idx=min(diff_cost,nargout=2)
# trackletCluster.m:98
        if min_cost >= 0:
            continue
        new_track_cluster[change_idx[min_idx](1)]=new_set[min_idx][1]
# trackletCluster.m:103
        new_track_cluster[change_idx[min_idx](2)]=new_set[min_idx][2]
# trackletCluster.m:104
        new_prev_cluster_cost[change_idx[min_idx](1),arange()]=new_C[min_idx](1,arange())
# trackletCluster.m:105
        new_prev_cluster_cost[change_idx[min_idx](2),arange()]=new_C[min_idx](2,arange())
# trackletCluster.m:106
        for k in arange(1,length(new_track_cluster[change_idx[min_idx](1)])).reshape(-1):
            new_track_class[new_track_cluster[change_idx[min_idx](1)](k)]=change_idx[min_idx](1)
# trackletCluster.m:109
        for k in arange(1,length(new_track_cluster[change_idx[min_idx](2)])).reshape(-1):
            new_track_class[new_track_cluster[change_idx[min_idx](2)](k)]=change_idx[min_idx](2)
# trackletCluster.m:112
    