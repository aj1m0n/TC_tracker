# Generated with SMOP  0.41
from libsmop import *
# bboxAssociate.m

    
@function
def bboxAssociate(det_bbox=None,gt_bbox=None,overlap_thresh=None,lb_thresh=None,mask=None,*args,**kwargs):
    varargin = bboxAssociate.varargin
    nargin = bboxAssociate.nargin

    # bbox = [x,y,width,height]
    if isempty(gt_bbox) or isempty(det_bbox):
        det_idx=[]
# bboxAssociate.m:6
        gt_idx=[]
# bboxAssociate.m:7
        final_overlap_mat=[]
# bboxAssociate.m:8
        return det_idx,gt_idx,final_overlap_mat
    
    N1=size(det_bbox,1)
# bboxAssociate.m:11
    N2=size(gt_bbox,1)
# bboxAssociate.m:12
    overlap_mat=overlap(det_bbox,gt_bbox)
# bboxAssociate.m:13
    if logical_not(isempty(mask)):
        overlap_mat[mask == 0]=0
# bboxAssociate.m:15
    
    final_overlap_mat=copy(overlap_mat)
# bboxAssociate.m:17
    # greedy search
    gt_idx=[]
# bboxAssociate.m:20
    det_idx=[]
# bboxAssociate.m:21
    while 1:

        max_v,idx=max_mat(overlap_mat,nargout=2)
# bboxAssociate.m:23
        if max_v < overlap_thresh:
            break
        overlap_idx=find(overlap_mat(idx(1),arange()) > lb_thresh)
# bboxAssociate.m:28
        if length(overlap_idx) == 1:
            det_idx=concat([det_idx,idx(1)])
# bboxAssociate.m:30
            gt_idx=concat([gt_idx,idx(2)])
# bboxAssociate.m:31
        overlap_mat[idx(1),arange()]=0
# bboxAssociate.m:33
        overlap_mat[arange(),idx(2)]=0
# bboxAssociate.m:34

    