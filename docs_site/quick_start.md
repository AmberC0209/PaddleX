### 🛠️ 安装

> ❗安装 PaddleX 前请先确保您有基础的 **Python 运行环境**（注：当前支持Python 3.8 ～ Python 3.10下运行，更多Python版本适配中）。

* **安装 PaddlePaddle**
```bash
# cpu
python -m pip install paddlepaddle==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# gpu，该命令仅适用于 CUDA 版本为 11.8 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# gpu，该命令仅适用于 CUDA 版本为 12.3 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
```
> ❗ 更多飞桨 Wheel 版本请参考[飞桨官网](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation./docs/zh/install/pip/linux-pip.html)。


* **安装PaddleX**

```bash
pip install https://paddle-model-ecology.bj.bcebos.com/paddlex/whl/paddlex-3.0.0b1-py3-none-any.whl
```

> ❗ 更多安装方式参考 [PaddleX 安装教程](installation/installation.md)

### 💻 命令行使用

一行命令即可快速体验产线效果，统一的命令行格式为：

```bash
paddlex --pipeline [产线名称] --input [输入图片] --device [运行设备]
```

只需指定三个参数：
* `pipeline`：产线名称
* `input`：待处理的输入文件（如图片）的本地路径或 URL
* `device`: 使用的 GPU 序号（例如`gpu:0`表示使用第 0 块 GPU），也可选择使用 CPU（`cpu`）


以通用 OCR 产线为例：
```bash
paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --device gpu:0
```
<details>
  <summary><b>👉 点击查看运行结果 </b></summary>

```bash
{
'input_path': '/root/.paddlex/predict_input/general_ocr_002.png',
'dt_polys': [array([[161,  27],
       [353,  22],
       [354,  69],
       [162,  74]], dtype=int16), array([[426,  26],
       [657,  21],
       [657,  58],
       [426,  62]], dtype=int16), array([[702,  18],
       [822,  13],
       [824,  57],
       [704,  62]], dtype=int16), array([[341, 106],
       [405, 106],
       [405, 128],
       [341, 128]], dtype=int16)
       ...],
'dt_scores': [0.758478200014338, 0.7021546472698513, 0.8536622648391111, 0.8619181462164781, 0.8321051217096188, 0.8868756173427551, 0.7982964727675609, 0.8289939036796322, 0.8289428877522524, 0.8587063317632897, 0.7786755892491615, 0.8502032769081344, 0.8703346500042997, 0.834490931790065, 0.908291103353393, 0.7614978661708064, 0.8325774055997542, 0.7843421347676149, 0.8680889482955594, 0.8788859304537682, 0.8963341277518075, 0.9364654810069546, 0.8092413027028257, 0.8503743089091863, 0.7920740420391101, 0.7592224394793805, 0.7920547400069311, 0.6641757962457888, 0.8650289477605955, 0.8079483304467047, 0.8532207681055275, 0.8913377034754717],
'rec_text': ['登机牌', 'BOARDING', 'PASS', '舱位', 'CLASS', '序号 SERIALNO.', '座位号', '日期 DATE', 'SEAT NO', '航班 FLIGHW', '035', 'MU2379', '始发地', 'FROM', '登机口', 'GATE', '登机时间BDT', '目的地TO', '福州', 'TAIYUAN', 'G11', 'FUZHOU', '身份识别IDNO', '姓名NAME', 'ZHANGQIWEI', 票号TKTNO', '张祺伟', '票价FARE', 'ETKT7813699238489/1', '登机口于起飞前10分钟关闭GATESCLOSE10MINUTESBEFOREDEPARTURETIME'],
'rec_score': [0.9985831379890442, 0.999696917533874512, 0.9985735416412354, 0.9842517971992493, 0.9383274912834167, 0.9943678975105286, 0.9419361352920532, 0.9221674799919128, 0.9555020928382874, 0.9870321154594421, 0.9664073586463928, 0.9988052248954773, 0.9979352355003357, 0.9985110759735107, 0.9943482875823975, 0.9991195797920227, 0.9936401844024658, 0.9974591135978699, 0.9743705987930298, 0.9980487823486328, 0.9874696135520935, 0.9900962710380554, 0.9952947497367859, 0.9950481653213501, 0.989926815032959, 0.9915552139282227, 0.9938777685165405, 0.997239887714386, 0.9963340759277344, 0.9936134815216064, 0.97223961353302]}
```

可视化结果如下：

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/boardingpass.png">

</details>

其他产线的命令行使用，只需将 `pipeline` 参数调整为相应产线的名称。下面列出了每个产线对应的命令：

<details>
  <summary><b>👉 更多产线的命令行使用</b></summary>

<table>
    <thead>
        <tr>
            <th>产线名称</th>
            <th>使用命令</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>通用图像分类</td>
            <td><code>paddlex --pipeline image_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg --device gpu:0</code></td>
        </tr>
        <tr>
            <td>通用目标检测</td>
            <td><code>paddlex --pipeline object_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_object_detection_002.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>通用实例分割</td>
            <td><code>paddlex --pipeline instance_segmentation --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_instance_segmentation_004.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>通用语义分割</td>
            <td><code>paddlex --pipeline semantic_segmentation --input https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/application/semantic_segmentation/makassaridn-road_demo.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>图像多标签分类</td>
            <td><code>paddlex --pipeline multi_label_image_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg --device gpu:0</code></td>
        </tr>
        <tr>
            <td>小目标检测</td>
            <td><code>paddlex --pipeline small_object_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/small_object_detection.jpg --device gpu:0</code></td>
        </tr>
        <tr>
            <td>图像异常检测</td>
            <td><code>paddlex --pipeline anomaly_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/uad_grid.png --device gpu:0 </code></td>
        </tr>
        <tr>
            <td>通用OCR</td>
            <td><code>paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>通用表格识别</td>
            <td><code>paddlex --pipeline table_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/table_recognition.jpg --device gpu:0</code></td>
        </tr>
        <tr>
            <td>通用版面解析</td>
            <td><code>paddlex --pipeline layout_parsing --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/demo_paper.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>公式识别</td>
            <td><code>paddlex --pipeline formula_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/demo_image/general_formula_recognition.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>印章文本识别</td>
            <td><code>paddlex --pipeline seal_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png --device gpu:0</code></td>
        </tr>
        <tr>
            <td>时序预测</td>
            <td><code>paddlex --pipeline ts_fc --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_fc.csv --device gpu:0</code></td>
        </tr>
        <tr>
            <td>时序异常检测</td>
            <td><code>paddlex --pipeline ts_ad --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv --device gpu:0</code></td>
        </tr>
        <tr>
            <td>时序分类</td>
            <td><code>paddlex --pipeline ts_cls --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_cls.csv --device gpu:0</code></td>
        </tr>
    </tbody>
</table>
</details>

### 📝 Python 脚本使用

几行代码即可完成产线的快速推理，统一的 Python 脚本格式如下：
```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline=[产线名称])
output = pipeline.predict([输入图片名称])
for res in output:
    res.print()
    res.save_to_img("./output/")
    res.save_to_json("./output/")
```
执行了如下几个步骤：

* `create_pipeline()` 实例化产线对象
* 传入图片并调用产线对象的 `predict` 方法进行推理预测
* 对预测结果进行处理

其他产线的 Python 脚本使用，只需将 `create_pipeline()` 方法的 `pipeline` 参数调整为相应产线的名称。下面列出了每个产线对应的参数名称及详细的使用解释：
<details>
  <summary><b>👉 更多产线的Python脚本使用</b></summary>

<table>
    <thead>
        <tr>
            <th>产线名称</th>
            <th>对应参数</th>
            <th>详细说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>文档场景信息抽取v3</td>
            <td><code>PP-ChatOCRv3-doc</code></td>
            <td><a href="pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.md#22-本地体验">文档场景信息抽取v3产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用图像分类</td>
            <td><code>image_classification</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/image_classification.md#222-python脚本方式集成">通用图像分类产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用目标检测</td>
            <td><code>object_detection</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/object_detection.md#222-python脚本方式集成">通用目标检测产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用实例分割</td>
            <td><code>instance_segmentation</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/instance_segmentation.md#222-python脚本方式集成">通用实例分割产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用语义分割</td>
            <td><code>semantic_segmentation</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.md#222-python脚本方式集成">通用语义分割产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>图像多标签分类</td>
            <td><code>multi_label_image_classification</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.md#22-python脚本方式集成">图像多标签分类产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>小目标检测</td>
            <td><code>small_object_detection</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/small_object_detection.md#22-python脚本方式集成">小目标检测产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>图像异常检测</td>
            <td><code>anomaly_detection</code></td>
            <td><a href="pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.md#22-python脚本方式集成">图像异常检测产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用OCR</td>
            <td><code>OCR</code></td>
            <td><a href="pipeline_usage/tutorials/ocr_pipelines/OCR.md#222-python脚本方式集成">通用OCR产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用表格识别</td>
            <td><code>table_recognition</code></td>
            <td><a href="pipeline_usage/tutorials/ocr_pipelines/table_recognition.md#22-python脚本方式集成">通用表格识别产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>通用版面解析</td>
            <td><code>layout_parsing</code></td>
            <td><a href="pipeline_usage/tutorials/ocr_pipelines/layout_parsing.md#22-python脚本方式集成">通用版面解析产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>公式识别</td>
            <td><code>formula_recognition</code></td>
            <td><a href="pipeline_usage/tutorials/ocr_pipelines/formula_recognition.md#22-python脚本方式集成">公式识别产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>印章文本识别</td>
            <td><code>seal_recognition</code></td>
            <td><a href="pipeline_usage/tutorials/ocr_pipelines/seal_recognition.md#22-python脚本方式集成">印章文本识别产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>时序预测</td>
            <td><code>ts_fc</code></td>
            <td><a href="pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.md#222-python脚本方式集成">时序预测产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>时序异常检测</td>
            <td><code>ts_ad</code></td>
            <td><a href="pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.md#222-python脚本方式集成">时序异常检测产线Python脚本使用说明</a></td>
        </tr>
        <tr>
            <td>时序分类</td>
            <td><code>ts_cls</code></td>
            <td><a href="pipeline_usage/tutorials/time_series_pipelines/time_series_classification.md#222-python脚本方式集成">时序分类产线Python脚本使用说明</a></td>
        </tr>
    </tbody>
</table>

</details>