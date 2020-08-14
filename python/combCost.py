# Generated with SMOP  0.41
from libsmop import *
# combCost.m

    
@function
def combCost(track_set=None,tracklet_mat=None,cluster_params=None,appearance_cost=None,*args,**kwargs):
    varargin = combCost.varargin
    nargin = combCost.nargin

    # make sure you should set the appearance_cost if you use other methods.
    N_tracklet=length(track_set)
# combCost.m:4
    track_interval=tracklet_mat.track_interval
# combCost.m:5
    __,sort_idx=sort(track_interval(track_set,2),'ascend',nargout=2)
# combCost.m:6
    # split cost
    split_cost=1
# combCost.m:9
    # regression cost
    t=[]
# combCost.m:12
    test_t=[]
# combCost.m:13
    test_x=[]
# combCost.m:14
    test_y=[]
# combCost.m:15
    test_w=[]
# combCost.m:16
    test_h=[]
# combCost.m:17
    det_x=[]
# combCost.m:18
    det_y=[]
# combCost.m:19
    det_w=[]
# combCost.m:20
    det_h=[]
# combCost.m:21
    train_t=[]
# combCost.m:22
    train_x=[]
# combCost.m:23
    train_y=[]
# combCost.m:24
    train_w=[]
# combCost.m:25
    train_h=[]
# combCost.m:26
    end_t=[]
# combCost.m:27
    piece_x=[]
# combCost.m:28
    piece_y=[]
# combCost.m:29
    len_test=4
# combCost.m:30
    if N_tracklet <= 1:
        color_flag=0
# combCost.m:32
    else:
        color_flag=1
# combCost.m:34
        diff_mean_color=zeros(3,N_tracklet - 1)
# combCost.m:35
    
    for n in arange(1,N_tracklet).reshape(-1):
        track_id=track_set(sort_idx(n))
# combCost.m:39
        temp_t=arange(track_interval(track_id,1),track_interval(track_id,2))
# combCost.m:40
        if color_flag == 1:
            if n == 1:
                temp_color=tracklet_mat.color_mat(track_id,temp_t,arange())
# combCost.m:44
                if length(temp_t) > cluster_params.color_sample_size:
                    end_color=temp_color(1,arange(end() - cluster_params.color_sample_size,end()),arange())
# combCost.m:46
                else:
                    end_color=copy(temp_color)
# combCost.m:48
            else:
                if n < N_tracklet:
                    temp_color=tracklet_mat.color_mat(track_id,temp_t,arange())
# combCost.m:51
                    if length(temp_t) > cluster_params.color_sample_size:
                        start_color=temp_color(1,arange(1,cluster_params.color_sample_size),arange())
# combCost.m:53
                    else:
                        start_color=copy(temp_color)
# combCost.m:55
                    diff_mean_color[1,n - 1]=abs(mean(start_color(arange(),1)) - mean(end_color(arange(),1)))
# combCost.m:57
                    diff_mean_color[2,n - 1]=abs(mean(start_color(arange(),2)) - mean(end_color(arange(),2)))
# combCost.m:58
                    diff_mean_color[3,n - 1]=abs(mean(start_color(arange(),3)) - mean(end_color(arange(),3)))
# combCost.m:59
                    if length(temp_t) > cluster_params.color_sample_size:
                        end_color=temp_color(1,arange(end() - cluster_params.color_sample_size,end()),arange())
# combCost.m:61
                    else:
                        end_color=copy(temp_color)
# combCost.m:63
                else:
                    temp_color=tracklet_mat.color_mat(track_id,temp_t,arange())
# combCost.m:66
                    if length(temp_t) > cluster_params.color_sample_size:
                        start_color=temp_color(1,arange(1,cluster_params.color_sample_size),arange())
# combCost.m:68
                    else:
                        start_color=copy(temp_color)
# combCost.m:70
                    diff_mean_color[1,n - 1]=abs(mean(start_color(1,arange(),1)) - mean(end_color(1,arange(),1)))
# combCost.m:72
                    diff_mean_color[2,n - 1]=abs(mean(start_color(1,arange(),2)) - mean(end_color(1,arange(),2)))
# combCost.m:73
                    diff_mean_color[3,n - 1]=abs(mean(start_color(1,arange(),3)) - mean(end_color(1,arange(),3)))
# combCost.m:74
        temp_test_t1=arange(temp_t(1),min(temp_t(end()),temp_t(1) + len_test))
# combCost.m:77
        temp_test_t2=arange(max(temp_t(end()) - len_test,temp_t(1)),temp_t(end()))
# combCost.m:78
        if n != 1:
            test_x=concat([test_x,tracklet_mat.det_x(track_id,temp_test_t1)])
# combCost.m:81
            test_y=concat([test_y,tracklet_mat.det_y(track_id,temp_test_t1)])
# combCost.m:82
            test_w=concat([test_w,tracklet_mat.xmax_mat(track_id,temp_test_t1) - tracklet_mat.xmin_mat(track_id,temp_test_t1) + 1])
# combCost.m:83
            test_h=concat([test_h,tracklet_mat.ymax_mat(track_id,temp_test_t1) - tracklet_mat.ymin_mat(track_id,temp_test_t1) + 1])
# combCost.m:84
            test_t=concat([test_t,temp_test_t1])
# combCost.m:85
            end_t=concat([end_t,temp_t(1)])
# combCost.m:86
        if n != N_tracklet:
            test_x=concat([test_x,tracklet_mat.det_x(track_id,temp_test_t2)])
# combCost.m:90
            test_y=concat([test_y,tracklet_mat.det_y(track_id,temp_test_t2)])
# combCost.m:91
            test_w=concat([test_w,tracklet_mat.xmax_mat(track_id,temp_test_t2) - tracklet_mat.xmin_mat(track_id,temp_test_t2) + 1])
# combCost.m:92
            test_h=concat([test_h,tracklet_mat.ymax_mat(track_id,temp_test_t2) - tracklet_mat.ymin_mat(track_id,temp_test_t2) + 1])
# combCost.m:93
            test_t=concat([test_t,temp_test_t2])
# combCost.m:94
            end_t=concat([end_t,temp_t(end())])
# combCost.m:95
        #     temp_t = uniformSample(temp_t, cluster_params.track_len);
        det_x=concat([det_x,tracklet_mat.det_x(track_id,temp_t)])
# combCost.m:99
        det_y=concat([det_y,tracklet_mat.det_y(track_id,temp_t)])
# combCost.m:100
        det_w=concat([det_w,tracklet_mat.xmax_mat(track_id,temp_t) - tracklet_mat.xmin_mat(track_id,temp_t) + 1])
# combCost.m:101
        det_h=concat([det_h,tracklet_mat.ymax_mat(track_id,temp_t) - tracklet_mat.ymin_mat(track_id,temp_t) + 1])
# combCost.m:102
        t=concat([t,temp_t])
# combCost.m:103
        temp_t1=temp_t(arange(1,min(length(temp_t),cluster_params.track_len)))
# combCost.m:105
        temp_t2=temp_t(arange(end() - min(length(temp_t),cluster_params.track_len) + 1,end()))
# combCost.m:106
        train_t=concat([train_t,temp_t1,temp_t2])
# combCost.m:107
        train_x=concat([train_x,tracklet_mat.det_x(track_id,temp_t1),tracklet_mat.det_x(track_id,temp_t2)])
# combCost.m:108
        train_y=concat([train_y,tracklet_mat.det_y(track_id,temp_t1),tracklet_mat.det_y(track_id,temp_t2)])
# combCost.m:109
        train_w=concat([train_w,tracklet_mat.xmax_mat(track_id,temp_t1) - tracklet_mat.xmin_mat(track_id,temp_t1) + 1,tracklet_mat.xmax_mat(track_id,temp_t2) - tracklet_mat.xmin_mat(track_id,temp_t2) + 1])
# combCost.m:110
        train_h=concat([train_h,tracklet_mat.ymax_mat(track_id,temp_t1) - tracklet_mat.ymin_mat(track_id,temp_t1) + 1,tracklet_mat.ymax_mat(track_id,temp_t2) - tracklet_mat.ymin_mat(track_id,temp_t2) + 1])
# combCost.m:112
    
    grad_cost=0
# combCost.m:116
    if length(unique(t)) < cluster_params.len_tracklet_thresh:
        reg_cost=cluster_params.small_track_cost
# combCost.m:118
        grad_cost=0
# combCost.m:119
    else:
        t,idx=unique(t,nargout=2)
# combCost.m:121
        det_x=det_x(idx)
# combCost.m:122
        det_y=det_y(idx)
# combCost.m:123
        det_w=det_w(idx)
# combCost.m:124
        det_h=det_h(idx)
# combCost.m:125
        #     [t,sample_idx] = uniformSample(t, cluster_params.track_len);
#     det_x = det_x(sample_idx);
#     det_y = det_y(sample_idx);
#     det_w = det_w(sample_idx);
#     det_h = det_h(sample_idx);
        train_t,idx=unique(train_t,nargout=2)
# combCost.m:132
        train_x=train_x(idx)
# combCost.m:133
        train_y=train_y(idx)
# combCost.m:134
        train_w=train_w(idx)
# combCost.m:135
        train_h=train_h(idx)
# combCost.m:136
        det_size=sqrt(train_w ** 2 + train_h ** 2)
# combCost.m:138
        model_x=fitrgp(train_t.T,train_x.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',cluster_params.sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# combCost.m:139
        model_y=fitrgp(train_t.T,train_y.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',cluster_params.sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# combCost.m:142
        model_bbox=fitrgp(train_t.T,det_size.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',cluster_params.sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# combCost.m:145
        if logical_not(isempty(test_t)):
            test_t,test_idx=unique(test_t,nargout=2)
# combCost.m:150
            test_x=test_x(test_idx)
# combCost.m:151
            test_y=test_y(test_idx)
# combCost.m:152
            test_w=test_w(test_idx)
# combCost.m:153
            test_h=test_h(test_idx)
# combCost.m:154
            pred_test_x=predict(model_x,test_t.T)
# combCost.m:155
            pred_test_y=predict(model_y,test_t.T)
# combCost.m:156
            test_size=predict(model_bbox,test_t.T)
# combCost.m:157
            err=sum(sqrt((pred_test_x - test_x.T) ** 2 + (pred_test_y - test_y.T) ** 2) / test_size)
# combCost.m:158
        else:
            err=0
# combCost.m:160
        reg_cost=copy(err)
# combCost.m:162
        pred_x=predict(model_x,t.T)
# combCost.m:164
        pred_y=predict(model_y,t.T)
# combCost.m:165
        smooth_size=predict(model_bbox,t.T)
# combCost.m:166
        t_min=min(t)
# combCost.m:167
        t_max=max(t)
# combCost.m:168
        t_t=arange(t_min,t_max)
# combCost.m:169
        #     pred_x_t = predict(model_x,t');
#     pred_y_t = predict(model_y,t');
        pred_x_t=interp1(t,pred_x.T,t_t,'linear')
# combCost.m:173
        pred_y_t=interp1(t,pred_y.T,t_t,'linear')
# combCost.m:174
        pred_size_t=interp1(t,smooth_size,t_t,'linear')
# combCost.m:175
        ax=pred_x_t(arange(3,end())) + pred_x_t(arange(1,end() - 2)) - dot(2,pred_x_t(arange(2,end() - 1)))
# combCost.m:177
        ay=pred_y_t(arange(3,end())) + pred_y_t(arange(1,end() - 2)) - dot(2,pred_y_t(arange(2,end() - 1)))
# combCost.m:178
        if isempty(ax):
            grad_cost=0
# combCost.m:180
        else:
            acc_err=sqrt(ax ** 2 + ay ** 2) / pred_size_t(arange(2,end() - 1))
# combCost.m:182
            t_interval=t_t(arange(2,end() - 1))
# combCost.m:183
            max_grad=zeros(size(end_t))
# combCost.m:184
            for n in arange(1,length(end_t)).reshape(-1):
                temp_idx=find(t_interval == end_t(n))
# combCost.m:186
                min_idx=max(1,temp_idx - 3)
# combCost.m:187
                max_idx=min(length(t_interval),temp_idx + 3)
# combCost.m:188
                max_grad[n]=max(acc_err(arange(min_idx,max_idx)))
# combCost.m:189
            grad_cost=sum(max_grad)
# combCost.m:191
            #         grad_cost = cluster_params.lambda_grad*sum(acc_err(acc_err>2e-3));#max(max(abs(ax)),max(abs(ay)))^2;#max(sqrt(ax.^2+ay.^2));
        #     if length(train_t)>100
#         figure, plot(t,pred_x,'r.',t,det_x,'k.')
#         figure, plot(t_t(2:end-1),acc_err,'b');
#         close all
#     end
    
    # color cost
    color_cost=0
# combCost.m:204
    if color_flag == 1:
        max_diff_color=max(diff_mean_color)
# combCost.m:206
        color_cost=sum(max_diff_color)
# combCost.m:207
    
    if nargin > 3:
        color_cost=copy(appearance_cost)
# combCost.m:210
    
    # time cost
    track_dist=track_interval(track_set(sort_idx(arange(2,end()))),1) - track_interval(track_set(sort_idx(arange(1,end() - 1))),2)
# combCost.m:214
    max_dist=max(track_dist)
# combCost.m:215
    if isempty(max_dist) or max_dist <= 0:
        time_cost=0
# combCost.m:217
    else:
        time_cost=(max_dist ** 3) / 1000000.0
# combCost.m:219
    
    # cost = cluster_params.split_cost*split_cost+cluster_params.lambda_reg*reg_cost+...
#     cluster_params.lambda_color*color_cost+cluster_params.lambda_grad*grad_cost+...
#     cluster_params.lambda_time*time_cost;
    f=concat([split_cost,reg_cost,color_cost,grad_cost,time_cost])
# combCost.m:225