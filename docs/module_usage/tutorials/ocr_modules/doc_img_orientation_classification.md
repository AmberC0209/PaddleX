简体中文 | [English](doc_img_orientation_classification.en.md)

# 文档图像方向分类模块使用教程

## 一、概述
文档图像方向分类模块主要是将文档图像的方向区分出来，并使用后处理将其矫正。在诸如文档扫描、证照拍摄等过程中，有时为了拍摄更清晰，会将拍摄设备进行旋转，导致得到的图片也是不同方向的。此时，标准的OCR流程无法很好地应对这些数据。利用图像分类技术，可以预先判断含文字区域的文档或证件的方向，并将其进行方向调整，从而提高OCR处理的准确性。

## 二、支持模型列表


<table>
<thead>
<tr>
<th>模型</th>
<th>Top-1 Acc（%）</th>
<th>GPU推理耗时（ms）</th>
<th>CPU推理耗时 (ms)</th>
<th>模型存储大小（M)</th>
<th>介绍</th>
</tr>
</thead>
<tbody>
<tr>
<td>PP-LCNet_x1_0_doc_ori</td>
<td>99.06</td>
<td>3.84845</td>
<td>9.23735</td>
<td>7</td>
<td>基于PP-LCNet_x1_0的文档图像分类模型，含有四个类别，即0度，90度，180度，270度</td>
</tr>
</tbody>
</table>

<b>注：以上精度指标的评估集是自建的数据集，覆盖证件和文档等多个场景，包含 1000 张图片。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。</b>

## 三、快速集成

> ❗ 在快速集成前，请先安装 PaddleX 的 wheel 包，详细请参考 [PaddleX本地安装教程](../../../installation/installation.md)

完成wheel 包的安装后，几行代码即可完成文档图像方向分类模块的推理，可以任意切换该模块下的模型，您也可以将文档图像方向分类模块中的模型推理集成到您的项目中。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/img_rot180_demo.jpg)到本地。

```bash
from paddlex import create_model
model = create_model("PP-LCNet_x1_0_doc_ori")
output = model.predict("img_rot180_demo.jpg",  batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_img("./output/demo.png")
    res.save_to_json("./output/res.json")
```
关于更多 PaddleX 的单模型推理的 API 的使用方法，可以参考的使用方法，可以参考[PaddleX单模型Python脚本使用说明](../../instructions/model_python_API.md)。

## 四、二次开发
如果你追求更高精度的现有模型，可以使用PaddleX的二次开发能力，开发更好的文档图像方向分类模型。在使用PaddleX开发文档图像方向分类模型之前，请务必安装PaddleX的分类相关的模型训练能力，安装过程可以参考 [PaddleX本地安装教程](../../../installation/installation.md)

### 4.1 数据准备
在进行模型训练前，需要准备相应任务模块的数据集。PaddleX 针对每一个模块提供了数据校验功能，<b>只有通过数据校验的数据才可以进行模型训练</b>。此外，PaddleX为每一个模块都提供了 Demo 数据集，您可以基于官方提供的 Demo 数据完成后续的开发。若您希望用私有数据集进行后续的模型训练，可以参考[PaddleX图像分类任务模块数据准备教程](../../../data_annotations/cv_modules/image_classification.md)。

#### 4.1.1 Demo 数据下载
您可以参考下面的命令将 Demo 数据集下载到指定文件夹：

```bash
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/text_image_orientation.tar -P ./dataset
tar -xf ./dataset/text_image_orientation.tar  -C ./dataset/
```
#### 4.1.2 数据校验
一行命令即可完成数据校验：

```bash
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/text_image_orientation
```
执行上述命令后，PaddleX 会对数据集进行校验，并统计数据集的基本信息，命令运行成功后会在log中打印出`Check dataset passed !`信息。校验结果文件保存在`./output/check_dataset_result.json`，同时相关产出会保存在当前目录的`./output/check_dataset`目录下，产出目录中包括可视化的示例样本图片和样本分布直方图。

<details>
  <summary>👉 <b>校验结果详情（点击展开）</b></summary>

校验结果文件具体内容为：

```bash
{
  "done_flag": true,
  "check_pass": true,
  "attributes": {
    "label_file": "..\/..\/text_image_orientation\/label.txt",
    "num_classes": 4,
    "train_samples": 1553,
    "train_sample_paths": [
      "check_dataset\/demo_img\/img_rot270_10351.jpg",
      "check_dataset\/demo_img\/img_rot0_3908.jpg",
      "check_dataset\/demo_img\/img_rot180_7712.jpg",
      "check_dataset\/demo_img\/img_rot0_7480.jpg",
      "check_dataset\/demo_img\/img_rot270_9599.jpg",
      "check_dataset\/demo_img\/img_rot90_10323.jpg",
      "check_dataset\/demo_img\/img_rot90_4885.jpg",
      "check_dataset\/demo_img\/img_rot180_3939.jpg",
      "check_dataset\/demo_img\/img_rot90_7153.jpg",
      "check_dataset\/demo_img\/img_rot180_1747.jpg"
    ],
    "val_samples": 2593,
    "val_sample_paths": [
      "check_dataset\/demo_img\/img_rot270_3190.jpg",
      "check_dataset\/demo_img\/img_rot0_10272.jpg",
      "check_dataset\/demo_img\/img_rot0_9930.jpg",
      "check_dataset\/demo_img\/img_rot90_918.jpg",
      "check_dataset\/demo_img\/img_rot180_2079.jpg",
      "check_dataset\/demo_img\/img_rot90_8574.jpg",
      "check_dataset\/demo_img\/img_rot90_7595.jpg",
      "check_dataset\/demo_img\/img_rot90_1751.jpg",
      "check_dataset\/demo_img\/img_rot180_1573.jpg",
      "check_dataset\/demo_img\/img_rot90_4401.jpg"
    ]
  },
  "analysis": {
    "histogram": "check_dataset\/histogram.png"
  },
  "dataset_path": ".\/text_image_orientation",
  "show_type": "image",
  "dataset_type": "ClsDataset"
}
```
上述校验结果中，check_pass 为 True 表示数据集格式符合要求，其他部分指标的说明如下：

* `attributes.num_classes`：该数据集类别数为 4；
* `attributes.train_samples`：该数据集训练集样本数量为 1552；
* `attributes.val_samples`：该数据集验证集样本数量为 2593；
* `attributes.train_sample_paths`：该数据集训练集样本可视化图片相对路径列表；
* `attributes.val_sample_paths`：该数据集验证集样本可视化图片相对路径列表；


数据集校验还对数据集中所有类别的样本数量分布情况进行了分析，并绘制了分布直方图（histogram.png）：

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/modules/doc_img_ori_classification/01.png">
</details>

#### 4.1.3 数据集格式转换/数据集划分（可选）
在您完成数据校验之后，可以通过<b>修改配置文件</b>或是<b>追加超参数</b>的方式对数据集的格式进行转换，也可以对数据集的训练/验证比例进行重新划分。

<details>
  <summary>👉 <b>格式转换/数据集划分详情（点击展开）</b></summary>

<b>（1）数据集格式转换</b>

文档图像方向分类暂不支持数据格式转换。

<b>（2）数据集划分</b>

数据集划分的参数可以通过修改配置文件中 `CheckDataset` 下的字段进行设置，配置文件中部分参数的示例说明如下：

* `CheckDataset`:
  * `split`:
    * `enable`: 是否进行重新划分数据集，为 `True` 时进行数据集格式转换，默认为 `False`；
    * `train_percent`: 如果重新划分数据集，则需要设置训练集的百分比，类型为0-100之间的任意整数，需要保证与 `val_percent` 的值之和为100；


例如，您想重新划分数据集为 训练集占比90%、验证集占比10%，则需将配置文件修改为：

```bash
......
CheckDataset:
  ......
  split:
    enable: True
    train_percent: 90
    val_percent: 10
  ......
```
随后执行命令：

```bash
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/text_image_orientation
```
数据划分执行之后，原有标注文件会被在原路径下重命名为 `xxx.bak`。

以上参数同样支持通过追加命令行参数的方式进行设置：

```bash
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/text_image_orientation \
    -o CheckDataset.split.enable=True \
    -o CheckDataset.split.train_percent=90 \
    -o CheckDataset.split.val_percent=10
```
</details>

### 4.2 模型训练
一条命令即可完成模型的训练，此处以文档图像方向分类模型（PP-LCNet_x1_0_doc_ori）的训练为例：

```bash
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=train \
    -o Global.dataset_dir=./dataset/text_image_orientation
```
需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-LCNet_x1_0_doc_ori.yaml`，训练其他模型时，需要的指定相应的配置文件，模型和配置的文件的对应关系，可以查阅[PaddleX模型列表（CPU/GPU）](../../../support_list/models_list.md)）
* 指定模式为模型训练：`-o Global.mode=train`
* 指定训练数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Train`下的字段来进行设置，也可以通过在命令行中追加参数来进行调整。如指定前 2 卡 gpu 训练：`-o Global.device=gpu:0,1`；设置训练轮次数为 10：`-o Train.epochs_iters=10`。更多可修改的参数及其详细解释，可以查阅模型对应任务模块的配置文件说明[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

<details>
  <summary>👉 <b>更多说明（点击展开）</b></summary>

* 模型训练过程中，PaddleX 会自动保存模型权重文件，默认为`output`，如需指定保存路径，可通过配置文件中 `-o Global.output` 字段进行设置。
* PaddleX 对您屏蔽了动态图权重和静态图权重的概念。在模型训练的过程中，会同时产出动态图和静态图的权重，在模型推理时，默认选择静态图权重推理。
* 在完成模型训练后，所有产出保存在指定的输出目录（默认为`./output/`）下，通常有以下产出：

* `train_result.json`：训练结果记录文件，记录了训练任务是否正常完成，以及产出的权重指标、相关文件路径等；
* `train.log`：训练日志文件，记录了训练过程中的模型指标变化、loss 变化等；
* `config.yaml`：训练配置文件，记录了本次训练的超参数的配置；
* `.pdparams`、`.pdema`、`.pdopt.pdstate`、`.pdiparams`、`.pdmodel`：模型权重相关文件，包括网络参数、优化器、EMA、静态图网络参数、静态图网络结构等；
</details>

### <b>4.3 模型评估</b>
在完成模型训练后，可以对指定的模型权重文件在验证集上进行评估，验证模型精度。使用 PaddleX 进行模型评估，一条命令即可完成模型的评估：

```
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=evaluate \
    -o Global.dataset_dir=./dataset/text_image_orientation
```
与模型训练类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-LCNet_x1_0_doc_ori.yaml`）
* 指定模式为模型评估：`-o Global.mode=evaluate`
* 指定验证数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Evaluate`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

<details>
  <summary>👉 <b>更多说明（点击展开）</b></summary>

在模型评估时，需要指定模型权重文件路径，每个配置文件中都内置了默认的权重保存路径，如需要改变，只需要通过追加命令行参数的形式进行设置即可，如`-o Evaluate.weight_path=``./output/best_model/best_model.pdparams`。

在完成模型评估后，通常有以下产出：

在完成模型评估后，会产出`evaluate_result.json，其记录了`评估的结果，具体来说，记录了评估任务是否正常完成，以及模型的评估指标，包含 Top1 Acc。

</details>

### <b>4.4 模型推理和模型集成</b>
在完成模型的训练和评估后，即可使用训练好的模型权重进行推理预测或者进行Python集成。

#### 4.4.1 模型推理
通过命令行的方式进行推理预测，只需如下一条命令。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/img_rot180_demo.jpg)到本地。

```
python main.py -c paddlex/configs/doc_text_orientation/PP-LCNet_x1_0_doc_ori.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir="./output/best_model/inference" \
    -o Predict.input="img_rot180_demo.jpg"
```
与模型训练和评估类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-LCNet_x1_0_doc_ori.yaml`）
* 指定模式为模型推理预测：`-o Global.mode=predict`
* 指定模型权重路径：`-o Predict.model_dir=``"./output/best_model/inference"`
* 指定输入数据路径：`-o Predict.input="..."`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Predict`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

#### 4.4.2 模型集成
模型可以直接集成到PaddleX产线中，也可以直接集成到您自己的项目中。

1.<b>产线集成</b>

文档图像分类模块可以集成的PaddleX产线有[文档场景信息抽取v3产线（PP-ChatOCRv3）](../../../pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.md)，只需要替换模型路径即可完成文本检测模块的模型更新。

2.<b>模块集成</b>

您产出的权重可以直接集成到文档图像方向分类模块中，可以参考[快速集成](#三快速集成)的 Python 示例代码，只需要将模型替换为你训练的到的模型路径即可。
