---
comments: true
typora-copy-images-to: images
hide:
  - navigation
  - toc
---

<p align="center">
  <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/logo.png" width="735" height ="200" alt="PaddleX" align="middle" />
</p>

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-red.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/Python-3.8%2C%203.9%2C%203.10-blue.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Windows%2C%20Mac-orange.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/Hardware-CPU%2C%20GPU%2C%20XPU%2C%20NPU%2C%20MLU%2C%20DCU-yellow.svg"></a>
</p>



## 🔍 Introduction

PaddleX 3.0 is a low-code development tool for AI models built on the PaddlePaddle framework. It integrates numerous<b>ready-to-use pre-trained models</b>, enabling<b>full-process development</b>from model training to inference, supporting<b>a variety of mainstream hardware</b> both domestic and international, and aiding AI developers in industrial practice.

<style>
        .centered-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .centered-table th, .centered-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        .centered-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .centered-table img {
            max-width: 100px;
            height: auto;
        }
</style>

<table class="centered-table">
        <tr>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_classification.md"><strong>Image Classification</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.md"><strong>Multi-label Image Classification</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/object_detection.md"><strong>Object Detection</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.md"><strong>Instance Segmentation</strong></a></th>
        </tr>
        <tr>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/b302cd7e-e027-4ea6-86d0-8a4dd6d61f39"></td>
            <td><img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/multilabel_cls.png"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/099e2b00-0bbe-4b20-9c5a-96b69e473bd2"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/09f683b4-27df-4c24-b8a7-84da20fdd182"></td>
        </tr>
        <tr>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.md"><strong>Semantic Segmentation</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.md"><strong>Image Anomaly Detection</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/OCR.md"><strong>OCR</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition.md"><strong>Table Recognition</strong></a></th>
        </tr>
        <tr>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/02637f8c-f248-415b-89ab-1276505f198c"></td>
            <td><img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/image_anomaly_detection.png"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1ef48536-48d4-484b-a6fb-0d6631ba2386"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1e798e05-dee7-4b41-9cc4-6708b6014efa"></td>
        </tr>
        <tr>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.md"><strong>PP-ChatOCRv3-doc</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.md"><strong>Time Series Forecasting</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.md"><strong>Time Series Anomaly Detection</strong></a></th>
            <th><a href="https://amberc0209.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.md"><strong>Time Series Classification</strong></a></th>
        </tr>
        <tr>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/e3d97f4e-ab46-411c-8155-494c61492b0a"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/6e897bf6-35fe-45e6-a040-e9a1a20cfdf2"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/c54c66cc-da4f-4631-877b-43b0fbb192a6"></td>
            <td><img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/0ce925b2-3776-4dde-8ce0-5156d5a2476e"></td>
        </tr>
    </table>

## 🌟 Why PaddleX ?

  🎨 **Rich Models One-click Call**: Integrate over **200 PaddlePaddle models** covering multiple key areas such as OCR, object detection, and time series forecasting into **19 pipelines**. Experience the model effects quickly through easy Python API calls. Also supports **more than 20 modules** for easy model combination use by developers.

  🚀 **High Efficiency and Low barrier of entry**: Achieve model **full-process development** based on graphical interfaces and unified commands, creating **8 featured model pipelines** that combine large and small models, semi-supervised learning of large models, and multi-model fusion, greatly reducing the cost of iterating models.

  🌐 **Flexible Deployment in Various Scenarios**: Support various deployment methods such as **high-performance inference**, **service deployment**, and **lite deployment** to ensure efficient operation and rapid response of models in different application scenarios.

  🔧 **Efficient Support for Mainstream Hardware**: Support seamless switching of various mainstream hardware such as NVIDIA GPUs, Kunlun XPU, Ascend NPU, and Cambricon MLU to ensure efficient operation.

## 📣 Recent Updates

🔥🔥 **"PaddleX Document Information Personalized Extraction Upgrade"**, PP-ChatOCRv3 innovatively provides custom development functions for OCR models based on data fusion technology, offering stronger model fine-tuning capabilities. Millions of high-quality general OCR text recognition data are automatically integrated into vertical model training data at a specific ratio, solving the problem of weakened general text recognition capabilities caused by vertical model training in the industry. Suitable for practical scenarios in industries such as automated office, financial risk control, healthcare, education and publishing, and legal and government sectors. **October 24th (Thursday) 19:00** Join our live session for an in-depth analysis of the open-source version of PP-ChatOCRv3 and the outstanding advantages of PaddleX 3.0 Beta1 in terms of accuracy and speed. [Registration Link](https://www.wjx.top/vm/wpPu8HL.aspx?udsid=994465)

🔥🔥 **9.30, 2024**, PaddleX 3.0 Beta1 open source version is officially released, providing **more than 200 models** that can be called with a simple Python API; achieve model full-process development based on unified commands, and open source the basic capabilities of the **PP-ChatOCRv3** pipeline; support **more than 100 models for high-performance inference and service-oriented deployment** (iterating continuously), **more than 7 key visual models for edge-deployment**; **more than 70 models have been adapted for the full development process of Ascend 910B**, **more than 15 models have been adapted for the full development process of Kunlun chips and Cambricon**

🔥 **6.27, 2024**, PaddleX 3.0 Beta open source version is officially released, supporting the use of various mainstream hardware for pipeline and model development in a low-code manner on the local side.

🔥 **3.25, 2024**, PaddleX 3.0 cloud release, supporting the creation of pipelines in the AI Studio Galaxy Community in a zero-code manner.

## 🔠 Explanation of Pipeline
PaddleX is dedicated to achieving pipeline-level model training, inference, and deployment. A pipeline refers to a series of predefined development processes for specific AI tasks, which includes a combination of single models (single-function modules) capable of independently completing a certain type of task.

## 📊 What can PaddleX do？


All pipelines of PaddleX support **online experience** on [AI Studio]((https://aistudio.baidu.com/overview)) and local **fast inference**. You can quickly experience the effects of each pre-trained pipeline. If you are satisfied with the effects of the pre-trained pipeline, you can directly perform [high-performance inference](./docs/pipeline_deploy/high_performance_inference_en.md) / [serving deployment](./docs/pipeline_deploy/service_deploy_en.md) / [edge deployment](./docs/pipeline_deploy/edge_deploy_en.md) on the pipeline. If not satisfied, you can also **Custom Development** to improve the pipeline effect. For the complete pipeline development process, please refer to the [PaddleX pipeline Development Tool Local Use Tutorial](./docs/pipeline_usage/pipeline_develop_guide_en.md).

In addition, PaddleX provides developers with a full-process efficient model training and deployment tool based on a [cloud-based GUI](https://aistudio.baidu.com/pipeline/mine). Developers **do not need code development**, just need to prepare a dataset that meets the pipeline requirements to **quickly start model training**. For details, please refer to the tutorial ["Developing Industrial-level AI Models with Zero Barrier"](https://aistudio.baidu.com/practical/introduce/546656605663301).

<table class="centered-table">
    <tr>
        <th>Pipeline</th>
        <th>Online Experience</th>
        <th>Local Inference</th>
        <th>High-Performance Inference</th>
        <th>Service-Oriented Deployment</th>
        <th>Edge Deployment</th>
        <th>Custom Development</th>
        <th><a href="https://aistudio.baidu.com/pipeline/mine">Zero-Code Development On AI Studio</a></td> 
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/OCR_en.md">OCR</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/91660/webUI?source=appMineRecent">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction_en.md">PP-ChatOCRv3</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/182491/webUI?source=appCenter">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/table_recognition_en.md">Table Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/91661?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/object_detection_en.md">Object Detection</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/70230/webUI?source=appMineRecent">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/instance_segmentation_en.md">Instance Segmentation</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100063/webUI?source=appMineRecent">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_classification_en.md">Image Classification</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100061/webUI?source=appMineRecent">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation_en.md">Semantic Segmentation</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100062/webUI?source=appMineRecent">Link</a></td> 
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting_en.md">Time Series Forecasting</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105706/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection_en.md">Time Series Anomaly Detection</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105708/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/time_series_pipelines/time_series_classification_en.md">Time Series Classification</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105707/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
        <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/small_object_detection_en.md">Small Object Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
        <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification_en.md">Multi-label Image Classification</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection_en.md">Image Anomaly Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/layout_parsing_en.md">Layout Parsing</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/formula_recognition_en.md">Formula Recognition</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="./docs/pipeline_usage/tutorials/ocr_pipelines/seal_recognition_en.md">Seal Recognition</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>Image Recognition</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>Pedestrian Attribute Recognition</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>Vehicle Attribute Recognition</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td>Face Recognition</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
</table>

> ❗Note: The above capabilities are implemented based on GPU/CPU. PaddleX can also perform local inference and custom development on mainstream hardware such as Kunlunxin, Ascend, Cambricon, and Haiguang. The table below details the support status of the pipelines. For specific supported model lists, please refer to the [Model List (Kunlunxin XPU)](./docs/support_list/model_list_xpu_en.md)/[Model List (Ascend NPU)](./docs/support_list/model_list_npu_en.md)/[Model List (Cambricon MLU)](./docs/support_list/model_list_mlu_en.md)/[Model List (Haiguang DCU)](./docs/support_list/model_list_dcu_en.md). We are continuously adapting more models and promoting the implementation of high-performance and service-oriented deployment on mainstream hardware.

🔥🔥 **Support for Domestic Hardware Capabilities**

<table class="centered-table">
  <tr>
    <th>Pipeline</th>
    <th>Ascend 910B</th>
    <th>Kunlunxin R200/R300</th>
    <th>Cambricon MLU370X8</th>
    <th>Haiguang Z100</th>
  </tr>
  <tr>
    <td>OCR</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Table Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Object Detection</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Instance Segmentation</td>
    <td>✅</td>
    <td>🚧</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Image Classification</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Semantic Segmentation</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Time Series Forecasting</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Time Series Anomaly Detection</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Time Series Classification</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
</table>

## 💬 Discussion

We warmly welcome and encourage community members to raise questions, share ideas, and feedback in the [Discussions](https://github.com/PaddlePaddle/PaddleX/discussions) section. Whether you want to report a bug, discuss a feature request, seek help, or just want to keep up with the latest project news, this is a great platform.

## 📄 License

The release of this project is licensed under the [Apache 2.0 license](https://github.com/PaddlePaddle/PaddleX/blob/release/3.0-beta/LICENSE).
