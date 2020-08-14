# Generated with SMOP  0.41
from libsmop import *
# TC_tracker.m

    # Copyright (C)2018, Gaoang Wang, All rights reserved.
    
@function
def TC_tracker(img_folder=None,det_path=None,ROI_path=None,param=None,save_path=None,seq_name=None,result_save_path=None,video_save_path=None,*args,**kwargs):
    print("HOGEHOGE")
    varargin = TC_tracker.varargin
    nargin = TC_tracker.nargin
    print("HOGEHOGE2")
    tic
    rand_color=rand(1500,3)
    print("HOGEHOGE3")    
# TC_tracker.m:5
    img_list=dir(img_folder+'/*.jpg')
    print("HOGEHOGE4")
# TC_tracker.m:6
    if isempty(ROI_path):
        temp_img=imread(concat([img_folder,'/',img_list(1).name]))
# TC_tracker.m:8
        mask=ones(size(temp_img,1),size(temp_img,2))
# TC_tracker.m:9
    else:
        mask=im2double(imread(ROI_path))
# TC_tracker.m:11
    ## read detection file
    fileID=fopen(det_path,'r')
# TC_tracker.m:15
    A=textscan(fileID,'%d %d %d %d %d %d %f %d %d %d %s','Delimiter',',')
# TC_tracker.m:16
    fclose(fileID)
    M=zeros(size(A[1],1),10)
# TC_tracker.m:18
    for n in arange(1,10).reshape(-1):
        M[arange(),n]=A[n]
# TC_tracker.m:20
    
    M[arange(),1]=M(arange(),1) + 1
# TC_tracker.m:22
    M[arange(),3]=M(arange(),3) + 1
# TC_tracker.m:23
    M[arange(),4]=M(arange(),4) + 1
# TC_tracker.m:24
    track_params.img_size = copy(size(mask))
# TC_tracker.m:27
    track_params.num_fr = copy(length(img_list))
# TC_tracker.m:28
    track_params.const_fr_thresh = copy(10)
# TC_tracker.m:29
    track_params.overlap_thresh1 = copy(param.IOU_thresh)
# TC_tracker.m:30
    track_params.overlap_thresh2 = copy(0.8)
# TC_tracker.m:31
    track_params.lb_thresh = copy(0.3)
# TC_tracker.m:32
    track_params.max_track_id = copy(0)
# TC_tracker.m:33
    track_params.color_thresh = copy(param.color_thresh)
# TC_tracker.m:34
    track_params.det_score_thresh = copy(param.det_score_thresh)
# TC_tracker.m:35
    track_struct.track_params = copy(track_params)
# TC_tracker.m:36
    track_struct.tracklet_mat = copy([])
# TC_tracker.m:37
    track_struct.track_obj = copy(cell(1,track_params.num_fr))
# TC_tracker.m:38
    M[arange(),5]=min(M(arange(),5),track_params.img_size(2) - M(arange(),3) + 1)
# TC_tracker.m:39
    M[arange(),6]=min(M(arange(),6),track_params.img_size(1) - M(arange(),4) + 1)
# TC_tracker.m:40
    for n in arange(1,track_params.num_fr).reshape(-1):
        idx=find(M(arange(),1) == logical_and(n,M(arange(),7)) > track_params.det_score_thresh)
# TC_tracker.m:42
        det_bbox=M(idx,arange(3,6))
# TC_tracker.m:43
        __,choose_idx=mergeBBox(det_bbox,0.8,M(idx,7),nargout=2)
# TC_tracker.m:44
        idx=idx(choose_idx)
# TC_tracker.m:45
        mask_flag=ones(length(idx),1)
# TC_tracker.m:48
        left_pts=round(concat([M(idx,3),M(idx,4) + M(idx,6) - 1]))
# TC_tracker.m:49
        right_pts=round(concat([M(idx,3) + M(idx,5) - 1,M(idx,4) + M(idx,6) - 1]))
# TC_tracker.m:50
        #     left_pts = max(left_pts,1);
#     left_pts(:,1) = min(left_pts(:,1),track_params.img_size(2));
#     left_pts(:,2) = min(left_pts(:,2),track_params.img_size(1));
#     right_pts = max(right_pts,1);
#     right_pts(:,1) = min(right_pts(:,1),track_params.img_size(2));
#     right_pts(:,2) = min(right_pts(:,2),track_params.img_size(1));
        right_idx=dot((right_pts(arange(),1) - 1),track_params.img_size(1)) + right_pts(arange(),2)
# TC_tracker.m:58
        left_idx=dot((left_pts(arange(),1) - 1),track_params.img_size(1)) + left_pts(arange(),2)
# TC_tracker.m:59
        right_idx[right_idx < 0]=1
# TC_tracker.m:61
        left_idx[left_idx < 0]=1
# TC_tracker.m:62
        out_idx=find(mask(right_idx) < logical_or(0.5,mask(left_idx)) < 0.5)
# TC_tracker.m:63
        mask_flag[out_idx]=0
# TC_tracker.m:64
        det_score=M(idx,7)
# TC_tracker.m:66
        mask_flag[det_score < track_params.det_score_thresh]=0
# TC_tracker.m:67
        track_struct.track_obj[n].track_id = copy([])
# TC_tracker.m:69
        if isempty(idx):
            track_struct.track_obj[n].bbox = copy([])
# TC_tracker.m:71
            track_struct.track_obj[n].det_class = copy([])
# TC_tracker.m:72
            track_struct.track_obj[n].det_score = copy([])
# TC_tracker.m:73
            track_struct.track_obj[n].mask_flag = copy([])
# TC_tracker.m:74
            continue
        track_struct.track_obj[n].bbox = copy(M(idx,arange(3,6)))
# TC_tracker.m:77
        track_struct.track_obj[n].det_class = copy(A[11](idx))
# TC_tracker.m:78
        track_struct.track_obj[n].det_score = copy(M(idx,7) / 100)
# TC_tracker.m:79
        track_struct.track_obj[n].mask_flag = copy(mask_flag)
# TC_tracker.m:80
    
    ## forward tracking
    for n in arange(1,track_params.num_fr - 1).reshape(-1):
        if n == 1:
            img_path=concat([img_folder,'/',img_list(n).name])
# TC_tracker.m:86
            img1=im2double(imread(img_path))
# TC_tracker.m:87
        img_path=concat([img_folder,'/',img_list(n + 1).name])
# TC_tracker.m:89
        img2=im2double(imread(img_path))
# TC_tracker.m:90
        track_struct.track_obj[n],track_struct.track_obj[n + 1],track_struct.tracklet_mat,track_struct.track_params=forwardTracking(track_struct.track_obj[n],track_struct.track_obj[n + 1],track_struct.track_params,n + 1,track_struct.tracklet_mat,img1,img2,nargout=4)
# TC_tracker.m:91
        img1=copy(img2)
# TC_tracker.m:94
    
    ## tracklet clustering
    iters=10
# TC_tracker.m:98
    track_struct.tracklet_mat = copy(preprocessing(track_struct.tracklet_mat,5))
# TC_tracker.m:99
    for n in arange(1,iters).reshape(-1):
        track_struct.tracklet_mat,flag,__=trackletClusterInit(track_struct.tracklet_mat,param,nargout=3)
# TC_tracker.m:101
        if flag == 1:
            break
    
    track_struct.prev_tracklet_mat,track_struct.tracklet_mat=postProcessing(track_struct.tracklet_mat,track_struct.track_params,nargout=2)
# TC_tracker.m:106
    ## Gaussian regression for smoothness
    sigma=8
# TC_tracker.m:109
    remove_idx=[]
# TC_tracker.m:110
    N_tracklet=size(track_struct.tracklet_mat.xmin_mat,1)
# TC_tracker.m:111
    xmin_reg=cell(1,N_tracklet)
# TC_tracker.m:112
    ymin_reg=cell(1,N_tracklet)
# TC_tracker.m:113
    xmax_reg=cell(1,N_tracklet)
# TC_tracker.m:114
    ymax_reg=cell(1,N_tracklet)
# TC_tracker.m:115
    for n in arange(1,N_tracklet).reshape(-1):
        det_idx=find(track_struct.tracklet_mat.xmin_mat(n,arange()) >= 0)
# TC_tracker.m:117
        if length(det_idx) < track_struct.track_params.const_fr_thresh:
            remove_idx=concat([remove_idx,n])
# TC_tracker.m:119
            continue
        # bbox regression
        xmin_reg[n]=fitrgp(det_idx.T,track_struct.tracklet_mat.xmin_mat(n,det_idx).T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# TC_tracker.m:124
        ymin_reg[n]=fitrgp(det_idx.T,track_struct.tracklet_mat.ymin_mat(n,det_idx).T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# TC_tracker.m:126
        xmax_reg[n]=fitrgp(det_idx.T,track_struct.tracklet_mat.xmax_mat(n,det_idx).T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# TC_tracker.m:128
        ymax_reg[n]=fitrgp(det_idx.T,track_struct.tracklet_mat.ymax_mat(n,det_idx).T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# TC_tracker.m:130
        t_min=min(det_idx)
# TC_tracker.m:132
        t_max=max(det_idx)
# TC_tracker.m:133
        track_struct.tracklet_mat.xmin_mat[n,arange(t_min,t_max)]=predict(xmin_reg[n],(arange(t_min,t_max)).T).T
# TC_tracker.m:134
        track_struct.tracklet_mat.ymin_mat[n,arange(t_min,t_max)]=predict(ymin_reg[n],(arange(t_min,t_max)).T).T
# TC_tracker.m:135
        track_struct.tracklet_mat.xmax_mat[n,arange(t_min,t_max)]=predict(xmax_reg[n],(arange(t_min,t_max)).T).T
# TC_tracker.m:136
        track_struct.tracklet_mat.ymax_mat[n,arange(t_min,t_max)]=predict(ymax_reg[n],(arange(t_min,t_max)).T).T
# TC_tracker.m:137
    
    track_struct.tracklet_mat.xmin_mat[remove_idx,arange()]=[]
# TC_tracker.m:139
    track_struct.tracklet_mat.ymin_mat[remove_idx,arange()]=[]
# TC_tracker.m:140
    track_struct.tracklet_mat.xmax_mat[remove_idx,arange()]=[]
# TC_tracker.m:141
    track_struct.tracklet_mat.ymax_mat[remove_idx,arange()]=[]
# TC_tracker.m:142
    track_struct.tracklet_mat.color_mat[remove_idx,arange(),arange()]=[]
# TC_tracker.m:143
    track_struct.tracklet_mat.class_mat[remove_idx,arange()]=[]
# TC_tracker.m:144
    track_struct.tracklet_mat.det_score_mat[remove_idx,arange()]=[]
# TC_tracker.m:145
    time_use=copy(toc)
# TC_tracker.m:146
    run_speed=track_params.num_fr / time_use
# TC_tracker.m:147
    if logical_not(isempty(seq_name)):
        save(concat([result_save_path,'/',seq_name,'.mat']),'track_struct')
    
    ## plot tracking result
    if exist(save_path,'dir') <= 0:
        mkdir(save_path)
    
    for t in arange(1,track_params.num_fr).reshape(-1):
        img_name=img_list(t).name
# TC_tracker.m:157
        img=imread(concat([img_folder,'/',img_name]))
# TC_tracker.m:158
        figure
        imshow(img)
        hold('on')
        for n in arange(1,size(track_struct.tracklet_mat.xmin_mat,1)).reshape(-1):
            if track_struct.tracklet_mat.xmin_mat(n,t) == - 1:
                continue
            x_min=track_struct.tracklet_mat.xmin_mat(n,t)
# TC_tracker.m:164
            y_min=track_struct.tracklet_mat.ymin_mat(n,t)
# TC_tracker.m:165
            x_max=track_struct.tracklet_mat.xmax_mat(n,t)
# TC_tracker.m:166
            y_max=track_struct.tracklet_mat.ymax_mat(n,t)
# TC_tracker.m:167
            plot(concat([x_min,x_min]),concat([y_min,y_max]),'Color',rand_color(n,arange()),'LineWidth',1)
            hold('on')
            plot(concat([x_min,x_max]),concat([y_min,y_min]),'Color',rand_color(n,arange()),'LineWidth',1)
            hold('on')
            plot(concat([x_min,x_max]),concat([y_max,y_max]),'Color',rand_color(n,arange()),'LineWidth',1)
            hold('on')
            plot(concat([x_max,x_max]),concat([y_min,y_max]),'Color',rand_color(n,arange()),'LineWidth',1)
            hold('on')
            text(x_min,y_min - 20,num2str(n),'FontSize',20,'Color',rand_color(n,arange()))
        saveas(gcf,concat([save_path,'/',img_list(t).name]))
        close_('all')
    
    fr2video(concat([save_path,'/']),concat([video_save_path,'/',seq_name,'.avi']),25)
    ## write results
    if logical_not(isempty(seq_name)):
        writeTxt(seq_name,result_save_path,result_save_path,'MOT')
        file_name=concat([result_save_path,'/',seq_name,'_Speed.txt'])
# TC_tracker.m:182
        fileID=fopen(file_name,'w')
# TC_tracker.m:183
        fprintf(fileID,'%f',run_speed)
        fclose(fileID)
    