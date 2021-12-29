# OpenCV Webcam Script v0.1
# 创建人：曾逸夫
# 创建时间：2021-12-26

import cv2
from pathlib import Path
import argparse
import time
import os
import glob
import re
import os

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description = 'OpenCV Webcam Script')
    parser.add_argument('--device','-dev', default = 0, type = int, help = 'device index for webcam')
    parser.add_argument('--quit','-q', default = "q", type = str, help = 'quit key for webcam')
    parser.add_argument('--is_autoSaveFrame', '-isasf', action='store_true', help = 'is auto save frame')
    parser.add_argument('--is_headSaveFrame', '-ishsf', action='store_true', help = 'is head save frame')
    parser.add_argument('--is_resizeFrame', '-isrf', action='store_true', help = 'is resize frame')
    parser.add_argument('--frame_saveDir', '-fsd', default = "./WebcamFrame", type = str, help = 'save frame dir')
    parser.add_argument('--frame_nSave', '-fns', default = 1, type = int, help = 'n frames save a frame (auto save frame)')
    parser.add_argument('--frame_capKey', '-fck', default = "a", type = str, help = 'frame capture key (head save frame)')
    parser.add_argument('--resize_frame', '-rf', default = [640, 480], type = int, nargs = '+', help = 'resize frame save')
    parser.add_argument('--resizeRatio_frame', '-rrf', default = 1.0, type = float, help = 'resize ratio frame save')

    global args
    args = parser.parse_args(argv)

# 保存路径管理 
def increment_path(path, exist_ok=False, sep='', mkdir=False):
    # 引用：https://github.com/ultralytics/yolov5/blob/master/utils/general.py
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        suffix = path.suffix
        path = path.with_suffix('')
        dirs = glob.glob(f"{path}{sep}*")  # similar paths
        matches = [re.search(rf"%s{sep}(\d+)" % path.stem, d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]  # indices
        n = max(i) + 1 if i else 2  # increment number
        path = Path(f"{path}{sep}{n}{suffix}")  # update path
    dir = path if path.suffix == '' else path.parent  # directory
    if not dir.exists() and mkdir:
        dir.mkdir(parents=True, exist_ok=True)  # make directory
    return path


# webcam opencv
def webcam_opencv(device_index, quit_key, is_autoSaveFrame, frame_saveDir, frame_nSave, is_headSaveFrame, frame_capKey, is_resizeFrame, resize_frame, resizeRatio_frame):
    cap = cv2.VideoCapture(device_index) # 连接设备
    frame_width = cap.get(3) # 宽度
    frame_height = cap.get(4) # 高度
    fps = cap.get(5) # 帧率
    print(f'宽度：{frame_width}, 高度：{frame_height}， FPS：{fps}')
    success, _ = cap.read() # 读取设备

    if success:
        print(f'摄像头连接成功！')

        if is_autoSaveFrame or is_headSaveFrame:
            # 帧保存路径管理
            frame_samePath = increment_path(Path(f"{frame_saveDir}") / "frames", exist_ok=False)  # 增量运行
            frame_samePath.mkdir(parents=True, exist_ok=True)  # 创建目录
        
        frame_num = 0 # 帧数
        while(1):
            ret, frame = cap.read() # 捕获画面
            frame_num += 1
            print(f'第{frame_num}帧')
            cv2.imshow("capture", frame) # 显示画面
            # print(frame.shape) # h,w,c
            if (is_autoSaveFrame): # 自动保存
                if (frame_num % frame_nSave == 0): # 每隔n帧保存一次
                    if (is_resizeFrame): # resize frame
                        w_resize = int(resize_frame[0] * resizeRatio_frame) # 重塑宽度
                        h_resize = int(resize_frame[1] * resizeRatio_frame) # 重塑高度
                        frame_new = cv2.resize(frame, (w_resize, h_resize), interpolation = cv2.INTER_AREA) # 重塑
                        cv2.imwrite(f'./{frame_samePath}/{frame_num}.jpg', frame_new)
                    else:
                        cv2.imwrite(f'./{frame_samePath}/{frame_num}.jpg', frame)
            if (is_headSaveFrame): # 手动保存
                if cv2.waitKey(20) & 0xFF == ord(frame_capKey): # 保存键
                    if (is_resizeFrame): # 重塑
                        w_resize = int(resize_frame[0] * resizeRatio_frame)
                        h_resize = int(resize_frame[1] * resizeRatio_frame)
                        frame_new = cv2.resize(frame, (w_resize, h_resize), interpolation = cv2.INTER_AREA)
                        cv2.imwrite(f'./{frame_samePath}/{frame_num}.jpg', frame_new)
                    else:
                        cv2.imwrite(f'./{frame_samePath}/{frame_num}.jpg', frame)
            if cv2.waitKey(20) & 0xFF == ord(quit_key): # 退出 ord：字符转ASCII码
                break
        print(f'一共处理了{frame_num}帧')
        # 释放缓存
        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f'摄像头连接异常！')



if __name__ == '__main__':
    # 参数
    parse_args()
    device_index = args.device
    quit_key = args.quit
    is_autoSaveFrame = args.is_autoSaveFrame
    is_headSaveFrame = args.is_headSaveFrame
    frame_saveDir = args.frame_saveDir
    frame_nSave = args.frame_nSave
    frame_capKey = args.frame_capKey
    resize_frame = args.resize_frame
    is_resizeFrame = args.is_resizeFrame
    resizeRatio_frame = args.resizeRatio_frame

    # 判断快捷键冲突
    if (quit_key == frame_capKey):
        print(f'快捷键冲突!')
    else:
        # 调用webcam opencv
        webcam_opencv(device_index, quit_key, is_autoSaveFrame, frame_saveDir, frame_nSave, is_headSaveFrame, frame_capKey, is_resizeFrame, resize_frame, resizeRatio_frame)

    print(f'程序结束！')