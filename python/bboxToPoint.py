# Generated with SMOP  0.41
from libsmop import *
# bboxToPoint.m

    
@function
def bboxToPoint(tracklet_mat=None,*args,**kwargs):
    varargin = bboxToPoint.varargin
    nargin = bboxToPoint.nargin

    new_tracklet_mat=copy(tracklet_mat)
# bboxToPoint.m:3
    new_tracklet_mat.det_x = copy(dot(0.5,(tracklet_mat.xmin_mat + tracklet_mat.xmax_mat)) + 1)
# bboxToPoint.m:4
    new_tracklet_mat.det_y = copy(dot(0.5,(tracklet_mat.ymax_mat + tracklet_mat.ymax_mat)) + 1)
# bboxToPoint.m:5
    new_tracklet_mat.det_x[new_tracklet_mat.det_x < 0]=- 1
# bboxToPoint.m:6
    new_tracklet_mat.det_y[new_tracklet_mat.det_y < 0]=- 1
# bboxToPoint.m:7