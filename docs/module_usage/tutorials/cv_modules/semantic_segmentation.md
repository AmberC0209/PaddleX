简体中文 | [English](semantic_segmentation.en.md)

# 语义分割模块使用教程

## 一、概述
语义分割是计算机视觉中的一种技术，它通过对图像中每个像素进行分类，将图像划分为不同的语义区域，每个区域对应一个具体的类别。这种技术能够生成精细的分割图，清晰地展现图像中的对象及其边界，为图像分析和理解提供有力支持。

## 二、支持模型列表

|模型名称|mloU（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M)|
|-|-|-|-|-|
|OCRNet_HRNet-W48|82.15|78.9976|2226.95|249.8 M|
|PP-LiteSeg-T|73.10|7.6827|138.683|28.5 M|

> ❗ 以上列出的是语义分割模块重点支持的**2个核心模型**，该模块总共支持**18个模型**，完整的模型列表如下：

<details>
   <summary> 👉模型列表详情</summary>

|模型名称|mloU（%）|GPU推理耗时（ms）|CPU推理耗时 (ms)|模型存储大小（M)|
|-|-|-|-|-|
|Deeplabv3_Plus-R50 |80.36|61.0531|1513.58|94.9 M|
|Deeplabv3_Plus-R101|81.10|100.026|2460.71|162.5 M|
|Deeplabv3-R50|79.90|82.2631|1735.83|138.3 M|
|Deeplabv3-R101|80.85|121.492|2685.51|205.9 M|
|OCRNet_HRNet-W18|80.67|48.2335|906.385|43.1 M|
|OCRNet_HRNet-W48|82.15|78.9976|2226.95|249.8 M|
|PP-LiteSeg-T|73.10|7.6827|138.683|28.5 M|
|PP-LiteSeg-B|75.25|-|-|47.0 M|
|SegFormer-B0 (slice)|76.73|11.1946|268.929|13.2 M|
|SegFormer-B1 (slice)|78.35|17.9998|403.393|48.5 M|
|SegFormer-B2 (slice)|81.60|48.0371|1248.52|96.9 M|
|SegFormer-B3 (slice)|82.47|64.341|1666.35|167.3 M|
|SegFormer-B4 (slice)|82.38|82.4336|1995.42|226.7 M|
|SegFormer-B5 (slice)|82.58|97.3717|2420.19|229.7 M|

**以上模型精度指标测量自[Cityscapes](https://www.cityscapes-dataset.com/)数据集。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。**


|模型名称|mloU（%）|GPU推理耗时（ms）|CPU推理耗时|模型存储大小（M)|
|-|-|-|-|-|
|SeaFormer_base(slice)|40.92|24.4073|397.574|30.8 M|
|SeaFormer_large (slice)|43.66|27.8123|550.464|49.8 M|
|SeaFormer_small (slice)|38.73|19.2295|358.343|14.3 M|
|SeaFormer_tiny (slice)|34.58|13.9496|330.132|6.1M |

**SeaFormer系列模型的精度指标测量自[ADE20k](https://groups.csail.mit.edu/vision/datasets/ADE20K/)数据集。GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。**

</details>

## 三、快速集成
> ❗ 在快速集成前，请先安装 PaddleX 的 wheel 包，详细请参考 [PaddleX本地安装教程](../../../installation/installation.md)

完成 wheel 包的安装后，几行代码即可完成语义分割模块的推理，可以任意切换该模块下的模型，您也可以将语义分割的模块中的模型推理集成到您的项目中。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_semantic_segmentation_002.png)到本地。

```python
from paddlex import create_model
model = create_model("PP-LiteSeg-T")
output = model.predict("general_semantic_segmentation_002.png", batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_img("./output/")
    res.save_to_json("./output/res.json")
```
关于更多 PaddleX 的单模型推理的 API 的使用方法，可以参考[PaddleX单模型Python脚本使用说明](../../instructions/model_python_API.md)。

## 四、二次开发
如果你追求更高精度的现有模型，可以使用PaddleX的二次开发能力，开发更好的语义分割模型。在使用PaddleX开发语义分割模型之前，请务必安装PaddleX的图像分割相关的模型训练能力，安装过程可以参考 [PaddleX本地安装教程](../../../installation/installation.md)中的二次开发部分。

### 4.1 数据准备
在进行模型训练前，需要准备相应任务模块的数据集。PaddleX 针对每一个模块提供了数据校验功能，**只有通过数据校验的数据才可以进行模型训练**。此外，PaddleX为每一个模块都提供了 Demo 数据集，您可以基于官方提供的 Demo 数据完成后续的开发。

#### 4.1.1 Demo 数据下载
您可以参考下面的命令将 Demo 数据集下载到指定文件夹：

```bash
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/seg_optic_examples.tar -P ./dataset
tar -xf ./dataset/seg_optic_examples.tar -C ./dataset/
```
#### 4.1.2 数据校验
一行命令即可完成数据校验：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/seg_optic_examples
```
执行上述命令后，PaddleX 会对数据集进行校验，并统计数据集的基本信息，命令运行成功后会在log中打印出 `Check dataset passed !` 信息。校验结果文件保存在`./output/check_dataset_result.json`，同时相关产出会保存在当前目录的`./output/check_dataset`目录下，产出目录中包括可视化的示例样本图片和样本分布直方图。

<details>
  <summary>👉 <b>校验结果详情（点击展开）</b></summary>


校验结果文件具体内容为：

```bash
{
  "done_flag": true,
  "check_pass": true,
  "attributes": {
    "train_sample_paths": [
      "check_dataset/demo_img/P0005.jpg",
      "check_dataset/demo_img/P0050.jpg"
    ],
    "train_samples": 267,
    "val_sample_paths": [
      "check_dataset/demo_img/N0139.jpg",
      "check_dataset/demo_img/P0137.jpg"
    ],
    "val_samples": 76,
    "num_classes": 2
  },
  "analysis": {
    "histogram": "check_dataset/histogram.png"
  },
  "dataset_path": "./dataset/seg_optic_examples",
  "show_type": "image",
  "dataset_type": "SegDataset"
}
```
上述校验结果中，check_pass 为 True 表示数据集格式符合要求，其他部分指标的说明如下：

* `attributes.num_classes`：该数据集类别数为 2；
* `attributes.train_samples`：该数据集训练集样本数量为 267；
* `attributes.val_samples`：该数据集验证集样本数量为 76；
* `attributes.train_sample_paths`：该数据集训练集样本可视化图片相对路径列表；
* `attributes.val_sample_paths`：该数据集验证集样本可视化图片相对路径列表；


数据集校验还对数据集中所有类别的样本数量分布情况进行了分析，并绘制了分布直方图（histogram.png）：

![](https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/modules/semanticseg/01.png)
</details>

#### 4.1.3 数据集格式转换/数据集划分（可选）（点击展开）
<details>
  <summary>👉 <b>格式转换/数据集划分详情（点击展开）</b></summary>


在您完成数据校验之后，可以通过修改配置文件或是追加超参数的方式对数据集的格式进行转换，也可以对数据集的训练/验证比例进行重新划分。

**（1）数据集格式转换**

语义分割支持 `LabelMe` 格式的数据集转换为要求的格式。

数据集校验相关的参数可以通过修改配置文件中 `CheckDataset` 下的字段进行设置，配置文件中部分参数的示例说明如下：

* `CheckDataset`:
  * `convert`:
    * `enable`: 是否进行数据集格式转换，支持`LabelMe` 格式的数据集转换，默认为 `False`;
    * `src_dataset_type`: 如果进行数据集格式转换，则需设置源数据集格式，默认为 `null`，支持的源数据集格式是`LabelMe`；
例如，您想转换 `LabelMe` 格式的数据集，提供了一个`LabelMe` 格式的示例数据集，如下：

```bash
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/seg_dataset_to_convert.tar -P ./dataset
tar -xf ./dataset/seg_dataset_to_convert.tar -C ./dataset/
```
下载后，需要修改 `paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml`配置如下：

```bash
......
CheckDataset:
  ......
  convert:
    enable: True
    src_dataset_type: LabelMe
  ......
```
随后执行命令：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/seg_dataset_to_convert
```
当然，以上参数同样支持通过追加命令行参数的方式进行设置，以 `LabelMe` 格式的数据集为例：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/seg_dataset_to_convert \
    -o CheckDataset.convert.enable=True \
    -o CheckDataset.convert.src_dataset_type=LabelMe
```
**（2）数据集划分**

数据集划分的参数可以通过修改配置文件中 CheckDataset 下的字段进行设置，配置文件中部分参数的示例说明如下：

* CheckDataset:
  * split:
    * enable: 是否进行重新划分数据集，为 True 时进行数据集格式转换，默认为 False；
    * train_percent: 如果重新划分数据集，则需要设置训练集的百分比，类型为0-100之间的任意整数，需要保证与 val_percent 的值之和为100；


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
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/seg_optic_examples
```
数据划分执行之后，原有标注文件会被在原路径下重命名为 xxx.bak。

以上参数同样支持通过追加命令行参数的方式进行设置：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml  \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/seg_optic_examples \
    -o CheckDataset.split.enable=True \
    -o CheckDataset.split.train_percent=90 \
    -o CheckDataset.split.val_percent=10
```
</details>

### 4.2 模型训练
一条命令即可完成模型的训练，此处以移动端语义分割模型PP-LiteSeg-T的训练为例：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=train \
    -o Global.dataset_dir=./dataset/seg_optic_examples
```


需要如下几步：

* 指定模型的.yaml 配置文件路径（此处为 `PP-LiteSeg-T.yam`，训练其他模型时，需要的指定相应的配置文件，模型和配置的文件的对应关系，可以查阅[PaddleX模型列表（CPU/GPU）](../../../support_list/models_list.md)）
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

## 4.3 模型评估
在完成模型训练后，可以对指定的模型权重文件在验证集上进行评估，验证模型精度。使用 PaddleX 进行模型评估，一条命令即可完成模型的评估：

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=evaluate \
    -o Global.dataset_dir=./dataset/seg_optic_examples
```
与模型训练类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-LiteSeg-T.yaml`）
* 指定模式为模型评估：`-o Global.mode=evaluate`
* 指定验证数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Evaluate`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

<details>
  <summary>👉 <b>更多说明（点击展开）</b></summary>


在模型评估时，需要指定模型权重文件路径，每个配置文件中都内置了默认的权重保存路径，如需要改变，只需要通过追加命令行参数的形式进行设置即可，如`-o Evaluate.weight_path=``./output/best_model/best_model.pdparams`。

在完成模型评估后，通常有以下产出：

在完成模型评估后，会产出`evaluate_result.json，其记录了`评估的结果，具体来说，记录了评估任务是否正常完成，以及模型的评估指标，包含 Top1 Acc

</details>

### 4.4 模型推理和模型集成
在完成模型的训练和评估后，即可使用训练好的模型权重进行推理预测或者进行Python集成。

#### 4.4.1 模型推理
通过命令行的方式进行推理预测，只需如下一条命令。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_semantic_segmentation_002.png)到本地。

```bash
python main.py -c paddlex/configs/semantic_segmentation/PP-LiteSeg-T.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir="./output/best_model" \
    -o Predict.input="general_semantic_segmentation_002.png"
```
与模型训练和评估类似，需要如下几步：

* 指定模型的.yaml 配置文件路径（此处为` PP-LiteSeg-T.yaml`）
* 指定模式为模型推理预测：`-o Global.mode=predict`
* 指定模型权重路径：`-o Predict.model_dir="./output/best_model/inference"`
* 指定输入数据路径：`-o Predict.input="..."`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Predict`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

#### 4.4.2 模型集成
模型可以直接集成到PaddleX产线中，也可以直接集成到您自己的项目中。

1.**产线集成**

文档图像分类模块可以集成的PaddleX产线有[通用语义分割](../../../pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.md)，只需要替换模型路径即可完成文本检测模块的模型更新。在产线集成中，你可以使用高性能部署和服务化部署来部署你得到的模型。

2.**模块集成**

您产出的权重可以直接集成到语义分割模块中，可以参考[快速集成](#三快速集成)的 Python 示例代码，只需要将模型替换为你训练的到的模型路径即可。
