# Generated with SMOP  0.41
from libsmop import *
# overlap.m

    
@function
def overlap(rect1=None,rect2=None,*args,**kwargs):
    varargin = overlap.varargin
    nargin = overlap.nargin

    # if input are rectangulars, rect = [x,y,width,height].
    N1=size(rect1,1)
# overlap.m:4
    N2=size(rect2,1)
# overlap.m:5
    __,xmin1=meshgrid(arange(1,N2),rect1(arange(),1),nargout=2)
# overlap.m:6
    xmin2,__=meshgrid(rect2(arange(),1),arange(1,N1),nargout=2)
# overlap.m:7
    __,ymin1=meshgrid(arange(1,N2),rect1(arange(),2),nargout=2)
# overlap.m:8
    ymin2,__=meshgrid(rect2(arange(),2),arange(1,N1),nargout=2)
# overlap.m:9
    __,xmax1=meshgrid(arange(1,N2),rect1(arange(),1) + rect1(arange(),3) - 1,nargout=2)
# overlap.m:10
    xmax2,__=meshgrid(rect2(arange(),1) + rect2(arange(),3) - 1,arange(1,N1),nargout=2)
# overlap.m:11
    __,ymax1=meshgrid(arange(1,N2),rect1(arange(),2) + rect1(arange(),4) - 1,nargout=2)
# overlap.m:12
    ymax2,__=meshgrid(rect2(arange(),2) + rect2(arange(),4) - 1,arange(1,N1),nargout=2)
# overlap.m:13
    xmin=max(xmin1,xmin2)
# overlap.m:14
    ymin=max(ymin1,ymin2)
# overlap.m:15
    xmax=min(xmax1,xmax2)
# overlap.m:16
    ymax=min(ymax1,ymax2)
# overlap.m:17
    mask=(xmax > logical_and(xmin,ymax) > ymin)
# overlap.m:18
    ratio_mat=zeros(N1,N2)
# overlap.m:19
    overlap_area=zeros(N1,N2)
# overlap.m:20
    overlap_area[mask]=multiply((xmax(mask) - xmin(mask)),(ymax(mask) - ymin(mask)))
# overlap.m:21
    area1=multiply((xmax1 - xmin1 + 1),(ymax1 - ymin1 + 1))
# overlap.m:22
    area2=multiply((xmax2 - xmin2 + 1),(ymax2 - ymin2 + 1))
# overlap.m:23
    ratio_mat[mask]=overlap_area(mask) / (area1(mask) + area2(mask) - overlap_area(mask))
# overlap.m:24
    # x_min = min(rect1(1),rect2(1));
# y_min = min(rect1(2),rect2(2));
# x_max = max(rect1(1)+rect1(3)-1,rect2(1)+rect2(3)-1);
# y_max = max(rect1(2)+rect1(4)-1,rect2(2)+rect2(4)-1);
# mask1 = zeros(x_max-x_min+1,y_max-y_min+1);
# mask2 = zeros(x_max-x_min+1,y_max-y_min+1);
# mask1(rect1(1)-x_min+1:rect1(1)+rect1(3)-x_min,rect1(2)-y_min+1:rect1(2)+rect1(4)-y_min) = 1;
# mask2(rect2(1)-x_min+1:rect2(1)+rect2(3)-x_min,rect2(2)-y_min+1:rect2(2)+rect2(4)-y_min) = 1;
# area1 = sum(sum(mask1));
# area2 = sum(sum(mask2));
# overlap_area = sum(sum((mask1+mask2)==2));
# ratio = 2*overlap_area/(area1+area2);