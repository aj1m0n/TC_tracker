# Generated with SMOP  0.41
from libsmop import *
# mergeTrack.m

    
@function
def mergeTrack(tracklet_mat=None,*args,**kwargs):
    varargin = mergeTrack.varargin
    nargin = mergeTrack.nargin

    # get tracklet interval
    new_tracklet_mat=copy(tracklet_mat)
# mergeTrack.m:4
    N_tracklet=size(new_tracklet_mat.xmin_mat,1)
# mergeTrack.m:5
    track_interval=zeros(N_tracklet,2)
# mergeTrack.m:6
    cand_idx=find(new_tracklet_mat.xmin_mat >= 0)
# mergeTrack.m:7
    min_mask=dot(Inf,ones(size(new_tracklet_mat.xmin_mat)))
# mergeTrack.m:8
    min_mask[cand_idx]=cand_idx
# mergeTrack.m:9
    min_v,track_interval(arange(),1)=min(min_mask,[],2,nargout=2)
# mergeTrack.m:10
    track_interval[min_v == Inf,1]=- 1
# mergeTrack.m:11
    max_mask=dot(- 1,ones(size(new_tracklet_mat.xmin_mat)))
# mergeTrack.m:12
    max_mask[cand_idx]=cand_idx
# mergeTrack.m:13
    max_v,track_interval(arange(),2)=max(max_mask,[],2,nargout=2)
# mergeTrack.m:14
    track_interval[max_v == 0,2]=- 1
# mergeTrack.m:15
    # fit gaussian regression model
    sigma=8
# mergeTrack.m:18
    len_tracklet_thresh=10
# mergeTrack.m:19
    model_set.x = copy(cell(1,N_tracklet))
# mergeTrack.m:20
    model_set.y = copy(cell(1,N_tracklet))
# mergeTrack.m:21
    for n in arange(1,N_tracklet).reshape(-1):
        len_tracklet=track_interval(n,2) - track_interval(n,1) + 1
# mergeTrack.m:23
        if len_tracklet < len_tracklet_thresh:
            continue
        t=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack.m:27
        det_pts=concat([[dot(0.5,(new_tracklet_mat.xmin_mat(n,t) + new_tracklet_mat.xmax_mat(n,t))) + 1],[new_tracklet_mat.ymax_mat(n,t)]])
# mergeTrack.m:28
        det_pts=det_pts.T
# mergeTrack.m:31
        model_set.x[n]=fitrgp(t.T,det_pts(arange(),1),'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# mergeTrack.m:33
        model_set.y[n]=fitrgp(t.T,det_pts(arange(),2),'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# mergeTrack.m:35
    
    # merge track
    t_dist_thresh=50
# mergeTrack.m:40
    lambda_fit_cost=80
# mergeTrack.m:41
    testing_size=10
# mergeTrack.m:42
    intersect_ratio=0.2
# mergeTrack.m:43
    # assign_idx = zeros(N_tracklet,50);
# assign_cost = zeros(N_tracklet,50);
    assign_cost=dot(- 1,ones(N_tracklet,N_tracklet))
# mergeTrack.m:46
    for n in arange(1,N_tracklet).reshape(-1):
        t_1=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack.m:48
        if length(t_1) < len_tracklet_thresh:
            continue
        # find available tracklets before and after
        cand_idx=find(track_interval(n,1) - track_interval(arange(),2) < logical_and(t_dist_thresh,track_interval(arange(),1) - track_interval(n,2)) < t_dist_thresh)
# mergeTrack.m:54
        if isempty(cand_idx):
            continue
        remove_idx=[]
# mergeTrack.m:58
        vec_idx1=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack.m:59
        for k in arange(1,length(cand_idx)).reshape(-1):
            vec_idx2=find(new_tracklet_mat.xmin_mat(cand_idx(k),arange()) >= 0)
# mergeTrack.m:61
            vec_idx3=intersect(vec_idx1,vec_idx2)
# mergeTrack.m:62
            if length(vec_idx3) / min(length(vec_idx1),length(vec_idx3)) > intersect_ratio:
                remove_idx=concat([remove_idx,k])
# mergeTrack.m:64
        cand_idx[remove_idx]=[]
# mergeTrack.m:67
        if isempty(cand_idx):
            continue
        cand_idx[assign_cost(n,cand_idx) >= 0]=[]
# mergeTrack.m:71
        if isempty(cand_idx):
            continue
        for k in arange(1,length(cand_idx)).reshape(-1):
            t2=find(new_tracklet_mat.xmin_mat(cand_idx(k),arange()) >= 0)
# mergeTrack.m:77
            t2_after_idx=t2(t2 > track_interval(n,2))
# mergeTrack.m:79
            if length(t2_after_idx) > testing_size:
                t2_after_idx=t2_after_idx(arange(1,testing_size))
# mergeTrack.m:81
            t2_before_idx=t2(t2 < track_interval(n,1))
# mergeTrack.m:83
            if length(t2_before_idx) > testing_size:
                t2_before_idx=t2_before_idx(arange(end() - testing_size + 1,end()))
# mergeTrack.m:85
            t2_mid_idx=t2(t2 < logical_and(track_interval(n,2),t2) > track_interval(n,1))
# mergeTrack.m:87
            t2=concat([t2_before_idx,t2_mid_idx,t2_after_idx])
# mergeTrack.m:88
            #         t_2 = find(new_tracklet_mat.xmin_mat(cand_idx(k),:)>=0);
#         t_3 = intersect(t_1,t_2);
#         t1 = setdiff(t_1,t_3);
#         t2 = setdiff(t_2,t_3);
            det_pts2=concat([[dot(0.5,(new_tracklet_mat.xmin_mat(cand_idx(k),t2) + new_tracklet_mat.xmax_mat(cand_idx(k),t2))) + 1],[new_tracklet_mat.ymax_mat(cand_idx(k),t2)]])
# mergeTrack.m:95
            det_pts2=det_pts2.T
# mergeTrack.m:98
            xpred2=predict(model_set.x[n],t2.T)
# mergeTrack.m:100
            ypred2=predict(model_set.y[n],t2.T)
# mergeTrack.m:101
            mean_err=mean(sqrt((xpred2 - det_pts2(arange(),1)) ** 2 + (ypred2 - det_pts2(arange(),2)) ** 2))
# mergeTrack.m:103
            assign_cost[cand_idx(k),n]=mean_err
# mergeTrack.m:105
            assign_cost[n,cand_idx(k)]=mean_err
# mergeTrack.m:106
            #         cost_vec(k) = mean(sqrt((xpred2-det_pts2(:,1)).^2+(ypred2-det_pts2(:,2)).^2));
        #     [min_cost,min_idx] = min(cost_vec);
#     if min_cost>lambda_fit_cost
#         continue
#     end
#     comb_idx = cand_idx(min_idx);
#     
#     [~,min_assign_idx] = min(assign_idx(comb_idx,:));
#     assign_idx(comb_idx,min_assign_idx) = n;
#     assign_cost(comb_idx,min_assign_idx) = min_cost;
        # find available tracklets after end fr
#     cand_idx = find(track_interval(:,1)>track_interval(n,2) & track_interval(:,1)-track_interval(n,2)<t_dist_thresh);
#     if isempty(cand_idx)
#         continue
#     end
#     cost_vec = zeros(size(cand_idx));
#     for k = 1:length(cand_idx)
#         t2 = find(new_tracklet_mat.xmin_mat(cand_idx(k),:)>=0);
#         det_pts2 = [0.5*(new_tracklet_mat.xmin_mat(cand_idx(k),t2)+...
#             new_tracklet_mat.xmax_mat(cand_idx(k),t2))+1; ...
#             new_tracklet_mat.ymax_mat(cand_idx(k),t2)];
#         det_pts2 = det_pts2';
#         if length(t2)>testing_size
#             t2 = t2(1:testing_size);
#             det_pts2 = det_pts2(1:testing_size,:);
#         end
#         
#         xpred2 = predict(model_set.x{n},t2');
#         ypred2 = predict(model_set.y{n},t2');
#         cost_vec(k) = mean(sqrt((xpred2-det_pts2(:,1)).^2+(ypred2-det_pts2(:,2)).^2));
#     end
#     [min_cost,min_idx] = min(cost_vec);
#     if min_cost>lambda_fit_cost
#         continue
#     end
#     comb_idx = cand_idx(min_idx);
#     
#     [~,min_assign_idx] = min(assign_idx(comb_idx,:));
#     assign_idx(comb_idx,min_assign_idx) = n;
#     assign_cost(comb_idx,min_assign_idx) = min_cost;
    
    assign_cost[assign_cost < 0]=Inf
# mergeTrack.m:154
    final_assign_idx=zeros(N_tracklet,1)
# mergeTrack.m:155
    cnt=0
# mergeTrack.m:156
    while 1:

        cnt=cnt + 1
# mergeTrack.m:158
        min_v,idx=min_mat(assign_cost,nargout=2)
# mergeTrack.m:159
        if min_v > lambda_fit_cost and cnt == 1:
            end_flag=1
# mergeTrack.m:161
            return new_tracklet_mat,end_flag
        if min_v > lambda_fit_cost:
            break
        final_assign_idx[idx(1)]=idx(2)
# mergeTrack.m:167
        assign_cost[idx(1),arange()]=Inf
# mergeTrack.m:168
        assign_cost[arange(),idx(1)]=Inf
# mergeTrack.m:169
        assign_cost[idx(2),arange()]=Inf
# mergeTrack.m:170
        assign_cost[arange(),idx(2)]=Inf
# mergeTrack.m:171
        final_assign_idx[final_assign_idx == n]=final_assign_idx(n)
# mergeTrack.m:172

    
    final_assign_idx[final_assign_idx == (arange(1,N_tracklet)).T]=0
# mergeTrack.m:174
    # sum_idx = sum(assign_idx);
# assign_idx(:,sum_idx==0) = [];
# assign_cost(:,sum_idx==0) = [];
# assign_cost(assign_cost==0) = Inf;
# if isempty(assign_cost)
#     end_flag = 1;
#     return
# end
# 
# final_assign_idx = zeros(N_tracklet,1);
# for n = 1:N_tracklet
#     if assign_idx(n,1)==0
#         continue
#     end
#     [~,min_cost_idx] = min(assign_cost(n,:));
#     final_assign_idx(n) = assign_idx(n,min_cost_idx);
#     assign_idx(assign_idx==n) = final_assign_idx(n);
#     final_assign_idx(final_assign_idx==n) = final_assign_idx(n);
# end
# final_assign_idx(final_assign_idx==(1:N_tracklet)') = 0;
    
    for n in arange(1,N_tracklet).reshape(-1):
        if final_assign_idx(n) == 0:
            continue
        #     t = find(new_tracklet_mat.xmin_mat(final_assign_idx(n),:)>=0);
#     det_pts = [0.5*(new_tracklet_mat.xmin_mat(final_assign_idx(n),t)+...
#         new_tracklet_mat.xmax_mat(final_assign_idx(n),t))+1; ...
#         new_tracklet_mat.ymax_mat(final_assign_idx(n),t)];
#     det_pts = det_pts';
#     t2 = find(new_tracklet_mat.xmin_mat(n,:)>=0);
#     det_pts2 = [0.5*(new_tracklet_mat.xmin_mat(n,t2)+...
#         new_tracklet_mat.xmax_mat(n,t2))+1; ...
#         new_tracklet_mat.ymax_mat(n,t2)];
#     det_pts2 = det_pts2';
#     figure, plot(t,det_pts(:,1),'k.',t2,det_pts2(:,1),'r.')
#     figure, plot(t,det_pts(:,2),'k.',t2,det_pts2(:,2),'r.')
#     close all
        t2=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack.m:216
        new_tracklet_mat.xmin_mat[final_assign_idx(n),t2]=new_tracklet_mat.xmin_mat(n,t2)
# mergeTrack.m:217
        new_tracklet_mat.ymin_mat[final_assign_idx(n),t2]=new_tracklet_mat.ymin_mat(n,t2)
# mergeTrack.m:219
        new_tracklet_mat.xmax_mat[final_assign_idx(n),t2]=new_tracklet_mat.xmax_mat(n,t2)
# mergeTrack.m:221
        new_tracklet_mat.ymax_mat[final_assign_idx(n),t2]=new_tracklet_mat.ymax_mat(n,t2)
# mergeTrack.m:223
        track_interval[n,arange()]=- 1
# mergeTrack.m:225
    
    new_tracklet_mat.xmin_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack.m:227
    new_tracklet_mat.ymin_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack.m:228
    new_tracklet_mat.xmax_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack.m:229
    new_tracklet_mat.ymax_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack.m:230
    end_flag=0
# mergeTrack.m:231