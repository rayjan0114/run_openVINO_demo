# openVINO-Demos 

### 教學：

建置 / 試跑 openVINO  官方 Demos (CPU+FP32)



### 安裝步驟：

1. 去官網安裝 openVINO : https://software.intel.com/en-us/openvino-toolkit/choose-download

2. 設定 openvino_demo.json 裡的 USERNAME , DOWNLOAD_PATH 的值(改掉 [Custom])，代表存放預訓練模型+測試影片的路徑

3. build 官方 Demos

   ```bash
   python run_openvino_demo.py --build
   ```

4. 下載預訓練模型 + 測試影片

   ```bash
   python run_openvino_demo.py --download_models
   ```

   ```bash
   python run_openvino_demo.py --download_videos 
   ```

   

