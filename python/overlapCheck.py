# Generated with SMOP  0.41
from libsmop import *
# overlapCheck.m

    
@function
def overlapCheck(track_interval1=None,track_interval2=None,*args,**kwargs):
    varargin = overlapCheck.varargin
    nargin = overlapCheck.nargin

    t_min=max(track_interval1(1),track_interval2(1))
# overlapCheck.m:3
    t_max=min(track_interval1(2),track_interval2(2))
# overlapCheck.m:4
    if t_min > t_max:
        overlap_ratio=0
# overlapCheck.m:6
        return overlap_ratio
    else:
        min_len=min(track_interval1(2) - track_interval1(1) + 1,track_interval2(2) - track_interval2(1) + 1)
# overlapCheck.m:9
        overlap_ratio=(t_max - t_min + 1) / min_len
# overlapCheck.m:10
    