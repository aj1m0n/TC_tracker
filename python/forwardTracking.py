# Generated with SMOP  0.41
from libsmop import *
# forwardTracking.m

    
@function
def forwardTracking(track_obj1=None,track_obj2=None,track_params=None,fr_idx2=None,tracklet_mat=None,img1=None,img2=None,*args,**kwargs):
    varargin = forwardTracking.varargin
    nargin = forwardTracking.nargin

    new_track_params=copy(track_params)
# forwardTracking.m:4
    new_track_obj1=copy(track_obj1)
# forwardTracking.m:5
    new_track_obj2=copy(track_obj2)
# forwardTracking.m:6
    new_tracklet_mat=copy(tracklet_mat)
# forwardTracking.m:7
    if new_track_params.max_track_id == 0:
        new_track_obj1.track_id = copy(arange(1,size(new_track_obj1.bbox,1)))
# forwardTracking.m:10
        track_params.max_track_id = copy(size(new_track_obj1.bbox,1))
# forwardTracking.m:11
        new_track_params.max_track_id = copy(track_params.max_track_id)
# forwardTracking.m:12
        new_tracklet_mat.xmin_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr)))
# forwardTracking.m:13
        new_tracklet_mat.ymin_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr)))
# forwardTracking.m:14
        new_tracklet_mat.xmax_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr)))
# forwardTracking.m:15
        new_tracklet_mat.ymax_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr)))
# forwardTracking.m:16
        new_tracklet_mat.color_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr,3)))
# forwardTracking.m:17
        new_tracklet_mat.class_mat = copy(cell(size(new_track_obj1.bbox,1),new_track_params.num_fr))
# forwardTracking.m:18
        new_tracklet_mat.det_score_mat = copy(dot(- 1,ones(size(new_track_obj1.bbox,1),new_track_params.num_fr)))
# forwardTracking.m:19
        new_tracklet_mat.mask_flag = copy(new_track_obj1.mask_flag)
# forwardTracking.m:20
        for n in arange(1,size(new_track_obj1.bbox,1)).reshape(-1):
            new_tracklet_mat.xmin_mat[n,fr_idx2 - 1]=new_track_obj1.bbox(n,1)
# forwardTracking.m:22
            new_tracklet_mat.ymin_mat[n,fr_idx2 - 1]=new_track_obj1.bbox(n,2)
# forwardTracking.m:23
            new_tracklet_mat.xmax_mat[n,fr_idx2 - 1]=new_track_obj1.bbox(n,1) + new_track_obj1.bbox(n,3) - 1
# forwardTracking.m:24
            new_tracklet_mat.ymax_mat[n,fr_idx2 - 1]=new_track_obj1.bbox(n,2) + new_track_obj1.bbox(n,4) - 1
# forwardTracking.m:26
            bbox_img=img1(arange(new_tracklet_mat.ymin_mat(n,fr_idx2 - 1),new_tracklet_mat.ymax_mat(n,fr_idx2 - 1)),arange(new_tracklet_mat.xmin_mat(n,fr_idx2 - 1),new_tracklet_mat.xmax_mat(n,fr_idx2 - 1)),arange())
# forwardTracking.m:29
            new_tracklet_mat.color_mat[n,fr_idx2 - 1,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:31
            new_tracklet_mat.color_mat[n,fr_idx2 - 1,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:32
            new_tracklet_mat.color_mat[n,fr_idx2 - 1,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:33
            new_tracklet_mat.class_mat[n,fr_idx2 - 1]=new_track_obj1.det_class(n)
# forwardTracking.m:35
            new_tracklet_mat.det_score_mat[n,fr_idx2 - 1]=new_track_obj1.det_score(n)
# forwardTracking.m:37
    
    # linear prediction
    track_id1=new_track_obj1.track_id
# forwardTracking.m:42
    pred_bbox1=zeros(length(track_id1),4)
# forwardTracking.m:43
    for n in arange(1,length(track_id1)).reshape(-1):
        temp_t=find(new_tracklet_mat.xmin_mat(track_id1(n),arange()) >= 0)
# forwardTracking.m:45
        if length(temp_t) > 10:
            temp_t=temp_t(arange(end() - 9,end()))
# forwardTracking.m:47
        pred_xmin=linearPred(temp_t,new_tracklet_mat.xmin_mat(track_id1(n),temp_t),fr_idx2)
# forwardTracking.m:49
        pred_xmax=linearPred(temp_t,new_tracklet_mat.xmax_mat(track_id1(n),temp_t),fr_idx2)
# forwardTracking.m:50
        pred_ymin=linearPred(temp_t,new_tracklet_mat.ymin_mat(track_id1(n),temp_t),fr_idx2)
# forwardTracking.m:51
        pred_ymax=linearPred(temp_t,new_tracklet_mat.ymax_mat(track_id1(n),temp_t),fr_idx2)
# forwardTracking.m:52
        pred_bbox1[n,arange()]=concat([pred_xmin,pred_ymin,pred_xmax - pred_xmin + 1,pred_ymax - pred_ymin + 1])
# forwardTracking.m:53
    
    out_idx1=find(new_track_obj1.mask_flag < 0.5)
# forwardTracking.m:56
    in_idx1=find(new_track_obj1.mask_flag > 0.5)
# forwardTracking.m:57
    out_idx2=find(new_track_obj2.mask_flag < 0.5)
# forwardTracking.m:58
    in_idx2=find(new_track_obj2.mask_flag > 0.5)
# forwardTracking.m:59
    out_bbox1=new_track_obj1.bbox(out_idx1,arange())
# forwardTracking.m:60
    in_bbox1=new_track_obj1.bbox(in_idx1,arange())
# forwardTracking.m:61
    pred_out_bbox1=pred_bbox1(out_idx1,arange())
# forwardTracking.m:62
    pred_in_bbox1=pred_bbox1(in_idx1,arange())
# forwardTracking.m:63
    out_bbox2=new_track_obj2.bbox(out_idx2,arange())
# forwardTracking.m:64
    in_bbox2=new_track_obj2.bbox(in_idx2,arange())
# forwardTracking.m:65
    N_out_bbox1=size(out_bbox1,1)
# forwardTracking.m:66
    N_in_bbox1=size(in_bbox1,1)
# forwardTracking.m:67
    N_out_bbox2=size(out_bbox2,1)
# forwardTracking.m:68
    N_in_bbox2=size(in_bbox2,1)
# forwardTracking.m:69
    out_bbox_color1=zeros(N_out_bbox1,3)
# forwardTracking.m:70
    in_bbox_color1=zeros(N_in_bbox1,3)
# forwardTracking.m:71
    out_bbox_color2=zeros(N_out_bbox2,3)
# forwardTracking.m:72
    in_bbox_color2=zeros(N_in_bbox2,3)
# forwardTracking.m:73
    for n in arange(1,N_out_bbox1).reshape(-1):
        bbox_img=img1(arange(out_bbox1(n,2),out_bbox1(n,2) + out_bbox1(n,4) - 1),arange(out_bbox1(n,1),out_bbox1(n,1) + out_bbox1(n,3) - 1),arange())
# forwardTracking.m:75
        out_bbox_color1[n,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:76
        out_bbox_color1[n,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:77
        out_bbox_color1[n,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:78
    
    for n in arange(1,N_in_bbox1).reshape(-1):
        bbox_img=img1(arange(in_bbox1(n,2),in_bbox1(n,2) + in_bbox1(n,4) - 1),arange(in_bbox1(n,1),in_bbox1(n,1) + in_bbox1(n,3) - 1),arange())
# forwardTracking.m:81
        in_bbox_color1[n,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:82
        in_bbox_color1[n,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:83
        in_bbox_color1[n,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:84
    
    for n in arange(1,N_out_bbox2).reshape(-1):
        bbox_img=img2(arange(out_bbox2(n,2),out_bbox2(n,2) + out_bbox2(n,4) - 1),arange(out_bbox2(n,1),out_bbox2(n,1) + out_bbox2(n,3) - 1),arange())
# forwardTracking.m:87
        out_bbox_color2[n,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:88
        out_bbox_color2[n,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:89
        out_bbox_color2[n,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:90
    
    for n in arange(1,N_in_bbox2).reshape(-1):
        #     n = logical(n);
#     disp(in_bbox2(n,1));
#     disp(in_bbox2(n,2));
#     disp(in_bbox2(n,3));
#     disp(in_bbox2(n,4));
        bbox_img=img2(arange(in_bbox2(n,2),in_bbox2(n,2) + in_bbox2(n,4) - 1),arange(in_bbox2(n,1),in_bbox2(n,1) + in_bbox2(n,3) - 1),arange())
# forwardTracking.m:98
        in_bbox_color2[n,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:99
        in_bbox_color2[n,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:100
        in_bbox_color2[n,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:101
    
    D_r_out=pdist2(out_bbox_color1(arange(),1),out_bbox_color2(arange(),1))
# forwardTracking.m:103
    D_g_out=pdist2(out_bbox_color1(arange(),2),out_bbox_color2(arange(),2))
# forwardTracking.m:104
    D_b_out=pdist2(out_bbox_color1(arange(),3),out_bbox_color2(arange(),3))
# forwardTracking.m:105
    D_max_out=max(max(D_r_out,D_g_out),D_b_out)
# forwardTracking.m:106
    D_r_in=pdist2(in_bbox_color1(arange(),1),in_bbox_color2(arange(),1))
# forwardTracking.m:107
    D_g_in=pdist2(in_bbox_color1(arange(),2),in_bbox_color2(arange(),2))
# forwardTracking.m:108
    D_b_in=pdist2(in_bbox_color1(arange(),3),in_bbox_color2(arange(),3))
# forwardTracking.m:109
    D_max_in=max(max(D_r_in,D_g_in),D_b_in)
# forwardTracking.m:110
    mask_out=double(D_max_out < new_track_params.color_thresh)
# forwardTracking.m:111
    mask_in=double(D_max_in < new_track_params.color_thresh)
# forwardTracking.m:112
    track_id2=zeros(1,N_out_bbox2 + N_in_bbox2)
# forwardTracking.m:115
    out_bbox1_idx,out_bbox2_idx,out_overlap_mat=bboxAssociate(pred_out_bbox1,out_bbox2,new_track_params.overlap_thresh2,new_track_params.lb_thresh,mask_out,nargout=3)
# forwardTracking.m:117
    new_track_obj1.out_overlap_mat = copy(out_overlap_mat)
# forwardTracking.m:119
    track_id2[out_idx2(out_bbox2_idx)]=track_id1(out_idx1(out_bbox1_idx))
# forwardTracking.m:120
    in_bbox1_idx,in_bbox2_idx,in_overlap_mat=bboxAssociate(pred_in_bbox1,in_bbox2,new_track_params.overlap_thresh1,new_track_params.lb_thresh,mask_in,nargout=3)
# forwardTracking.m:122
    new_track_obj1.in_overlap_mat = copy(in_overlap_mat)
# forwardTracking.m:124
    track_id2[in_idx2(in_bbox2_idx)]=track_id1(in_idx1(in_bbox1_idx))
# forwardTracking.m:125
    for n in arange(1,(N_out_bbox2 + N_in_bbox2)).reshape(-1):
        if track_id2(n) == 0:
            track_id2[n]=new_track_params.max_track_id + 1
# forwardTracking.m:129
            new_track_params.max_track_id = copy(new_track_params.max_track_id + 1)
# forwardTracking.m:130
    
    new_track_obj2.track_id = copy(track_id2)
# forwardTracking.m:133
    if new_track_params.max_track_id > track_params.max_track_id:
        new_tracklet_mat.xmin_mat = copy(concat([[new_tracklet_mat.xmin_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.xmin_mat,2)))]]))
# forwardTracking.m:136
        new_tracklet_mat.ymin_mat = copy(concat([[new_tracklet_mat.ymin_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.ymin_mat,2)))]]))
# forwardTracking.m:138
        new_tracklet_mat.xmax_mat = copy(concat([[new_tracklet_mat.xmax_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.xmax_mat,2)))]]))
# forwardTracking.m:140
        new_tracklet_mat.ymax_mat = copy(concat([[new_tracklet_mat.ymax_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.ymax_mat,2)))]]))
# forwardTracking.m:142
        new_tracklet_mat.color_mat = copy(concat([[new_tracklet_mat.color_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.color_mat,2),3))]]))
# forwardTracking.m:144
        new_tracklet_mat.class_mat = copy(concat([[new_tracklet_mat.class_mat],[cell(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.class_mat,2))]]))
# forwardTracking.m:146
        new_tracklet_mat.det_score_mat = copy(concat([[new_tracklet_mat.det_score_mat],[dot(- 1,ones(new_track_params.max_track_id - track_params.max_track_id,size(new_tracklet_mat.det_score_mat,2)))]]))
# forwardTracking.m:148
    
    for n in arange(1,(N_out_bbox2 + N_in_bbox2)).reshape(-1):
        #     n = logical(n);
        new_tracklet_mat.xmin_mat[track_id2(n),fr_idx2]=new_track_obj2.bbox(n,1)
# forwardTracking.m:153
        new_tracklet_mat.ymin_mat[track_id2(n),fr_idx2]=new_track_obj2.bbox(n,2)
# forwardTracking.m:154
        new_tracklet_mat.xmax_mat[track_id2(n),fr_idx2]=new_track_obj2.bbox(n,1) + new_track_obj2.bbox(n,3) - 1
# forwardTracking.m:155
        new_tracklet_mat.ymax_mat[track_id2(n),fr_idx2]=new_track_obj2.bbox(n,2) + new_track_obj2.bbox(n,4) - 1
# forwardTracking.m:156
        bbox_img=img2(arange(new_tracklet_mat.ymin_mat(track_id2(n),fr_idx2),new_tracklet_mat.ymax_mat(track_id2(n),fr_idx2)),arange(new_tracklet_mat.xmin_mat(track_id2(n),fr_idx2),new_tracklet_mat.xmax_mat(track_id2(n),fr_idx2)),arange())
# forwardTracking.m:158
        new_tracklet_mat.color_mat[track_id2(n),fr_idx2,1]=mean(mean(bbox_img(arange(),arange(),1)))
# forwardTracking.m:160
        new_tracklet_mat.color_mat[track_id2(n),fr_idx2,2]=mean(mean(bbox_img(arange(),arange(),2)))
# forwardTracking.m:161
        new_tracklet_mat.color_mat[track_id2(n),fr_idx2,3]=mean(mean(bbox_img(arange(),arange(),3)))
# forwardTracking.m:162
        new_tracklet_mat.class_mat[track_id2(n),fr_idx2]=new_track_obj2.det_class(n)
# forwardTracking.m:164
        new_tracklet_mat.det_score_mat[track_id2(n),fr_idx2]=new_track_obj2.det_score(n)
# forwardTracking.m:166
        new_tracklet_mat.mask_flag[track_id2(n)]=new_track_obj2.mask_flag(n)
# forwardTracking.m:168
    
    # bbox1 = new_track_obj1.bbox;
# bbox2 = new_track_obj2.bbox;
# N_bbox1 = size(bbox1,1);
# N_bbox2 = size(bbox2,1);
# bbox_color1 = zeros(N_bbox1,3);
# bbox_color2 = zeros(N_bbox2,3);
# for n = 1:N_bbox1
#     bbox_img = img1(bbox1(n,2):bbox1(n,2)+bbox1(n,4)-1,bbox1(n,1):bbox1(n,1)+bbox1(n,3)-1,:);
#     bbox_color1(n,1) =  mean(mean(bbox_img(:,:,1)));
#     bbox_color1(n,2) =  mean(mean(bbox_img(:,:,2)));
#     bbox_color1(n,3) =  mean(mean(bbox_img(:,:,3)));
# end
# for n = 1:N_bbox2
#     bbox_img = img2(bbox2(n,2):bbox2(n,2)+bbox2(n,4)-1,bbox2(n,1):bbox2(n,1)+bbox2(n,3)-1,:);
#     bbox_color2(n,1) =  mean(mean(bbox_img(:,:,1)));
#     bbox_color2(n,2) =  mean(mean(bbox_img(:,:,2)));
#     bbox_color2(n,3) =  mean(mean(bbox_img(:,:,3)));
# end
# D_r = pdist2(bbox_color1(:,1),bbox_color2(:,1));
# D_g = pdist2(bbox_color1(:,2),bbox_color2(:,2));
# D_b = pdist2(bbox_color1(:,3),bbox_color2(:,3));
# D_max = max(max(D_r,D_g),D_b);
# mask = double(D_max<new_track_params.color_thresh);
# 
# track_id1 = new_track_obj1.track_id;
# [bbox1_idx, bbox2_idx, overlap_mat] = bboxAssociate(bbox1, bbox2,...
#     new_track_params.overlap_thresh, new_track_params.lb_thresh, mask);
# new_track_obj1.overlap_mat = overlap_mat;
# track_id2 = zeros(1,size(bbox2,1));
# track_id2(bbox2_idx) = track_id1(bbox1_idx);
# for n = 1:size(bbox2,1)
#     if track_id2(n)==0
#         track_id2(n) = new_track_params.max_track_id+1;
#         new_track_params.max_track_id = new_track_params.max_track_id+1;
#     end
# end
# new_track_obj2.track_id = track_id2;
# 
# 
# if new_track_params.max_track_id>track_params.max_track_id
#     new_tracklet_mat.xmin_mat = [new_tracklet_mat.xmin_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.xmin_mat,2))];
#     new_tracklet_mat.ymin_mat = [new_tracklet_mat.ymin_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.ymin_mat,2))];
#     new_tracklet_mat.xmax_mat = [new_tracklet_mat.xmax_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.xmax_mat,2))];
#     new_tracklet_mat.ymax_mat = [new_tracklet_mat.ymax_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.ymax_mat,2))];
#     new_tracklet_mat.color_mat = [new_tracklet_mat.color_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.color_mat,2),3)];
#     new_tracklet_mat.class_mat = [new_tracklet_mat.class_mat;...
#         cell(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.class_mat,2))];
#     new_tracklet_mat.det_score_mat = [new_tracklet_mat.det_score_mat;...
#         -1*ones(new_track_params.max_track_id-track_params.max_track_id,size(new_tracklet_mat.det_score_mat,2))];
# end
# for n = 1:size(bbox2,1)
#     new_tracklet_mat.xmin_mat(track_id2(n),fr_idx2) = bbox2(n,1);
#     new_tracklet_mat.ymin_mat(track_id2(n),fr_idx2) = bbox2(n,2);
#     new_tracklet_mat.xmax_mat(track_id2(n),fr_idx2) = bbox2(n,1)+bbox2(n,3)-1;
#     new_tracklet_mat.ymax_mat(track_id2(n),fr_idx2) = bbox2(n,2)+bbox2(n,4)-1;
#     
#     bbox_img = img2(new_tracklet_mat.ymin_mat(track_id2(n),fr_idx2):new_tracklet_mat.ymax_mat(track_id2(n),fr_idx2),...
#         new_tracklet_mat.xmin_mat(track_id2(n),fr_idx2):new_tracklet_mat.xmax_mat(track_id2(n),fr_idx2),:);
#     new_tracklet_mat.color_mat(track_id2(n),fr_idx2,1) = mean(mean(bbox_img(:,:,1)));
#     new_tracklet_mat.color_mat(track_id2(n),fr_idx2,2) = mean(mean(bbox_img(:,:,2)));
#     new_tracklet_mat.color_mat(track_id2(n),fr_idx2,3) = mean(mean(bbox_img(:,:,3)));
#     
#     new_tracklet_mat.class_mat{track_id2(n),fr_idx2} = new_track_obj2.det_class(n);
#     
#     new_tracklet_mat.det_score_mat(track_id2(n),fr_idx2) = new_track_obj2.det_score(n);
# end