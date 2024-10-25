<p align="center">
  <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/logo.png" width="735" height ="200" alt="PaddleX" align="middle" />
</p>

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-red.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/Python-3.8%2C%203.9%2C%203.10-blue.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Windows%2C%20Mac-orange.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/Hardware-CPU%2C%20GPU%2C%20XPU%2C%20NPU%2C%20MLU%2C%20DCU-yellow.svg"></a>
</p>

<h4 align="center">
  <a href=#-特性>🌟 特性</a> | <a href=https://aistudio.baidu.com/pipeline/mine>🌐 在线体验</a>｜<a href=#️-快速开始>🚀 快速开始</a> | <a href=#-文档> 📖 文档</a> | <a href=#-能力支持> 🔥能力支持</a> | <a href=./docs/support_list/models_list.md> 📋 模型列表</a>

</h4>

<h5 align="center">
  <a href="README.md">🇨🇳 简体中文</a> | <a href="README_en.md">🇬🇧 English</a></a>
</h5>

## 🔍 简介

PaddleX 3.0 是基于飞桨框架构建的低代码开发工具，它集成了众多**开箱即用的预训练模型**，可以实现模型从训练到推理的**全流程开发**，支持国内外**多款主流硬件**，助力AI 开发者进行产业实践。

|                                                            [**通用图像分类**](./docs/pipeline_usage/tutorials/cv_pipelines/image_classification.md)                                                            |                                                            [**图像多标签分类**](./docs/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.md)                                                            |                                                            [**通用目标检测**](./docs/pipeline_usage/tutorials/cv_pipelines/object_detection.md)                                                            |                                                            [**通用实例分割**](./docs/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.md)                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/b302cd7e-e027-4ea6-86d0-8a4dd6d61f39" height="126px" width="180px"> | <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/multilabel_cls.png" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/099e2b00-0bbe-4b20-9c5a-96b69e473bd2" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/09f683b4-27df-4c24-b8a7-84da20fdd182" height="126px" width="180px"> |
|                                                              [**通用语义分割**](./docs/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.md)                                                               |                                                            [**图像异常检测**](./docs/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.md)                                                            |                                                         [ **通用OCR**](./docs/pipeline_usage/tutorials/ocr_pipelines/OCR.md)                                                          |                                                          [**通用表格识别**](./docs/pipeline_usage/tutorials/ocr_pipelines/table_recognition.md)                                                          |
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/02637f8c-f248-415b-89ab-1276505f198c" height="126px" width="180px"> | <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/image_anomaly_detection.png" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1ef48536-48d4-484b-a6fb-0d6631ba2386" height="126px" width="180px"> |  <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1e798e05-dee7-4b41-9cc4-6708b6014efa" height="126px" width="180px"> |
|                                                              [**文本图像智能分析**](./docs/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.md)                                                              |                                                            [**时序预测**](./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.md)                                                            |                                                              [**时序异常检测**](./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.md)                                                              |                                                         [**时序分类**](./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.md)                                                         |
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/e3d97f4e-ab46-411c-8155-494c61492b0a" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/6e897bf6-35fe-45e6-a040-e9a1a20cfdf2" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/c54c66cc-da4f-4631-877b-43b0fbb192a6" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/0ce925b2-3776-4dde-8ce0-5156d5a2476e" height="126px" width="180px"> |

## 🌟 特性
  🎨 **模型丰富一键调用**：将覆盖文本图像智能分析、OCR、目标检测、时序预测等多个关键领域的 **200+ 飞桨模型**整合为 **19 条模型产线**，通过极简的 Python API 一键调用，快速体验模型效果。同时支持 **20+ 单功能模块**，方便开发者进行模型组合使用。

  🚀 **提高效率降低门槛**：实现基于统一命令和图形界面的模型**全流程开发**，打造大小模型结合、大模型半监督学习和多模型融合的[**8 条特色模型产线**](https://aistudio.baidu.com/intro/paddlex)，大幅度降低迭代模型的成本。

  🌐 **多种场景灵活部署**：支持**高性能部署**、**服务化部署**和**端侧部署**等多种部署方式，确保不同应用场景下模型的高效运行和快速响应。

  🔧 **主流硬件高效支持**：支持英伟达 GPU、昆仑芯、昇腾和寒武纪等**多种主流硬件**的无缝切换，确保高效运行。

## 📣 近期更新

🔥🔥 **2024.9.30**，PaddleX 3.0 Beta1 开源版正式发布，提供 **200+ 模型** 通过极简的 Python API 一键调用；实现基于统一命令的模型全流程开发，并开源 **PP-ChatOCRv3** 特色模型产线基础能力；支持 **100+ 模型高性能推理和服务化部署**（持续迭代中），**4条模型产线8个重点视觉模型端侧部署**；**100+ 模型开发全流程适配昇腾 910B**，**39+ 模型开发全流程适配昆仑芯和寒武纪**。低成本完成一站式全流程开发，加速产业应用。新增文本图像智能分析利器，大小模型融合策略显著增强版面解析能力，实现高精度实时预测。**10月24日（周四）19：00**直播为您深度解析 PP-ChatOCRv3 开源版本以及 PaddleX 3.0 Beta1 在精度、速度方面的卓越优势。 [报名链接](https://www.wjx.top/vm/wpPu8HL.aspx?udsid=994465)

🔥 **2024.6.27**，PaddleX 3.0 Beta 开源版正式发布，支持以低代码的方式在本地端使用多种主流硬件进行产线和模型开发。

🔥 **2024.3.25**，PaddleX 3.0 云端发布，支持在 AI Studio 星河社区 以零代码的方式【创建产线】使用。

 ## 🔠 模型产线说明

 **PaddleX 致力于实现产线级别的模型训练、推理与部署。模型产线是指一系列预定义好的、针对特定AI任务的开发流程，其中包含能够独立完成某类任务的单模型（单功能模块）组合。**


 ## 📊 能力支持


PaddleX的各个产线均支持本地**快速推理**，部分模型支持在[AI Studio星河社区](https://aistudio.baidu.com/overview)上进行**在线体验**，您可以快速体验各个产线的预训练模型效果，如果您对产线的预训练模型效果满意，可以直接对产线进行[高性能推理](./docs/pipeline_deploy/high_performance_inference.md)/[服务化部署](./docs/pipeline_deploy/service_deploy.md)/[端侧部署](./docs/pipeline_deploy/edge_deploy.md)，如果不满意，您也可以使用产线的**二次开发**能力，提升效果。完整的产线开发流程请参考[PaddleX产线使用概览](./docs/pipeline_usage/pipeline_develop_guide.md)或各产线使用[教程](#-文档)。


此外，PaddleX在[AI Studio星河社区](https://aistudio.baidu.com/overview)为开发者提供了基于[云端图形化开发界面](https://aistudio.baidu.com/pipeline/mine)的全流程开发工具, 点击【创建产线】，选择对应的任务场景和模型产线，就可以开启全流程开发。详细请参考[教程《零门槛开发产业级AI模型》](https://aistudio.baidu.com/practical/introduce/546656605663301)

<table >
    <tr>
        <th>模型产线</th>
        <th>在线体验</th>
        <th>快速推理</th>
        <th>高性能推理</th>
        <th>服务化部署</th>
        <th>端侧部署</th>
        <th>二次开发</th>
        <th><a href = "https://aistudio.baidu.com/pipeline/mine">星河零代码产线</a></td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/OCR.md">通用OCR</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/91660/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.md">文档场景信息抽取v3</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/182491/webUI?source=appCenter">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/table_recognition.md">通用表格识别</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/91661?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/object_detection.md">通用目标检测</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/70230/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.md">通用实例分割</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/100063/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_classification.md">通用图像分类</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/100061/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.md">通用语义分割</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/100062/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.md">时序预测</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/105706/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.md">时序异常检测</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/105708/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.md">时序分类</a></td>
        <td><a href = "https://aistudio.baidu.com/community/app/105707/webUI?source=appMineRecent">链接</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
        <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/small_object_detection.md">小目标检测</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
        <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.md">图像多标签分类</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.md">图像异常检测</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/layout_parsing.md">通用版面解析</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/formula_recognition.md">公式识别</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/seal_recognition.md">印章文本识别</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>通用图像识别</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>行人属性识别</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>车辆属性识别</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>人脸识别</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>


</table>

> ❗注：以上功能均基于 GPU/CPU 实现。PaddleX 还可在昆仑芯、昇腾、寒武纪和海光等主流硬件上进行快速推理和二次开发。下表详细列出了模型产线的支持情况，具体支持的模型列表请参阅[模型列表(昆仑芯XPU)](./docs/support_list/model_list_xpu.md)/[模型列表(昇腾NPU)](./docs/support_list/model_list_npu.md)/[模型列表(寒武纪MLU)](./docs/support_list/model_list_mlu.md)/[模型列表(海光DCU)](./docs/support_list/model_list_dcu.md)。我们正在适配更多的模型，并在主流硬件上推动高性能和服务化部署的实施。

🔥🔥 **国产化硬件能力支持**

<table>
  <tr>
    <th>模型产线</th>
    <th>昇腾 910B</th>
    <th>昆仑芯 R200/R300</th>
    <th>寒武纪 MLU370X8</th>
    <th>海光 Z100</th>
  </tr>
  <tr>
    <td>通用OCR</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>通用表格识别</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>通用目标检测</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>通用实例分割</td>
    <td>✅</td>
    <td>🚧</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>通用图像分类</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>通用语义分割</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>时序预测</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>时序异常检测</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>时序分类</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
</table>

## 💬 Discussion

我们非常欢迎并鼓励社区成员在 [Discussions](https://github.com/PaddlePaddle/PaddleX/discussions) 板块中提出问题、分享想法和反馈。无论您是想要报告一个 bug、讨论一个功能请求、寻求帮助还是仅仅想要了解项目的最新动态，这里都是一个绝佳的平台。


## 📄 许可证书

本项目的发布受 [Apache 2.0 license](./LICENSE) 许可认证。
