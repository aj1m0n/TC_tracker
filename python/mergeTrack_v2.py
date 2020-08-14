# Generated with SMOP  0.41
from libsmop import *
# mergeTrack_v2.m

    
@function
def mergeTrack_v2(tracklet_mat=None,*args,**kwargs):
    varargin = mergeTrack_v2.varargin
    nargin = mergeTrack_v2.nargin

    # get tracklet interval
    new_tracklet_mat=copy(tracklet_mat)
# mergeTrack_v2.m:4
    N_tracklet=size(new_tracklet_mat.xmin_mat,1)
# mergeTrack_v2.m:5
    track_interval=zeros(N_tracklet,2)
# mergeTrack_v2.m:6
    cand_idx=find(new_tracklet_mat.xmin_mat >= 0)
# mergeTrack_v2.m:7
    min_mask=dot(Inf,ones(size(new_tracklet_mat.xmin_mat)))
# mergeTrack_v2.m:8
    min_mask[cand_idx]=cand_idx
# mergeTrack_v2.m:9
    min_v,track_interval(arange(),1)=min(min_mask,[],2,nargout=2)
# mergeTrack_v2.m:10
    track_interval[min_v == Inf,1]=- 1
# mergeTrack_v2.m:11
    max_mask=dot(- 1,ones(size(new_tracklet_mat.xmin_mat)))
# mergeTrack_v2.m:12
    max_mask[cand_idx]=cand_idx
# mergeTrack_v2.m:13
    max_v,track_interval(arange(),2)=max(max_mask,[],2,nargout=2)
# mergeTrack_v2.m:14
    track_interval[max_v == 0,2]=- 1
# mergeTrack_v2.m:15
    det_x=dot(0.5,(new_tracklet_mat.xmin_mat + new_tracklet_mat.xmax_mat)) + 1
# mergeTrack_v2.m:17
    det_y=new_tracklet_mat.ymax_mat
# mergeTrack_v2.m:18
    # merge track
    len_tracklet_thresh=10
# mergeTrack_v2.m:21
    sigma=8
# mergeTrack_v2.m:22
    intersect_ratio=0.2
# mergeTrack_v2.m:23
    t_dist_thresh=30
# mergeTrack_v2.m:24
    lambda_fit_cost=10
# mergeTrack_v2.m:25
    testing_size=10
# mergeTrack_v2.m:26
    # data_cost_thresh = 10;
    tr_size=50
# mergeTrack_v2.m:28
    assign_cost=dot(- 1,ones(N_tracklet,N_tracklet))
# mergeTrack_v2.m:29
    assign_cost_data=dot(- 1,ones(N_tracklet,N_tracklet))
# mergeTrack_v2.m:30
    for n in arange(1,N_tracklet).reshape(-1):
        t_1=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack_v2.m:32
        if length(t_1) < len_tracklet_thresh:
            continue
        # find available tracklets before and after
        cand_idx=find(track_interval(n,1) - track_interval(arange(),2) < logical_and(t_dist_thresh,track_interval(arange(),1) - track_interval(n,2)) < t_dist_thresh)
# mergeTrack_v2.m:39
        if isempty(cand_idx):
            continue
        remove_idx=[]
# mergeTrack_v2.m:43
        vec_idx1=find(new_tracklet_mat.xmin_mat(n,arange()) >= 0)
# mergeTrack_v2.m:44
        for k in arange(1,length(cand_idx)).reshape(-1):
            vec_idx2=find(new_tracklet_mat.xmin_mat(cand_idx(k),arange()) >= 0)
# mergeTrack_v2.m:46
            vec_idx3=intersect(vec_idx1,vec_idx2)
# mergeTrack_v2.m:47
            if length(vec_idx3) / min(length(vec_idx1),length(vec_idx3)) > intersect_ratio:
                remove_idx=concat([remove_idx,k])
# mergeTrack_v2.m:49
        cand_idx[remove_idx]=[]
# mergeTrack_v2.m:52
        if isempty(cand_idx):
            continue
        cand_idx[assign_cost(n,cand_idx) >= 0]=[]
# mergeTrack_v2.m:56
        if isempty(cand_idx):
            continue
        for k in arange(1,length(cand_idx)).reshape(-1):
            if (cand_idx(k) == 59 and n == 9) or (cand_idx(k) == 9 and n == 59):
                aa=0
# mergeTrack_v2.m:64
            t_2=find(new_tracklet_mat.xmin_mat(cand_idx(k),arange()) >= 0)
# mergeTrack_v2.m:66
            t_3=intersect(t_1,t_2)
# mergeTrack_v2.m:67
            t1=setdiff(t_1,t_3)
# mergeTrack_v2.m:68
            t2=setdiff(t_2,t_3)
# mergeTrack_v2.m:69
            det_x1=det_x(n,t1)
# mergeTrack_v2.m:70
            det_y1=det_y(n,t1)
# mergeTrack_v2.m:71
            det_x2=det_x(cand_idx(k),t2)
# mergeTrack_v2.m:72
            det_y2=det_y(cand_idx(k),t2)
# mergeTrack_v2.m:73
            t,det_x_t,det_x_tr,t_interval,t_tr=dataGroup(t1,t2,det_x1,det_x2,tr_size,nargout=5)
# mergeTrack_v2.m:75
            model_x=fitrgp(t_tr.T,det_x_tr.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# mergeTrack_v2.m:77
            xpred=predict(model_x,(arange(t_interval(1) - 2,t_interval(end()) + 2)).T)
# mergeTrack_v2.m:80
            vx_pred=(xpred(arange(2,end())) - xpred(arange(1,end() - 1)))
# mergeTrack_v2.m:81
            choose_idx=(t >= logical_and(t_interval(1),t) <= t_interval(2))
# mergeTrack_v2.m:82
            sub_t=t(choose_idx)
# mergeTrack_v2.m:83
            sub_x=det_x_t(choose_idx)
# mergeTrack_v2.m:84
            t_test,interp_x,pred_x=vInterp_v2(sub_t,sub_x,xpred(arange(2,end() - 1)).T,vx_pred.T,t_tr,det_x_tr,nargout=3)
# mergeTrack_v2.m:85
            t,det_y_t,det_y_tr,t_interval,t_tr=dataGroup(t1,t2,det_y1,det_y2,tr_size,nargout=5)
# mergeTrack_v2.m:87
            model_y=fitrgp(t_tr.T,det_y_tr.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# mergeTrack_v2.m:88
            ypred=predict(model_y,(arange(t_interval(1) - 2,t_interval(end()) + 2)).T)
# mergeTrack_v2.m:91
            vy_pred=(ypred(arange(2,end())) - ypred(arange(1,end() - 1)))
# mergeTrack_v2.m:92
            sub_t=t(choose_idx)
# mergeTrack_v2.m:93
            sub_y=det_y_t(choose_idx)
# mergeTrack_v2.m:94
            t_test,interp_y,pred_y=vInterp_v2(sub_t,sub_y,ypred(arange(2,end() - 1)).T,vy_pred.T,t_tr,det_y_tr,nargout=3)
# mergeTrack_v2.m:95
            err=sqrt((pred_x - interp_x) ** 2 + (pred_y - interp_y) ** 2)
# mergeTrack_v2.m:97
            #         mean_err = mean(err);
            if length(err) > testing_size:
                err=sort(err,'descend')
# mergeTrack_v2.m:100
                err=err(arange(1,testing_size))
# mergeTrack_v2.m:101
                mean_err=mean(err)
# mergeTrack_v2.m:102
            else:
                mean_err=mean(err)
# mergeTrack_v2.m:104
            #         if mean(sqrt((pred_x-interp_x).^2+(pred_y-interp_y).^2))<5
#             figure, plot(t_test,interp_x,'r.',t_tr,det_x_tr,'k.',t_test,pred_x,'b.');
#             
#             figure, plot(t_test,interp_y,'r.',t_tr,det_y_tr,'k.',t_test,pred_y,'b.');
#             mean_err
#             
#             #         mean(sqrt((xpred(change_idx)-det_x_t(change_idx)').^2+(ypred(change_idx)-det_y_t(change_idx)').^2))
#             close all
#         end
#         assign_cost(cand_idx(k),n) = mean(sqrt((pred_x-interp_x).^2+(pred_y-interp_y).^2));
#         assign_cost(n,cand_idx(k)) = assign_cost(cand_idx(k),n);
            if length(t1) > length(t2):
                assign_cost[cand_idx(k),n]=mean_err
# mergeTrack_v2.m:120
                #             assign_cost_data(cand_idx(k),n) = mean(sqrt((xpred(change_idx)-det_x_t(change_idx)').^2+(ypred(change_idx)-det_y_t(change_idx)').^2));
            else:
                assign_cost[n,cand_idx(k)]=mean_err
# mergeTrack_v2.m:123
                #             assign_cost_data(n,cand_idx(k)) = mean(sqrt((xpred(change_idx)-det_x_t(change_idx)').^2+(ypred(change_idx)-det_y_t(change_idx)').^2));
    
    assign_cost[assign_cost < 0]=Inf
# mergeTrack_v2.m:128
    # assign_cost_data(assign_cost_data<0) = Inf;
    
    final_assign_idx=zeros(N_tracklet,1)
# mergeTrack_v2.m:131
    cnt=0
# mergeTrack_v2.m:132
    while 1:

        cnt=cnt + 1
# mergeTrack_v2.m:134
        min_v,idx=min_mat(assign_cost,nargout=2)
# mergeTrack_v2.m:135
        if min_v > lambda_fit_cost and cnt == 1:
            end_flag=1
# mergeTrack_v2.m:137
            return new_tracklet_mat,end_flag
        if min_v > lambda_fit_cost:
            break
        final_assign_idx[idx(1)]=idx(2)
# mergeTrack_v2.m:143
        assign_cost[idx(1),arange()]=Inf
# mergeTrack_v2.m:144
        assign_cost[arange(),idx(1)]=Inf
# mergeTrack_v2.m:145
        assign_cost[idx(2),arange()]=Inf
# mergeTrack_v2.m:146
        assign_cost[arange(),idx(2)]=Inf
# mergeTrack_v2.m:147
        final_assign_idx[final_assign_idx == n]=final_assign_idx(n)
# mergeTrack_v2.m:148

    
    # for n = 1:N_tracklet
#     [min_cost,min_cost_idx] = min(assign_cost(n,:));
#     if min_cost<lambda_fit_cost #&& assign_cost_data(n,min_cost_idx)<data_cost_thresh
#         final_assign_idx(n) = min_cost_idx;
#         final_assign_idx(final_assign_idx==n) = final_assign_idx(n);
#     end
# end
    final_assign_idx[final_assign_idx == (arange(1,N_tracklet)).T]=0
# mergeTrack_v2.m:157
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
# mergeTrack_v2.m:177
        new_tracklet_mat.xmin_mat[final_assign_idx(n),t2]=new_tracklet_mat.xmin_mat(n,t2)
# mergeTrack_v2.m:178
        new_tracklet_mat.ymin_mat[final_assign_idx(n),t2]=new_tracklet_mat.ymin_mat(n,t2)
# mergeTrack_v2.m:180
        new_tracklet_mat.xmax_mat[final_assign_idx(n),t2]=new_tracklet_mat.xmax_mat(n,t2)
# mergeTrack_v2.m:182
        new_tracklet_mat.ymax_mat[final_assign_idx(n),t2]=new_tracklet_mat.ymax_mat(n,t2)
# mergeTrack_v2.m:184
        track_interval[n,arange()]=- 1
# mergeTrack_v2.m:186
    
    new_tracklet_mat.xmin_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack_v2.m:188
    new_tracklet_mat.ymin_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack_v2.m:189
    new_tracklet_mat.xmax_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack_v2.m:190
    new_tracklet_mat.ymax_mat[track_interval(arange(),1) == - 1,arange()]=[]
# mergeTrack_v2.m:191
    end_flag=0
# mergeTrack_v2.m:192