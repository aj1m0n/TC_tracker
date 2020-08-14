# Generated with SMOP  0.41
from libsmop import *
# getLoss.m

    
@function
def getLoss(track_id=None,sigma=None,tracklet_mat=None,*args,**kwargs):
    varargin = getLoss.varargin
    nargin = getLoss.nargin

    t=[]
# getLoss.m:3
    det_x=[]
# getLoss.m:4
    det_y=[]
# getLoss.m:5
    for n in arange(1,length(track_id)).reshape(-1):
        temp_t=find(tracklet_mat.det_x(track_id(n),arange()) > 0)
# getLoss.m:7
        det_x=concat([det_x,tracklet_mat.det_x(track_id(n),temp_t)])
# getLoss.m:8
        det_y=concat([det_y,tracklet_mat.det_y(track_id(n),temp_t)])
# getLoss.m:9
        t=concat([t,temp_t])
# getLoss.m:10
    
    model_x=fitrgp(t.T,det_x.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# getLoss.m:13
    pred_x=predict(model_x,t.T)
# getLoss.m:16
    model_y=fitrgp(t.T,det_y.T,'Basis','linear','FitMethod','exact','PredictMethod','exact','Sigma',sigma,'ConstantSigma',true,'KernelFunction','matern52','KernelParameters',concat([1000,1000]))
# getLoss.m:18
    pred_y=predict(model_y,t.T)
# getLoss.m:21
    err=sum(sqrt((pred_x - det_x.T) ** 2 + (pred_y - det_y.T) ** 2))
# getLoss.m:23
    # figure, plot(t,det_x,'k.',t,pred_x,'r.')
# figure, plot(t,det_y,'k.',t,pred_y,'r.')