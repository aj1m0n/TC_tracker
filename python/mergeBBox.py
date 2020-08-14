# Generated with SMOP  0.41
from libsmop import *
# mergeBBox.m

    
@function
def mergeBBox(bbox=None,overlap_thresh=None,det_score=None,*args,**kwargs):
    varargin = mergeBBox.varargin
    nargin = mergeBBox.nargin

    # bbox = [x,y,width,height].
    cand_idx=ones(size(bbox,1),1)
# mergeBBox.m:4
    for n1 in arange(1,size(bbox,1) - 1).reshape(-1):
        for n2 in arange((n1 + 1),size(bbox,1)).reshape(-1):
            if cand_idx(n1) == 0 or cand_idx(n2) == 0:
                continue
            r,overlap_area=overlap(bbox(n1,arange()),bbox(n2,arange()),nargout=2)
# mergeBBox.m:10
            #         r = overlap_area/(bbox(n1,3)*bbox(n1,4)+bbox(n2,3)*bbox(n2,4)-overlap_area);
            r1=overlap_area / (dot(bbox(n1,3),bbox(n1,4)))
# mergeBBox.m:14
            r2=overlap_area / (dot(bbox(n2,3),bbox(n2,4)))
# mergeBBox.m:15
            s1=det_score(n1)
# mergeBBox.m:16
            s2=det_score(n2)
# mergeBBox.m:17
            if r1 > overlap_thresh or r2 > overlap_thresh:
                if s1 > s2:
                    cand_idx[n2]=0
# mergeBBox.m:21
                else:
                    cand_idx[n1]=0
# mergeBBox.m:23
            #         if r1>=r2 && r1>overlap_thresh
#             cand_idx(n1) = 0;
#         end
#         if r1<r2 && r2>overlap_thresh
#             cand_idx(n2) = 0;
#         end
    
    idx=find(cand_idx == 1)
# mergeBBox.m:35
    update_bbox=bbox(cand_idx == 1,arange())
# mergeBBox.m:36