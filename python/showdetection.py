# Generated with SMOP  0.41
from libsmop import *
# showdetection.m

    
    img_folder='D:\Data\UA-Detrac\DETRAC-train-data\Insight-MVT_Annotation_Train\MVI_20011'
# showdetection.m:2
    txt_file='D:\Data\UA-Detrac\CompACT-train\CompACT\MVI_20011_Det_CompACT.txt'
# showdetection.m:3
    fr_idx=203
# showdetection.m:4
    detection_thresh=0.0
# showdetection.m:5
    fileID=fopen(txt_file,'r')
# showdetection.m:7
    A=textscan(fileID,'%f %f %f %f %f %f %f %f %f %f %s','Delimiter',',')
# showdetection.m:8
    fclose(fileID)
    M=zeros(size(A[1],1),10)
# showdetection.m:10
    for n in arange(1,10).reshape(-1):
        M[arange(),n]=A[n]
# showdetection.m:12
    
    idx=find(M(arange(),1) == fr_idx)
# showdetection.m:15
    img_name=fileName(fr_idx,4)
# showdetection.m:16
    img_list=dir(concat([img_folder,'\*.jpg']))
# showdetection.m:17
    img=imread(concat([img_folder,'\',img_list(fr_idx).name]))
# showdetection.m:18
    figure
    imshow(img)
    hold('on')
    for n in arange(1,length(idx)).reshape(-1):
        if M(idx(n),7) < detection_thresh:
            continue
        bbox=M(idx(n),arange(3,6))
# showdetection.m:26
        xmin=bbox(1)
# showdetection.m:27
        ymin=bbox(2)
# showdetection.m:28
        xmax=bbox(1) + bbox(3) - 1
# showdetection.m:29
        ymax=bbox(2) + bbox(4) - 1
# showdetection.m:30
        plot(concat([xmin,xmin]),concat([ymin,ymax]),'r')
        hold('on')
        plot(concat([xmax,xmax]),concat([ymin,ymax]),'r')
        hold('on')
        plot(concat([xmin,xmax]),concat([ymin,ymin]),'r')
        hold('on')
        plot(concat([xmin,xmax]),concat([ymax,ymax]),'r')
        hold('on')
    