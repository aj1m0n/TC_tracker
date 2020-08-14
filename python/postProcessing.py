# Generated with SMOP  0.41
from libsmop import *
# postProcessing.m

    
@function
def postProcessing(tracklet_mat=None,track_params=None,*args,**kwargs):
    varargin = postProcessing.varargin
    nargin = postProcessing.nargin

    new_tracklet_mat=copy(tracklet_mat)
# postProcessing.m:3
    # update track clusters
    N_cluster=length(tracklet_mat.track_cluster)
# postProcessing.m:6
    remove_idx=[]
# postProcessing.m:7
    for n in arange(1,N_cluster).reshape(-1):
        if isempty(tracklet_mat.track_cluster[n]):
            remove_idx=concat([remove_idx,n])
# postProcessing.m:10
            continue
        cnt=0
# postProcessing.m:13
        temp_ids=zeros(1,length(tracklet_mat.track_cluster[n]))
# postProcessing.m:14
        for k in arange(1,length(tracklet_mat.track_cluster[n])).reshape(-1):
            track_id=tracklet_mat.track_cluster[n](k)
# postProcessing.m:16
            temp_ids[k]=track_id
# postProcessing.m:17
            cnt=cnt + tracklet_mat.track_interval(track_id,2) - tracklet_mat.track_interval(track_id,1) + 1
# postProcessing.m:18
        if cnt < track_params.const_fr_thresh:
            remove_idx=concat([remove_idx,n])
# postProcessing.m:21
            new_tracklet_mat.mask_flag[temp_ids]=0
# postProcessing.m:22
    
    new_tracklet_mat.track_cluster[remove_idx]=[]
# postProcessing.m:25
    new_tracklet_mat.cluster_cost[remove_idx]=[]
# postProcessing.m:26
    new_tracklet_mat.cluster_flag = copy(zeros(size(new_tracklet_mat.track_class)))
# postProcessing.m:27
    new_tracklet_mat.cluster_flag[arange(1,length(new_tracklet_mat.track_cluster))]=1
# postProcessing.m:28
    # update track class
    new_tracklet_mat.track_class = copy(dot(- 1,ones(size(new_tracklet_mat.track_class))))
# postProcessing.m:31
    N_cluster=length(new_tracklet_mat.track_cluster)
# postProcessing.m:32
    for n in arange(1,N_cluster).reshape(-1):
        for k in arange(1,length(new_tracklet_mat.track_cluster[n])).reshape(-1):
            track_id=new_tracklet_mat.track_cluster[n](k)
# postProcessing.m:35
            new_tracklet_mat.track_class[track_id]=n
# postProcessing.m:36
    
    for n in arange(1,length(new_tracklet_mat.track_class)).reshape(-1):
        if new_tracklet_mat.track_class(n) > 0:
            continue
        new_tracklet_mat.track_cluster[length(new_tracklet_mat.track_cluster) + 1]=n
# postProcessing.m:44
        new_tracklet_mat.track_class[n]=length(new_tracklet_mat.track_cluster)
# postProcessing.m:45
    
    # assign tracklet
    N_id=round(sum(new_tracklet_mat.cluster_flag))
# postProcessing.m:50
    N_cluster=length(new_tracklet_mat.track_cluster)
# postProcessing.m:51
    N_fr=track_params.num_fr
# postProcessing.m:52
    N_tracklet=length(new_tracklet_mat.track_class)
# postProcessing.m:53
    new_track_cluster=new_tracklet_mat.track_cluster
# postProcessing.m:54
    new_track_class=new_tracklet_mat.track_class
# postProcessing.m:55
    cluster_params=new_tracklet_mat.cluster_params
# postProcessing.m:56
    track_interval=new_tracklet_mat.track_interval
# postProcessing.m:57
    neighbor_track_idx=new_tracklet_mat.neighbor_track_idx
# postProcessing.m:58
    new_tracklet_mat.track_cluster[arange(N_id + 1,end())]=[]
# postProcessing.m:60
    new_tracklet_mat2=updateTrackletMat(new_tracklet_mat)
# postProcessing.m:61
    return new_tracklet_mat,new_tracklet_mat2
    tic
    ex_track_idx=cell(1,N_tracklet)
# postProcessing.m:65
    for n in arange(1,N_tracklet).reshape(-1):
        t_min=max(track_interval(n,1),track_interval(arange(),1))
# postProcessing.m:67
        t_max=min(track_interval(n,2),track_interval(arange(),2))
# postProcessing.m:68
        ex_track_idx[n]=find(t_max >= t_min)
# postProcessing.m:69
        ex_track_idx[n][ex_track_idx[n] == n]=[]
# postProcessing.m:70
    
    toc
    tic
    dist_thresh=0.2
# postProcessing.m:75
    t_dist_thresh=15
# postProcessing.m:76
    sigma=16
# postProcessing.m:77
    cluster_map=dot(- 1,ones(N_id,N_fr))
# postProcessing.m:78
    pred_map=dot(- 1,ones(N_id,N_fr))
# postProcessing.m:79
    pred_x_map=dot(- 1,ones(N_id,N_fr))
# postProcessing.m:80
    pred_y_map=dot(- 1,ones(N_id,N_fr))
# postProcessing.m:81
    for n in arange(1,N_id).reshape(-1):
        t=[]
# postProcessing.m:83
        x=[]
# postProcessing.m:84
        y=[]
# postProcessing.m:85
        for k in arange(1,length(new_track_cluster[n])).reshape(-1):
            track_id=new_track_cluster[n](k)
# postProcessing.m:87
            temp_t=arange(track_interval(track_id,1),track_interval(track_id,2))
# postProcessing.m:88
            cluster_map[n,temp_t]=1
# postProcessing.m:89
            temp_t=uniformSample(temp_t,cluster_params.track_len)
# postProcessing.m:90
            temp_x=new_tracklet_mat.det_x(track_id,temp_t)
# postProcessing.m:91
            temp_y=new_tracklet_mat.det_y(track_id,temp_t)
# postProcessing.m:92
            t=concat([t,temp_t])
# postProcessing.m:93
            x=concat([x,temp_x])
# postProcessing.m:94
            y=concat([y,temp_y])
# postProcessing.m:95
        uniq_t,idx=unique(t,nargout=2)
# postProcessing.m:97
        uniq_x=x(idx)
# postProcessing.m:98
        uniq_y=y(idx)
# postProcessing.m:99
        t_min=max(min(uniq_t) - t_dist_thresh,1)
# postProcessing.m:100
        t_max=min(max(uniq_t) + t_dist_thresh,N_fr)
# postProcessing.m:101
        model_x=fitrgp(uniq_t.T,uniq_x.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# postProcessing.m:103
        pred_x_map[n,arange(t_min,t_max)]=(predict(model_x,concat([arange(t_min,t_max)]).T)).T
# postProcessing.m:106
        model_y=fitrgp(uniq_t.T,uniq_y.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# postProcessing.m:108
        pred_y_map[n,arange(t_min,t_max)]=(predict(model_y,concat([arange(t_min,t_max)]).T)).T
# postProcessing.m:111
    
    pred_x_map[cluster_map > 0]=- 1
# postProcessing.m:113
    pred_y_map[cluster_map > 0]=- 1
# postProcessing.m:114
    pred_map[pred_x_map != - 1]=1
# postProcessing.m:115
    toc
    # tic
# left_id = find(new_tracklet_mat.mask_flag<0.5);
# D = Inf*ones(N_id,N_cluster-N_id);
# parfor n = 1:length(left_id)
#     track_id = left_id(n);
#     temp_interval = track_interval(track_id,:);
#     for k = 1:N_id
#         if ~isempty(intersect(ex_track_idx{track_id},new_track_cluster{k}))
#             continue
#         end
#         if isempty(intersect(neighbor_track_idx{track_id},new_track_cluster{k}))
#             continue
#         end
#         D(k,n) = combCost(track_set, new_tracklet_mat, new_tracklet_mat.cluster_params);
#     end
# end
# toc
    
    tic
    left_id=find(new_tracklet_mat.mask_flag < 0.5)
# postProcessing.m:137
    D=dot(Inf,ones(N_id,N_cluster - N_id))
# postProcessing.m:138
    for n in arange(1,length(left_id)).reshape(-1):
        track_id=left_id(n)
# postProcessing.m:140
        temp_interval=track_interval(track_id,arange())
# postProcessing.m:141
        for k in arange(1,N_id).reshape(-1):
            if logical_not(isempty(intersect(ex_track_idx[track_id],new_track_cluster[k]))):
                continue
            if isempty(intersect(neighbor_track_idx[track_id],new_track_cluster[k])):
                continue
            temp_t=zeros(1,N_fr)
# postProcessing.m:149
            temp_t[arange(temp_interval(1),temp_interval(2))]=1
# postProcessing.m:150
            t_idx=(temp_t > logical_and(0.5,pred_map(k,arange())) > 0.5)
# postProcessing.m:151
            if sum(t_idx) < 0.5:
                continue
            delta_x=new_tracklet_mat.det_x(track_id,t_idx) - pred_x_map(k,t_idx)
# postProcessing.m:155
            delta_y=new_tracklet_mat.det_y(track_id,t_idx) - pred_y_map(k,t_idx)
# postProcessing.m:156
            w=new_tracklet_mat.xmax_mat(track_id,t_idx) - new_tracklet_mat.xmin_mat(track_id,t_idx)
# postProcessing.m:157
            h=new_tracklet_mat.ymax_mat(track_id,t_idx) - new_tracklet_mat.ymin_mat(track_id,t_idx)
# postProcessing.m:158
            D[k,n]=mean(sqrt(delta_x ** 2 + delta_y ** 2) / sqrt(w ** 2 + h ** 2))
# postProcessing.m:159
    
    toc
    tic
    update_flag=zeros(1,length(left_id))
# postProcessing.m:167
    while 1:

        cluster_change_idx=zeros(1,N_id)
# postProcessing.m:169
        while 1:

            D[arange(),update_flag == 1]=Inf
# postProcessing.m:171
            min_v,idx=min_mat(D,nargout=2)
# postProcessing.m:172
            if min_v > dist_thresh:
                break
            new_track_cluster[idx(1)]=concat([new_track_cluster[idx(1)],left_id(idx(2))])
# postProcessing.m:176
            cluster_change_idx[idx(1)]=1
# postProcessing.m:177
            update_flag[idx(2)]=1
# postProcessing.m:178
            D[arange(),idx(2)]=Inf
# postProcessing.m:179
            for n in arange(1,length(left_id)).reshape(-1):
                if update_flag(n) == 1 or D(idx(1),n) == Inf:
                    continue
                track_id=left_id(n)
# postProcessing.m:186
                if logical_not(isempty(intersect(ex_track_idx[track_id],new_track_cluster[idx(1)]))):
                    D[idx(1),n]=Inf
# postProcessing.m:189
                    continue

        if sum(cluster_change_idx) == 0:
            break
        # update model
        for n in arange(1,N_id).reshape(-1):
            if cluster_change_idx(n) == 0:
                continue
            pred_x_map[n,arange()]=- 1
# postProcessing.m:206
            pred_y_map[n,arange()]=- 1
# postProcessing.m:207
            cluster_map[n,arange()]=- 1
# postProcessing.m:208
            t=[]
# postProcessing.m:209
            x=[]
# postProcessing.m:210
            y=[]
# postProcessing.m:211
            for k in arange(1,length(new_track_cluster[n])).reshape(-1):
                track_id=new_track_cluster[n](k)
# postProcessing.m:213
                temp_t=arange(track_interval(track_id,1),track_interval(track_id,2))
# postProcessing.m:214
                cluster_map[n,temp_t]=1
# postProcessing.m:215
                temp_t=uniformSample(temp_t,cluster_params.track_len)
# postProcessing.m:216
                temp_x=new_tracklet_mat.det_x(track_id,temp_t)
# postProcessing.m:217
                temp_y=new_tracklet_mat.det_y(track_id,temp_t)
# postProcessing.m:218
                t=concat([t,temp_t])
# postProcessing.m:219
                x=concat([x,temp_x])
# postProcessing.m:220
                y=concat([y,temp_y])
# postProcessing.m:221
            uniq_t,t_idx=unique(t,nargout=2)
# postProcessing.m:223
            uniq_x=x(t_idx)
# postProcessing.m:224
            uniq_y=y(t_idx)
# postProcessing.m:225
            t_min=max(min(uniq_t) - t_dist_thresh,1)
# postProcessing.m:226
            t_max=min(max(uniq_t) + t_dist_thresh,N_fr)
# postProcessing.m:227
            model_x=fitrgp(uniq_t.T,uniq_x.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# postProcessing.m:229
            pred_x_map[n,arange(t_min,t_max)]=(predict(model_x,concat([arange(t_min,t_max)]).T)).T
# postProcessing.m:232
            model_y=fitrgp(uniq_t.T,uniq_y.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# postProcessing.m:234
            pred_y_map[n,arange(t_min,t_max)]=(predict(model_y,concat([arange(t_min,t_max)]).T)).T
# postProcessing.m:237
            pred_map[n,pred_x_map(n,arange()) != - 1]=1
# postProcessing.m:238
        tic
        for n in arange(1,length(left_id)).reshape(-1):
            if update_flag(n) == 1:
                continue
            track_id=left_id(n)
# postProcessing.m:247
            temp_interval=track_interval(track_id,arange())
# postProcessing.m:248
            for k in arange(1,N_id).reshape(-1):
                if cluster_change_idx(k) == 0:
                    continue
                if logical_not(isempty(intersect(ex_track_idx[track_id],new_track_cluster[k]))):
                    continue
                if isempty(intersect(neighbor_track_idx[track_id],new_track_cluster[k])):
                    continue
                temp_t=zeros(1,N_fr)
# postProcessing.m:260
                temp_t[arange(temp_interval(1),temp_interval(2))]=1
# postProcessing.m:261
                t_idx=(temp_t > logical_and(0.5,pred_map(k,arange())) > 0.5)
# postProcessing.m:262
                delta_x=new_tracklet_mat.det_x(track_id,t_idx) - pred_x_map(k,t_idx)
# postProcessing.m:263
                delta_y=new_tracklet_mat.det_y(track_id,t_idx) - pred_y_map(k,t_idx)
# postProcessing.m:264
                w=new_tracklet_mat.xmax_mat(track_id,t_idx) - new_tracklet_mat.xmin_mat(track_id,t_idx)
# postProcessing.m:265
                h=new_tracklet_mat.ymax_mat(track_id,t_idx) - new_tracklet_mat.ymin_mat(track_id,t_idx)
# postProcessing.m:266
                D[k,n]=mean(sqrt(delta_x ** 2 + delta_y ** 2) / sqrt(w ** 2 + h ** 2))
# postProcessing.m:267
        toc

    
    new_tracklet_mat.track_cluster = copy(new_track_cluster(arange(1,N_id)))
# postProcessing.m:272
    toc
    new_tracklet_mat2=updateTrackletMat(new_tracklet_mat)
# postProcessing.m:275