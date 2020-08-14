# Generated with SMOP  0.41
from libsmop import *
# assignDetToTracklet.m

    
@function
def assignDetToTracklet(tracklet_mat=None,*args,**kwargs):
    varargin = assignDetToTracklet.varargin
    nargin = assignDetToTracklet.nargin

    # get tracklet interval
    new_tracklet_mat=copy(tracklet_mat)
# assignDetToTracklet.m:4
    N_tracklet=size(new_tracklet_mat.xmin_mat,1)
# assignDetToTracklet.m:5
    N_fr=size(new_tracklet_mat.xmin_mat,2)
# assignDetToTracklet.m:6
    track_interval=zeros(N_tracklet,2)
# assignDetToTracklet.m:7
    cand_idx=find(new_tracklet_mat.xmin_mat >= 0)
# assignDetToTracklet.m:8
    min_mask=dot(Inf,ones(size(new_tracklet_mat.xmin_mat)))
# assignDetToTracklet.m:9
    min_mask[cand_idx]=cand_idx
# assignDetToTracklet.m:10
    min_v,track_interval(arange(),1)=min(min_mask,[],2,nargout=2)
# assignDetToTracklet.m:11
    track_interval[min_v == Inf,1]=- 1
# assignDetToTracklet.m:12
    max_mask=zeros(size(new_tracklet_mat.xmin_mat))
# assignDetToTracklet.m:13
    max_mask[cand_idx]=cand_idx
# assignDetToTracklet.m:14
    max_v,track_interval(arange(),2)=max(max_mask,[],2,nargout=2)
# assignDetToTracklet.m:15
    track_interval[max_v == 0,2]=- 1
# assignDetToTracklet.m:16
    # fit gaussian regression model
    len_tracklet_thresh=5
# assignDetToTracklet.m:19
    sigma=8
# assignDetToTracklet.m:20
    model_set.x = copy(cell(1,N_tracklet))
# assignDetToTracklet.m:21
    model_set.y = copy(cell(1,N_tracklet))
# assignDetToTracklet.m:22
    for n in arange(1,N_tracklet).reshape(-1):
        len_tracklet=track_interval(n,2) - track_interval(n,1) + 1
# assignDetToTracklet.m:24
        if len_tracklet < len_tracklet_thresh:
            continue
        t=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# assignDetToTracklet.m:28
        det_pts=concat([[dot(0.5,(new_tracklet_mat.xmin_mat(n,t) + new_tracklet_mat.xmax_mat(n,t))) + 1],[new_tracklet_mat.ymax_mat(n,t)]])
# assignDetToTracklet.m:29
        det_pts=det_pts.T
# assignDetToTracklet.m:32
        model_set.x[n]=fitrgp(t.T,det_pts(arange(),1),'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# assignDetToTracklet.m:34
        model_set.y[n]=fitrgp(t.T,det_pts(arange(),2),'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# assignDetToTracklet.m:36
    
    # assign det to tracklet
    pred_model_x=dot(- 1,ones(N_tracklet,N_fr))
# assignDetToTracklet.m:41
    pred_model_y=dot(- 1,ones(N_tracklet,N_fr))
# assignDetToTracklet.m:42
    for n in arange(1,N_tracklet).reshape(-1):
        if isempty(model_set.x[n]):
            continue
        pred_model_x[n,arange()]=predict(model_set.x[n],(arange(1,N_fr)).T).T
# assignDetToTracklet.m:47
        pred_model_y[n,arange()]=predict(model_set.y[n],(arange(1,N_fr)).T).T
# assignDetToTracklet.m:48
    
    for t in arange(1,N_fr).reshape(-1):
        #     cand_track = 1:N_tracklet;
        cand_track=find(t >= logical_and(track_interval(arange(),1),t) <= track_interval(arange(),2))
# assignDetToTracklet.m:53
        #     cand_track = find(new_tracklet_mat.xmin_mat(:,t)>=0);
        remove_idx=[]
# assignDetToTracklet.m:56
        for n in arange(1,length(cand_track)).reshape(-1):
            if logical_not(isempty(model_set.x[cand_track(n)])):
                remove_idx=concat([remove_idx,n])
# assignDetToTracklet.m:59
        cand_track[remove_idx]=[]
# assignDetToTracklet.m:62
        if length(cand_track) < 2:
            continue
        det_x=dot(0.5,(new_tracklet_mat.xmin_mat(cand_track,t) + new_tracklet_mat.xmax_mat(cand_track,t))) + 1
# assignDetToTracklet.m:67
        det_y=new_tracklet_mat.ymax_mat(cand_track,t)
# assignDetToTracklet.m:68
        det_pts=concat([det_x,det_y])
# assignDetToTracklet.m:69
        pred_pts=concat([pred_model_x(cand_track,t),pred_model_y(cand_track,t)])
# assignDetToTracklet.m:70
        dist_mat=pdist2(det_pts,pred_pts)
# assignDetToTracklet.m:71
        N_cand=length(cand_track)
# assignDetToTracklet.m:72
        for n1 in arange(1,N_cand).reshape(-1):
            prev_cost=zeros(1,N_cand)
# assignDetToTracklet.m:74
            cur_cost=zeros(1,N_cand)
# assignDetToTracklet.m:75
            for n2 in arange(1,N_cand).reshape(-1):
                if n2 == n1:
                    continue
                prev_cost[n2]=dist_mat(n1,n1) + dist_mat(n2,n2)
# assignDetToTracklet.m:80
                cur_cost[n2]=dist_mat(n1,n2) + dist_mat(n2,n1)
# assignDetToTracklet.m:81
            diff_cost=cur_cost - prev_cost
# assignDetToTracklet.m:83
            diff_cost[n1]=Inf
# assignDetToTracklet.m:84
            min_cost,idx2=min(diff_cost,nargout=2)
# assignDetToTracklet.m:85
            if min_cost > 0:
                continue
            vec1=dist_mat(n1,arange())
# assignDetToTracklet.m:89
            dist_mat[n1,arange()]=dist_mat(idx2,arange())
# assignDetToTracklet.m:90
            dist_mat[idx2,arange()]=vec1
# assignDetToTracklet.m:91
            vec2=dist_mat(arange(),n1)
# assignDetToTracklet.m:92
            dist_mat[arange(),n1]=dist_mat(arange(),idx2)
# assignDetToTracklet.m:93
            dist_mat[arange(),idx2]=vec2
# assignDetToTracklet.m:94
            temp_v=new_tracklet_mat.xmin_mat(cand_track(n1),t)
# assignDetToTracklet.m:97
            new_tracklet_mat.xmin_mat[cand_track(n1),t]=new_tracklet_mat.xmin_mat(cand_track(idx2),t)
# assignDetToTracklet.m:98
            new_tracklet_mat.xmin_mat[cand_track(idx2),t]=temp_v
# assignDetToTracklet.m:99
            temp_v=new_tracklet_mat.ymin_mat(cand_track(n1),t)
# assignDetToTracklet.m:100
            new_tracklet_mat.ymin_mat[cand_track(n1),t]=new_tracklet_mat.ymin_mat(cand_track(idx2),t)
# assignDetToTracklet.m:101
            new_tracklet_mat.ymin_mat[cand_track(idx2),t]=temp_v
# assignDetToTracklet.m:102
            temp_v=new_tracklet_mat.xmax_mat(cand_track(n1),t)
# assignDetToTracklet.m:103
            new_tracklet_mat.xmax_mat[cand_track(n1),t]=new_tracklet_mat.xmax_mat(cand_track(idx2),t)
# assignDetToTracklet.m:104
            new_tracklet_mat.xmax_mat[cand_track(idx2),t]=temp_v
# assignDetToTracklet.m:105
            temp_v=new_tracklet_mat.ymax_mat(cand_track(n1),t)
# assignDetToTracklet.m:106
            new_tracklet_mat.ymax_mat[cand_track(n1),t]=new_tracklet_mat.ymax_mat(cand_track(idx2),t)
# assignDetToTracklet.m:107
            new_tracklet_mat.ymax_mat[cand_track(idx2),t]=temp_v
# assignDetToTracklet.m:108
    