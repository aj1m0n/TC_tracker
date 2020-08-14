# Generated with SMOP  0.41
from libsmop import *
# preprocessing.m

    
@function
def preprocessing(tracklet_mat=None,len_thresh=None,*args,**kwargs):
    varargin = preprocessing.varargin
    nargin = preprocessing.nargin

    new_tracklet_mat=copy(tracklet_mat)
# preprocessing.m:3
    N_tracklet=size(tracklet_mat.xmin_mat,1)
# preprocessing.m:4
    remove_idx=[]
# preprocessing.m:5
    for n in arange(1,N_tracklet).reshape(-1):
        t=find(tracklet_mat.xmin_mat(n,arange()) >= 0)
# preprocessing.m:7
        if length(t) < len_thresh:
            remove_idx=concat([remove_idx,n])
# preprocessing.m:9
    
    new_tracklet_mat.mask_flag[remove_idx]=0
# preprocessing.m:13
    # new_tracklet_mat.xmin_mat(remove_idx,:) = [];
# new_tracklet_mat.ymin_mat(remove_idx,:) = [];
# new_tracklet_mat.xmax_mat(remove_idx,:) = [];
# new_tracklet_mat.ymax_mat(remove_idx,:) = [];
# new_tracklet_mat.color_mat(remove_idx,:,:) = [];
# new_tracklet_mat.class_mat(remove_idx,:) = [];
# new_tracklet_mat.det_score_mat(remove_idx,:) = [];