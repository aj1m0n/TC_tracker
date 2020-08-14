# Generated with SMOP  0.41
from libsmop import *
# writeTxt.m

    
@function
def writeTxt(seq_name=None,track_struct_path=None,save_path=None,dataset=None,*args,**kwargs):
    varargin = writeTxt.varargin
    nargin = writeTxt.nargin

    load(concat([track_struct_path,'/',seq_name,'.mat']))
    ## UA-Detrac dataset
    if strcmp(dataset,'UA-Detrac') > 0:
        X=track_struct.tracklet_mat.xmin_mat.T
# writeTxt.m:7
        Y=track_struct.tracklet_mat.ymin_mat.T
# writeTxt.m:8
        W=track_struct.tracklet_mat.xmax_mat.T - X + 1
# writeTxt.m:9
        H=track_struct.tracklet_mat.ymax_mat.T - Y + 1
# writeTxt.m:10
        W[X < 0]=0
# writeTxt.m:11
        H[X < 0]=0
# writeTxt.m:12
        Y[X < 0]=0
# writeTxt.m:13
        X[X < 0]=0
# writeTxt.m:14
        fileID=fopen(concat([save_path,'/',seq_name,'_LX.txt']),'w')
# writeTxt.m:16
        for r in arange(1,size(X,1)).reshape(-1):
            for c in arange(1,size(X,2)).reshape(-1):
                fprintf(fileID,'%f',X(r,c))
                if c != size(X,2):
                    fprintf(fileID,',')
                else:
                    fprintf(fileID,'\n')
        fclose(fileID)
        fileID=fopen(concat([save_path,'/',seq_name,'_LY.txt']),'w')
# writeTxt.m:29
        for r in arange(1,size(X,1)).reshape(-1):
            for c in arange(1,size(X,2)).reshape(-1):
                fprintf(fileID,'%f',Y(r,c))
                if c != size(X,2):
                    fprintf(fileID,',')
                else:
                    fprintf(fileID,'\n')
        fclose(fileID)
        fileID=fopen(concat([save_path,'/',seq_name,'_W.txt']),'w')
# writeTxt.m:42
        for r in arange(1,size(X,1)).reshape(-1):
            for c in arange(1,size(X,2)).reshape(-1):
                fprintf(fileID,'%f',W(r,c))
                if c != size(X,2):
                    fprintf(fileID,',')
                else:
                    fprintf(fileID,'\n')
        fclose(fileID)
        fileID=fopen(concat([save_path,'\',seq_name,'_H.txt']),'w')
# writeTxt.m:55
        for r in arange(1,size(X,1)).reshape(-1):
            for c in arange(1,size(X,2)).reshape(-1):
                fprintf(fileID,'%f',H(r,c))
                if c != size(X,2):
                    fprintf(fileID,',')
                else:
                    fprintf(fileID,'\n')
        fclose(fileID)
    
    ## MOT dataset
    if strcmp(dataset,'MOT') > 0:
        xmin_mat=track_struct.tracklet_mat.xmin_mat
# writeTxt.m:71
        ymin_mat=track_struct.tracklet_mat.ymin_mat
# writeTxt.m:72
        xmax_mat=track_struct.tracklet_mat.xmax_mat
# writeTxt.m:73
        ymax_mat=track_struct.tracklet_mat.ymax_mat
# writeTxt.m:74
        N_id=size(xmin_mat,1)
# writeTxt.m:75
        N_fr=size(xmin_mat,2)
# writeTxt.m:76
        fileID=fopen(concat([save_path,'\',seq_name,'.txt']),'w')
# writeTxt.m:77
        for t in arange(1,N_fr).reshape(-1):
            for n in arange(1,N_id).reshape(-1):
                if xmin_mat(n,t) == - 1:
                    continue
                xmin=round(xmin_mat(n,t))
# writeTxt.m:83
                ymin=round(ymin_mat(n,t))
# writeTxt.m:84
                w=round(xmax_mat(n,t)) - xmin
# writeTxt.m:85
                h=round(ymax_mat(n,t)) - ymin
# writeTxt.m:86
                fprintf(fileID,'%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n',t,n,xmin,ymin,w,h,- 1,- 1,- 1,- 1)
        fclose(fileID)
    