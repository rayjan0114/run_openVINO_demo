#=================================================================================================#
#  2019/09/30 


#=================================================================================================#
import os
import sys
import json
import subprocess
import shutil



class OpenVINO_Demo:
	def __init__(self):
		with open("openvino_demo.json",encoding='utf8') as f: 
			self._dictJson = json.load(f)

		# handcraft your model_path 
		self.create_paths()
	def to_current_dir(self):
		os.chdir(os.path.dirname(os.path.abspath(__file__)))	

	
	# 儲存 demo 路徑
	def create_paths(self):
		if os.name == "nt":
			self.samples_path = "C:/Users/{}/Documents/Intel/OpenVINO/inference_engine_samples_build/intel64/Release".format(self._dictJson["USERNAME"])
			self.demos_path = "C:/Users/{}/Documents/Intel/OpenVINO/omz_demos_build/intel64/Release".format(self._dictJson["USERNAME"])
		else:
			self.samples_path = "/Users/{}/inference_engine_samples_build/intel64/Release".format(self._dictJson["USERNAME"])
			self.demos_path = "/Users/{}/omz_demos_build/intel64/Release".format(self._dictJson["USERNAME"])
	#------------------------------------------------------------------------------------------------------------
	# 自動化 build 
	def build(self):
		if os.name == "nt":
			subprocess.run(["C:/Program Files (x86)/IntelSWTools/openvino/deployment_tools/inference_engine/demos/build_demos_msvc.bat"])
			subprocess.run(["C:/Program Files (x86)/IntelSWTools/openvino/deployment_tools/inference_engine/samples/build_samples_msvc.bat"])
			print("======================================================================")
			print(" build openvino demos ( open model zoo ) + samples completed !! ")
			print("======================================================================")
		else:
			subprocess.run(["/opt/intel/openvino/deployment_tools/inference_engine/demos/build_demos.sh"])
			subprocess.run(["/opt/intel/openvino/deployment_tools/inference_engine/samples/build_samples.sh"])
			print("======================================================================")
			print(" build openvino demos ( open model zoo ) + samples completed !! ")
			print("======================================================================")

	#--------------------------------------------------------------------------------------------------------------
	# 自動化下載 models
	def download_models(self):
		self.download_model_path = self._dictJson["DOWNLOAD_PATH"] + "/download_models"
		if os.name == "nt":
			os.chdir("C:/Program Files (x86)/IntelSWTools/openvino/deployment_tools/open_model_zoo/tools/downloader")
		else:
			os.chdir("/opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader")
		
		subprocess.run(["python","downloader.py","--all","-o",self.download_model_path])
		# subprocess.run(["python3","downloader.py","--all","-o",self.download_model_path])
		self.to_current_dir()
	#----------------------------------------------------------------------------------------------------------------	
	# 自動化下載範例影片
	def download_videos(self):
		self.download_video_path = self._dictJson["DOWNLOAD_PATH"] + "/sample-videos"
		os.chdir(self._dictJson["DOWNLOAD_PATH"])
		subprocess.run(["git","clone","https://github.com/intel-iot-devkit/sample-videos.git"])
		self.to_current_dir()
	#-------------------------------------------------------------------------------------------------------------
	
	def cmd(self):
		if len(sys.argv) == 2:
			if sys.argv[1] == "--build":
				self.build()
			elif sys.argv[1] == "--download_models":
				self.download_models()
			elif sys.argv[1] == "--download_videos":
				self.download_videos()
			else:
				self.comment()
		elif len(sys.argv) == 4:
			self.main_routine() 
		else:
			self.comment()
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
	def comment(self):
			print("====================================================================")
			print(" 激活 openVINO : 複製以下指令到 cmd ")
			print(" Windows : \"C:/Program Files (x86)/IntelSWTools/openvino/bin/setupvars.bat\" ")
			print(" Linux/Mac : source \"/opt/intel/openvino/bin/setupvars.sh\"")
			print("====================================================================")
			print(" 下載/建構 : (請確認 openvino_demo.json , key = DOWNLOAD_PATH 的值 )")
			print("====================================================================")
			print("--build  \t 建構官方 openVINO 例子執行檔 (會執行官方 .bat/.sh)")
			print("--download_models \t 下載官方 openVINO 所有預訓練模型 (會執行官方 downloader.py + 花費些時間!!)")
			print("--download_videos \t 下載官方 openVINO 測試影片  (會 git clone)")
			print("====================================================================")
			print(" 在 CPU + FP32 上 ，執行 demo 列表 : (請確認 openvino_demo.json , key = USERNAME 的值 )")	
			print("====================================================================")
			print("--crossroad_camera_demo [model:{}] [.mp4]  行人辨識".format(len(self._dictJson["crossroad_camera_demo"])))
			#print("--gaze_estimation_demo [model:{}] [.mp4] 臉部辨識".format(len(self._dictJson["gaze_estimation_demo"])))
			print("--human_pose_estimation_demo [model:{}] [.mp4] 臉部辨識".format(len(self._dictJson["human_pose_estimation_demo"])))
			print("--interactive_face_detection_demo [model:{}] [.mp4] 臉部辨識".format(len(self._dictJson["interactive_face_detection_demo"])))
			#print("--mask_rcnn_demo [model:{}] [.bmp] ".format(len(self._dictJson["mask_rcnn_demo"])))
			#print("--object_detection_demo_faster_rcnn [model:{}] [.bmp] ".format(len(self._dictJson["object_detection_demo_faster_rcnn"])))
			#print("--object_detection_demo_ssd_async [model:{}] [.mp4] ".format(len(self._dictJson["object_detection_demo_ssd_async"])))
			#print("--object_detection_demo_yolov3_async [model:{}] [.mp4] ".format(len(self._dictJson["object_detection_demo_yolov3_async"])))
			print("--pedestrian_tracker_demo [model:{}] [.mp4] \t 行人辨識".format(len(self._dictJson["pedestrian_tracker_demo"])))
			print("--security_barrier_camera_demo [model:{}] [.mp4] \t 車牌辨識".format(len(self._dictJson["security_barrier_camera_demo"])))
			print("--segmentation_demo [model:{}] [.bmp]  \t 圖片分割著色".format(len(self._dictJson["segmentation_demo"])))
			#print("--smart_classroom_demo [model:{}] [.mp4] ".format(len(self._dictJson["smart_classroom_demo"])))
			print("--text_detection_demo  [model:{}] [.bmp] \t 圖片英文辨識".format(len(self._dictJson["text_detection_demo"])))
			print("--super_resolution_demo [model:{}] [.bmp] \t 圖片 640x360 高解析度還原4x大".format(len(self._dictJson["super_resolution_demo"])))

			
	def main_routine(self):
		self.download_model_path = self._dictJson["DOWNLOAD_PATH"] + "/download_models"
		self.download_video_path = self._dictJson["DOWNLOAD_PATH"] + "/sample-videos"

		os.chdir(self.demos_path)
		print(self.demos_path)
		#==================================================================================================================================================================
		if sys.argv[1] == "--crossroad_camera_demo":
			if os.name == "nt":
				subprocess.run(["crossroad_camera_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][0],\
					"-m_pa",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][1],\
					"-m_reid",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][2]
					])
			else:
				subprocess.run(["./crossroad_camera_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][0],\
					"-m_pa",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][1],\
					"-m_reid",self.download_model_path+self._dictJson["crossroad_camera_demo"][int(sys.argv[2])-1][2]
					])
		#===========================================================================================================================================================
		elif sys.argv[1] == "--gaze_estimation_demo":
			if os.name == "nt":
				subprocess.run(["gaze_estimation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][0],\
					"-m_fd",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][1],\
					"-m_hp",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][2],\
					"-m_lm",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][3],\
					
					])
			else:
				subprocess.run(["./gaze_estimation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][0],\
					"-m_fd",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][1],\
					"-m_hp",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][2],\
					"-m_lm",self.download_model_path+self._dictJson["gaze_estimation_demo"][int(sys.argv[2])-1][3],\
					
					])


		#=============================================================================================================================================================
		elif sys.argv[1] == "--human_pose_estimation_demo":
			if os.name == "nt":
				subprocess.run(["human_pose_estimation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["human_pose_estimation_demo"][int(sys.argv[2])-1],\
					"-d","CPU"
					])
			else:
				subprocess.run(["./human_pose_estimation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["human_pose_estimation_demo"][int(sys.argv[2])-1],\
					"-d","CPU"
					])
		#===============================================================================================================================================================
		elif sys.argv[1] == "--interactive_face_detection_demo":
			if os.name == "nt":
				subprocess.run([
						"interactive_face_detection_demo",\
						"-i",sys.argv[3],\
						"-m",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][0],\
						"-m_ag",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][1],\
						"-m_hp",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][2],\
						"-m_em",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][3],\
						"-m_lm",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][4]	
					])
			else:
				subprocess.run([
						"./interactive_face_detection_demo",\
						"-i",sys.argv[3],\
						"-m",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][0],\
						"-m_ag",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][1],\
						"-m_hp",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][2],\
						"-m_em",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][3],\
						"-m_lm",self.download_model_path+self._dictJson["interactive_face_detection_demo"][int(sys.argv[2])-1][4]	
					])

		#================================================================================================================================================================

		elif sys.argv[1] == "--pedestrian_tracker_demo":
			if os.name == "nt":
				subprocess.run(["pedestrian_tracker_demo",\
					"-i",sys.argv[3],\
					"-m_det",self.download_model_path+self._dictJson["pedestrian_tracker_demo"][int(sys.argv[2])-1][0],\
					"-m_reid",self.download_model_path+self._dictJson["pedestrian_tracker_demo"][int(sys.argv[2])-1][1]
					])

			else:
				subprocess.run(["./pedestrian_tracker_demo",\
					"-i",sys.argv[3],\
					"-m_det",self.download_model_path+self._dictJson["pedestrian_tracker_demo"][int(sys.argv[2])-1][0],\
					"-m_reid",self.download_model_path+self._dictJson["pedestrian_tracker_demo"][int(sys.argv[2])-1][1]
					])



		#==============================================================================================================================================================================

		elif sys.argv[1] == "--security_barrier_camera_demo":
			if os.name == "nt":
				subprocess.run(["security_barrier_camera_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][0],\
					"-m_va",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][1],\
					"-m_lpr",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][2],\
					"-fps","10"
					])
			else:
				subprocess.run(["./security_barrier_camera_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][0],\
					"-m_va",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][1],\
					"-m_lpr",self.download_model_path+self._dictJson["security_barrier_camera_demo"][int(sys.argv[2])-1][2],\
					"-fps","10"
					])
		#=================================================================================================================================================================================
		elif sys.argv[1] == "--segmentation_demo":
			if os.name == "nt":
				subprocess.run(["segmentation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["segmentation_demo"][int(sys.argv[2])-1],\
					"-d","CPU"])

			else:
				subprocess.run(["./segmentation_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["segmentation_demo"][int(sys.argv[2])-1],\
					"-d","CPU"])
			shutil.copy("./out_0.bmp",self._dictJson["DOWNLOAD_PATH"]+"/segmentation_demo_out.bmp")
			
		#=======================================================================================================================================================================================		
		# some bug of -fg 
		elif sys.argv[1] == "--smart_classroom_demo":
			if os.name == "nt":
				subprocess.run(["smart_classroom_demo",\
					"-i",sys.argv[3],\
					"-m_act",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][0],\
					"-m_fd",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][1],\
					"-m_lm",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][2],\
					"-m_reid",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][3]])
			else:
				subprocess.run(["./smart_classroom_demo",\
					"-i",sys.argv[3],\
					"-m_act",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][0],\
					"-m_fd",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][1],\
					"-m_lm",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][2],\
					"-m_reid",self.download_model_path+self._dictJson["smart_classroom_demo"][int(sys.argv[2])-1][3]])
		

		#===================================================================================================================================================================================
		elif sys.argv[1] == "--text_detection_demo":
			if os.name == "nt":
				subprocess.run(["text_detection_demo",\
					"-i",sys.argv[3],\
					"-m_td",self.download_model_path+self._dictJson["text_detection_demo"][int(sys.argv[2])-1][0],\
					"-m_tr",self.download_model_path+self._dictJson["text_detection_demo"][int(sys.argv[2])-1][1],\
					"-dt","image","-d_td","CPU","-d_tr","CPU"])
			else:
				subprocess.run(["./text_detection_demo","-i",sys.argv[3],\
					"-m_td",self.download_model_path+self._dictJson["text_detection_demo"][int(sys.argv[2])-1][0],\
					"-m_tr",self.download_model_path+self._dictJson["text_detection_demo"][int(sys.argv[2])-1][1],\
					"-dt","image","-d_td","CPU","-d_tr","CPU"])
			
		#=================================================================================================================================================================================
		elif sys.argv[1] == "--super_resolution_demo":
			
			if os.name == "nt":
				subprocess.run(["super_resolution_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["super_resolution_demo"][int(sys.argv[2])-1],\
					"-d","CPU","-show"])
			else:
				subprocess.run(["./super_resolution_demo",\
					"-i",sys.argv[3],\
					"-m",self.download_model_path+self._dictJson["super_resolution_demo"][int(sys.argv[2])-1],\
					"-d","CPU","-show"])
			#================================#
			os.remove("sr_1.png")
			#================================#
		#======================================================================================================================================================================================
		else:
			self.comment()
		self.to_current_dir()

if __name__ == "__main__":
	OpenVINO_Demo().cmd()

