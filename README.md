# openVINO-Demos 

### 動機/目的：

建置 / 試跑 openVINO  官方 Demos (CPU+FP32) ，

若要理解/手動 openVINO 建議先查看 [](./doc/openVINONote.pdf) , 以下為更方便的 script !!

### 自動化步驟：

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


5.  跑官方測試程式

```python
python run_openvino_demo.py --[DemoName] [model_index] [.mp4/.bmp]
```

- 註:  可執行 python run_openvino_demo.py 會印出有哪些 [DemoName]
- 註:  [model_index] 為陣列位址，對應到 openvino_demo.json 的第 [model_index]-1 個模型路徑設定
- [.mp4/.bmp]  請放檔案的絕對路徑



