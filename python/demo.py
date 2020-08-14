from TC_tracker import TC_tracker


img_path = '../Loc1_1/img1'
det_path = '../Loc1_1/det.txt'
seq_name = 'Loc1_1'
ROI_path = []
img_save_path = '../save/Loc1_1/'
result_save_path = '../save/Loc1_1/track/test_result'
video_save_path = '../save/Loc1_1/track/tracking_video'

# parameter setting
param={}
param['det_score_thresh'] = 0.1   # detection score threshold, [0,1]
param['IOU_thresh'] = 0.5         # IOU threshold for detection asscociation 
                               # across frames, [0,1]
param['color_thresh'] = 0.15      # color threshold for detection asscociation 
                               # across frames, [0,1]                              
param['lambda_time'] = 25         # time interval cost
param['lambda_split'] = 0.35      # tracklet separation cost
param['lambda_reg'] = 0.2         # smoothness cost
param['lambda_color'] = 0.25      # color change cost
param['lambda_grad'] = 8          # velocity change cost

## tracklet clustering tracking

TC_tracker(img_folder=img_path, det_path=det_path, ROI_path=ROI_path, param=param, save_path=img_save_path, seq_name=seq_name, result_save_path=result_save_path, video_save_path=video_save_path)
