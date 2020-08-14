# Generated with SMOP  0.41
from libsmop import *
# updateTrackletMat.m

    
@function
def updateTrackletMat(tracklet_mat=None,*args,**kwargs):
    varargin = updateTrackletMat.varargin
    nargin = updateTrackletMat.nargin

    new_tracklet_mat=copy(tracklet_mat)
# updateTrackletMat.m:3
    track_interval=tracklet_mat.track_interval
# updateTrackletMat.m:4
    num_cluster=sum(tracklet_mat.cluster_flag)
# updateTrackletMat.m:5
    new_xmin_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2)))
# updateTrackletMat.m:7
    new_ymin_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2)))
# updateTrackletMat.m:8
    new_xmax_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2)))
# updateTrackletMat.m:9
    new_ymax_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2)))
# updateTrackletMat.m:10
    new_color_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2),3))
# updateTrackletMat.m:11
    new_class_mat=cell(num_cluster,size(new_tracklet_mat.xmin_mat,2))
# updateTrackletMat.m:12
    new_det_score_mat=dot(- 1,ones(num_cluster,size(new_tracklet_mat.xmin_mat,2)))
# updateTrackletMat.m:13
    for n in arange(1,num_cluster).reshape(-1):
        for k in arange(1,length(new_tracklet_mat.track_cluster[n])).reshape(-1):
            temp_id=new_tracklet_mat.track_cluster[n](k)
# updateTrackletMat.m:18
            new_xmin_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.xmin_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:19
            new_ymin_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.ymin_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:21
            new_xmax_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.xmax_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:23
            new_ymax_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.ymax_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:25
            new_color_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2)),arange()]=new_tracklet_mat.color_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)),arange())
# updateTrackletMat.m:28
            new_class_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.class_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:31
            new_det_score_mat[n,arange(track_interval(temp_id,1),track_interval(temp_id,2))]=new_tracklet_mat.det_score_mat(temp_id,arange(track_interval(temp_id,1),track_interval(temp_id,2)))
# updateTrackletMat.m:34
    
    new_tracklet_mat.xmin_mat = copy(new_xmin_mat)
# updateTrackletMat.m:38
    new_tracklet_mat.ymin_mat = copy(new_ymin_mat)
# updateTrackletMat.m:39
    new_tracklet_mat.xmax_mat = copy(new_xmax_mat)
# updateTrackletMat.m:40
    new_tracklet_mat.ymax_mat = copy(new_ymax_mat)
# updateTrackletMat.m:41
    new_tracklet_mat.color_mat = copy(new_color_mat)
# updateTrackletMat.m:42
    new_tracklet_mat.class_mat = copy(new_class_mat)
# updateTrackletMat.m:43
    new_tracklet_mat.det_score_mat = copy(new_det_score_mat)
# updateTrackletMat.m:44