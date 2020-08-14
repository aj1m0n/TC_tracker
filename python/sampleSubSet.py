# Generated with SMOP  0.41
from libsmop import *
# sampleSubSet.m

    
@function
def sampleSubSet(tracklet_mat=None,track_id=None,*args,**kwargs):
    varargin = sampleSubSet.varargin
    nargin = sampleSubSet.nargin

    new_tracklet_mat.xmin_mat = copy(tracklet_mat.xmin_mat(track_id,arange()))
# sampleSubSet.m:3
    new_tracklet_mat.ymin_mat = copy(tracklet_mat.ymin_mat(track_id,arange()))
# sampleSubSet.m:4
    new_tracklet_mat.xmax_mat = copy(tracklet_mat.xmax_mat(track_id,arange()))
# sampleSubSet.m:5
    new_tracklet_mat.ymax_mat = copy(tracklet_mat.ymax_mat(track_id,arange()))
# sampleSubSet.m:6
    new_tracklet_mat.color_mat = copy(tracklet_mat.color_mat(track_id,arange(),arange()))
# sampleSubSet.m:7