[简体中文](instance_segmentation.md) | English

# General Instance Segmentation Pipeline Tutorial

## 1. Introduction to the General Instance Segmentation Pipeline
Instance segmentation is a computer vision task that not only identifies the object categories in an image but also distinguishes the pixels of different instances within the same category, enabling precise segmentation of each object. Instance segmentation can separately label each car, person, or animal in an image, ensuring they are independently processed at the pixel level. For example, in a street scene image containing multiple cars and pedestrians, instance segmentation can clearly separate the contours of each car and person, forming multiple independent region labels. This technology is widely used in autonomous driving, video surveillance, and robotic vision, often relying on deep learning models (such as Mask R-CNN) to achieve efficient pixel classification and instance differentiation through Convolutional Neural Networks (CNNs), providing powerful support for understanding complex scenes.

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/instance_segmentation/01.png">


<b>The General Instance Segmentation Pipeline includes a</b> <b>Object Detection</b> <b>module. If you prioritize model precision, choose a model with higher precision. If you prioritize inference speed, choose a model with faster inference. If you prioritize model storage size, choose a model with a smaller storage size.</b>

<details>
   <summary> 👉Model List Details</summary>

<table>
<thead>
<tr>
<th>Model Name</th>
<th>Mask AP</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time (ms)</th>
<th>Model Size (M)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mask-RT-DETR-H</td>
<td>50.6</td>
<td>132.693</td>
<td>4896.17</td>
<td>449.9</td>
</tr>
<tr>
<td>Mask-RT-DETR-L</td>
<td>45.7</td>
<td>46.5059</td>
<td>2575.92</td>
<td>113.6</td>
</tr>
<tr>
<td>Mask-RT-DETR-M</td>
<td>42.7</td>
<td>36.8329</td>
<td>-</td>
<td>66.6 M</td>
</tr>
<tr>
<td>Mask-RT-DETR-S</td>
<td>41.0</td>
<td>33.5007</td>
<td>-</td>
<td>51.8 M</td>
</tr>
<tr>
<td>Mask-RT-DETR-X</td>
<td>47.5</td>
<td>75.755</td>
<td>3358.04</td>
<td>237.5 M</td>
</tr>
<tr>
<td>Cascade-MaskRCNN-ResNet50-FPN</td>
<td>36.3</td>
<td>-</td>
<td>-</td>
<td>254.8</td>
</tr>
<tr>
<td>Cascade-MaskRCNN-ResNet50-vd-SSLDv2-FPN</td>
<td>39.1</td>
<td>-</td>
<td>-</td>
<td>254.7</td>
</tr>
<tr>
<td>MaskRCNN-ResNet50-FPN</td>
<td>35.6</td>
<td>-</td>
<td>-</td>
<td>157.5 M</td>
</tr>
<tr>
<td>MaskRCNN-ResNet50-vd-FPN</td>
<td>36.4</td>
<td>-</td>
<td>-</td>
<td>157.5 M</td>
</tr>
<tr>
<td>MaskRCNN-ResNet50</td>
<td>32.8</td>
<td>-</td>
<td>-</td>
<td>127.8 M</td>
</tr>
<tr>
<td>MaskRCNN-ResNet101-FPN</td>
<td>36.6</td>
<td>-</td>
<td>-</td>
<td>225.4 M</td>
</tr>
<tr>
<td>MaskRCNN-ResNet101-vd-FPN</td>
<td>38.1</td>
<td>-</td>
<td>-</td>
<td>225.1 M</td>
</tr>
<tr>
<td>MaskRCNN-ResNeXt101-vd-FPN</td>
<td>39.5</td>
<td>-</td>
<td>-</td>
<td>370.0 M</td>
</tr>
<tr>
<td>PP-YOLOE_seg-S</td>
<td>32.5</td>
<td>-</td>
<td>-</td>
<td>31.5 M</td>
</tr>
<tr>
<td>SOLOv2</td>
<td>35.5</td>
<td>-</td>
<td>-</td>
<td>179.1 M</td>
</tr>
</tbody>
</table>

<b>Note: The above accuracy metrics are Mask AP(0.5:0.95) on the </b>[COCO2017](https://cocodataset.org/#home)<b> validation set. All GPU inference times are based on an NVIDIA Tesla T4 machine with FP32 precision. CPU inference speeds are based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>

</details>

## 2. Quick Start
The pre-trained model pipelines provided by PaddleX allow for quick experience of the effects. You can experience the effects of the General Instance Segmentation Pipeline online or locally using command line or Python.

### 2.1 Online Experience
You can [experience online](https://aistudio.baidu.com/community/app/100063/webUI) the effects of the General Instance Segmentation Pipeline using the demo images provided by the official. For example:

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/instance_segmentation/02.png">

If you are satisfied with the pipeline's performance, you can directly integrate and deploy it. If not, you can also use your private data to <b>fine-tune the model within the pipeline</b>.

### 2.2 Local Experience
Before using the General Image Classification Pipeline locally, ensure you have installed the PaddleX wheel package following the [PaddleX Local Installation Tutorial](../../../installation/installation.en.md).

#### 2.2.1 Command Line Experience
A single command is all you need to quickly experience the image classification pipeline, Use the [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_instance_segmentation_004.png), and replace `--input` with the local path to perform prediction.


```bash
paddlex --pipeline instance_segmentation --input  general_instance_segmentation_004.png --device gpu:0
```

Parameter Description:

```
--pipeline: The name of the pipeline, here it refers to the object detection pipeline.
--input: The local path or URL of the input image to be processed.
--device: The GPU index to use (e.g., gpu:0 indicates using the first GPU, gpu:1,2 indicates using the second and third GPUs), or you can choose to use CPU (--device cpu).
```

When executing the above Python script, the default instance segmentation pipeline configuration file is loaded. If you need to customize the configuration file, you can execute the following command to obtain it:

<details>
   <summary> 👉Click to expand</summary>

```
paddlex --get_pipeline_config instance_segmentation
```

After execution, the instance segmentation pipeline configuration file will be saved in the current path. If you wish to customize the save location, you can execute the following command (assuming the custom save location is `./my_path`):

```
paddlex --get_pipeline_config instance_segmentation --save_path ./my_path
```

After obtaining the pipeline configuration file, you can replace `--pipeline` with the configuration file save path to make the configuration file take effect. For example, if the configuration file save path is `./instance_segmentation.yaml`, simply execute:

```bash
paddlex --pipeline ./instance_segmentation.yaml --input general_instance_segmentation_004.png --device gpu:0
```

Where `--model`, `--device`, and other parameters do not need to be specified, and the parameters in the configuration file will be used. If parameters are still specified, the specified parameters will take precedence.

</details>

After running, the result is:

```
{'input_path': 'general_instance_segmentation_004.png', 'boxes': [{'cls_id': 0, 'label': 'person', 'score': 0.8698326945304871, 'coordinate': [339, 0, 639, 575]}, {'cls_id': 0, 'label': 'person', 'score': 0.8571141362190247, 'coordinate': [0, 0, 195, 575]}, {'cls_id': 0, 'label': 'person', 'score': 0.8202633857727051, 'coordinate': [88, 113, 401, 574]}, {'cls_id': 0, 'label': 'person', 'score': 0.7108577489852905, 'coordinate': [522, 21, 767, 574]}, {'cls_id': 27, 'label': 'tie', 'score': 0.554280698299408, 'coordinate': [247, 311, 355, 574]}]}
```

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/instance_segmentation/03.png">

The visualized image not saved by default. You can customize the save path through `--save_path`, and then all results will be saved in the specified path.

#### 2.2.2 Python Script Integration
A few lines of code can complete the quick inference of the pipeline. Taking the general instance segmentation pipeline as an example:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="instance_segmentation")

output = pipeline.predict("general_instance_segmentation_004.png")
for res in output:
    res.print() # Print the structured output of the prediction
    res.save_to_img("./output/") # Save the visualization image of the result
    res.save_to_json("./output/") # Save the structured output of the prediction
```
The results obtained are the same as those obtained through the command line method.

In the above Python script, the following steps are executed:

(1) Instantiate the `create_pipeline` to create a pipeline object: The specific parameter descriptions are as follows:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Type</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pipeline</code></td>
<td>The name of the pipeline or the path to the pipeline configuration file. If it is the name of the pipeline, it must be a pipeline supported by PaddleX.</td>
<td><code>str</code></td>
<td>None</td>
</tr>
<tr>
<td><code>device</code></td>
<td>The device for pipeline model inference. Supports: "gpu", "cpu".</td>
<td><code>str</code></td>
<td>"gpu"</td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>Whether to enable high-performance inference, which is only available when the pipeline supports it.</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>

(2) Call the `predict` method of the image classification pipeline object for inference prediction: The `predict` method parameter is `x`, which is used to input data to be predicted, supporting multiple input methods, as shown in the following examples:

<table>
<thead>
<tr>
<th>Parameter Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python Var</td>
<td>Supports directly passing Python variables, such as numpy.ndarray representing image data.</td>
</tr>
<tr>
<td><code>str</code></td>
<td>Supports passing the path of the file to be predicted, such as the local path of an image file: <code>/root/data/img.jpg</code>.</td>
</tr>
<tr>
<td><code>str</code></td>
<td>Supports passing the URL of the file to be predicted, such as the network URL of an image file: <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_instance_segmentation_004.png">Example</a>.</td>
</tr>
<tr>
<td><code>str</code></td>
<td>Supports passing a local directory, which should contain files to be predicted, such as the local path: <code>/root/data/</code>.</td>
</tr>
<tr>
<td><code>dict</code></td>
<td>Supports passing a dictionary type, where the key needs to correspond to the specific task, such as "img" for the image classification task, and the value of the dictionary supports the above data types, e.g., <code>{"img": "/root/data1"}</code>.</td>
</tr>
<tr>
<td><code>list</code></td>
<td>Supports passing a list, where the list elements need to be the above data types, such as <code>[numpy.ndarray, numpy.ndarray]</code>, <code>["/root/data/img1.jpg", "/root/data/img2.jpg"]</code>, <code>["/root/data1", "/root/data2"]</code>, <code>[{"img": "/root/data1"}, {"img": "/root/data2/img.jpg"}]</code>.</td>
</tr>
</tbody>
</table>

3）Obtain prediction results by calling the `predict` method: The `predict` method is a `generator`, so prediction results need to be obtained through iteration. The `predict` method predicts data in batches, so the prediction results are in the form of a list.

（4）Process the prediction results: The prediction result for each sample is of `dict` type and supports printing or saving to files, with the supported file types depending on the specific pipeline. For example:

<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
<th>Method Parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td>print</td>
<td>Prints results to the terminal</td>
<td><code>- format_json</code>: bool, whether to format the output content with json indentation, default is True;<br><code>- indent</code>: int, json formatting setting, only valid when format_json is True, default is 4;<br><code>- ensure_ascii</code>: bool, json formatting setting, only valid when format_json is True, default is False;</td>
</tr>
<tr>
<td>save_to_json</td>
<td>Saves results as a json file</td>
<td><code>- save_path</code>: str, the path to save the file, when it's a directory, the saved file name is consistent with the input file type;<br><code>- indent</code>: int, json formatting setting, default is 4;<br><code>- ensure_ascii</code>: bool, json formatting setting, default is False;</td>
</tr>
<tr>
<td>save_to_img</td>
<td>Saves results as an image file</td>
<td><code>- save_path</code>: str, the path to save the file, when it's a directory, the saved file name is consistent with the input file type;</td>
</tr>
</tbody>
</table>

If you have a configuration file, you can customize the configurations of the image anomaly detection pipeline by simply modifying the `pipeline` parameter in the `create_pipeline` method to the path of the pipeline configuration file.

For example, if your configuration file is saved at `./my_path/instance_segmentation.yaml`, you only need to execute:

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/instance_segmentation.yaml")
output = pipeline.predict("general_instance_segmentation_004.png")
for res in output:
    res.print() # Print the structured output of prediction
    res.save_to_img("./output/") # Save the visualized image of the result
    res.save_to_json("./output/") # Save the structured output of prediction
```

## 3. Development Integration/Deployment
If the pipeline meets your requirements for inference speed and accuracy, you can proceed with development integration/deployment.

If you need to directly apply the pipeline in your Python project, you can refer to the example code in [2.2.2 Python Script Integration](#222-python-script-integration).

Additionally, PaddleX provides three other deployment methods, detailed as follows:

🚀 <b>High-Performance Inference</b>: In actual production environments, many applications have stringent standards for the performance metrics of deployment strategies (especially response speed) to ensure efficient system operation and smooth user experience. To this end, PaddleX provides high-performance inference plugins that aim to deeply optimize model inference and pre/post-processing for significant speedups in the end-to-end process. For detailed high-performance inference procedures, please refer to the [PaddleX High-Performance Inference Guide](../../../pipeline_deploy/high_performance_inference.en.md).

☁️ <b>Service-Oriented Deployment</b>: Service-oriented deployment is a common deployment form in actual production environments. By encapsulating inference functions as services, clients can access these services through network requests to obtain inference results. PaddleX supports users in achieving low-cost service-oriented deployment of pipelines. For detailed service-oriented deployment procedures, please refer to the [PaddleX Service-Oriented Deployment Guide](../../../pipeline_deploy/service_deploy.en.md).

Below are the API references and multi-language service invocation examples:

<details>
<summary>API Reference</summary>

For all operations provided by the service:

- Both the response body and the request body for POST requests are JSON data (JSON objects).
- When the request is processed successfully, the response status code is `200`, and the response body properties are as follows:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Fixed as <code>0</code>.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error message. Fixed as <code>"Success"</code>.</td>
</tr>
</tbody>
</table>

    The response body may also have a `result` property of type `object`, which stores the operation result information.

- When the request is not processed successfully, the response body properties are as follows:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Same as the response status code.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error message.</td>
</tr>
</tbody>
</table>

Operations provided by the service:

- <b>`infer`</b>

    Performs instance segmentation on an image.

    `POST /instance-segmentation`

    - The request body properties are as follows:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td><code>string</code></td>
<td>The URL of an image file accessible by the service or the Base64 encoded result of the image file content.</td>
<td>Yes</td>
</tr>
</tbody>
</table>

    - When the request is processed successfully, the `result` of the response body has the following properties:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>instances</code></td>
<td><code>array</code></td>
<td>Information about the locations and categories of instances.</td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>string</code></td>
<td>The result image of instance segmentation. The image is in JPEG format and encoded in Base64.</td>
</tr>
</tbody>
</table>

        Each element in `instances` is an `object` with the following properties:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>bbox</code></td>
<td><code>array</code></td>
<td>The location of the instance. The elements in the array are the x-coordinate of the top-left corner, the y-coordinate of the top-left corner, the x-coordinate of the bottom-right corner, and the y-coordinate of the bottom-right corner of the bounding box, respectively.</td>
</tr>
<tr>
<td><code>categoryId</code></td>
<td><code>integer</code></td>
<td>The ID of the instance category.</td>
</tr>
<tr>
<td><code>score</code></td>
<td><code>number</code></td>
<td>The score of the instance.</td>
</tr>
<tr>
<td><code>mask</code></td>
<td><code>object</code></td>
<td>The segmentation mask of the instance.</td>
</tr>
</tbody>
</table>

        The properties of `mask` are as follows:

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rleResult</code></td>
<td><code>str</code></td>
<td>The run-length encoding result of the mask.</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>array</code></td>
<td>The shape of the mask. The elements in the array are the height and width of the mask, respectively.</td>
</tr>
</tbody>
</table>

        An example of `result` is as follows:

        ```json
        {
          "instances": [
            {
              "bbox": [
                162.39381408691406,
                83.88176727294922,
                624.0797119140625,
                343.4986877441406
              ],
              "categoryId": 33,
              "score": 0.8691174983978271,
              "mask": {
                "rleResult": "xxxxxx",
                "size": [
                  259,
                  462
                ]
              }
            }
          ],
          "image": "xxxxxx"
        }
        ```

</details>

<details>
<summary>Multi-Language Service Invocation Examples</summary>

<details>
<summary>Python</summary>

```python
import base64
import requests

API_URL = "http://localhost:8080/instance-segmentation"
image_path = "./demo.jpg"
output_image_path = "./out.jpg"

with open(image_path, "rb") as file:
    image_bytes = file.read()
    image_data = base64.b64encode(image_bytes).decode("ascii")

payload = {"image": image_data}

response = requests.post(API_URL, json=payload)

assert response.status_code == 200
result = response.json()["result"]
with open(output_image_path, "wb") as file:
    file.write(base64.b64decode(result["image"]))
print(f"Output image saved at {output_image_path}")
print("\nInstances:")
print(result["instances"])
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <iostream>
#include "cpp-httplib/httplib.h" // https://github.com/Huiyicc/cpp-httplib
#include "nlohmann/json.hpp" // https://github.com/nlohmann/json
#include "base64.hpp" // https://github.com/tobiaslocker/base64

int main() {
    httplib::Client client("localhost:8080");
    const std::string imagePath = "./demo.jpg";
    const std::string outputImagePath = "./out.jpg";

    httplib::Headers headers = {
        {"Content-Type", "application/json"}
    };

    std::ifstream file(imagePath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> buffer(size);
    if (!file.read(buffer.data(), size)) {
        std::cerr << "Error reading file." << std::endl;
        return 1;
    }
    std::string bufferStr(reinterpret_cast<const char*>(buffer.data()), buffer.size());
    std::string encodedImage = base64::to_base64(bufferStr);

    nlohmann::json jsonObj;
    jsonObj["image"] = encodedImage;
    std::string body = jsonObj.dump();

    auto response = client.Post("/instance-segmentation", headers, body, "application/json");
    if (response && response->status == 200) {
        nlohmann::json jsonResponse = nlohmann::json::parse(response->body);
        auto result = jsonResponse["result"];

        encodedImage = result["image"];
        std::string decodedString = base64::from_base64(encodedImage);
        std::vector<unsigned char> decodedImage(decodedString.begin(), decodedString.end());
        std::ofstream outputImage(outPutImagePath, std::ios::binary | std::ios::out);
        if (outputImage.is_open()) {
            outputImage.write(reinterpret_cast<char*>(decodedImage.data()), decodedImage.size());
            outputImage.close();
            std::cout << "Output image saved at " << outPutImagePath << std::endl;
        } else {
            std::cerr << "Unable to open file for writing: " << outPutImagePath << std::endl;
        }

        auto instances = result["instances"];
        std::cout << "\nInstances:" << std::endl;
        for (const auto& inst : instances) {
            std::cout << inst << std::endl;
        }
    } else {
        std::cout << "Failed to send HTTP request." << std::endl;
        return 1;
    }

    return 0;
}
```

</details>

<details>
<summary>Java</summary>

```java
import okhttp3.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws IOException {
        String API_URL = "http://localhost:8080/instance-segmentation";
        String imagePath = "./demo.jpg";
        String outputImagePath = "./out.jpg";

        File file = new File(imagePath);
        byte[] fileContent = java.nio.file.Files.readAllBytes(file.toPath());
        String imageData = Base64.getEncoder().encodeToString(fileContent);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode params = objectMapper.createObjectNode();
        params.put("image", imageData);

        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.Companion.get("application/json; charset=utf-8");
        RequestBody body = RequestBody.Companion.create(params.toString(), JSON);
        Request request = new Request.Builder()
                .url(API_URL)
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                JsonNode resultNode = objectMapper.readTree(responseBody);
                JsonNode result = resultNode.get("result");
                String base64Image = result.get("image").asText();
                JsonNode instances = result.get("instances");

                byte[] imageBytes = Base64.getDecoder().decode(base64Image);
                try (FileOutputStream fos = new FileOutputStream(outputImagePath)) {
                    fos.write(imageBytes);
                }
                System.out.println("Output image saved at " + outputImagePath);
                System.out.println("\nInstances: " + instances.toString());
            } else {
                System.err.println("Request failed with code: " + response.code());
            }
        }
    }
}
```

</details>

<details>
<summary>Go</summary>

```go
package main

import (
    "bytes"
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    API_URL := "http://localhost:8080/instance-segmentation"
    imagePath := "./demo.jpg"
    outputImagePath := "./out.jpg"

    imageBytes, err := ioutil.ReadFile(imagePath)
    if err != nil {
        fmt.Println("Error reading image file:", err)
        return
    }
    imageData := base64.StdEncoding.EncodeToString(imageBytes)

    payload := map[string]string{"image": imageData}
    payloadBytes, err := json.Marshal(payload)
    if err != nil {
        fmt.Println("Error marshaling payload:", err)
        return
    }

    client := &http.Client{}
    req, err := http.NewRequest("POST", API_URL, bytes.NewBuffer(payloadBytes))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    res, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer res.Body.Close()

    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }
    type Response struct {
        Result struct {
            Image      string   `json:"image"`
            Instances []map[string]interface{} `json:"instances"`
        } `json:"result"`
    }
    var respData Response
    err = json.Unmarshal([]byte(string(body)), &respData)
    if err != nil {
        fmt.Println("Error unmarshaling response body:", err)
        return
    }

    outputImageData, err := base64.StdEncoding.DecodeString(respData.Result.Image)
    if err != nil {
        fmt.Println("Error decoding base64 image data:", err)
        return
    }
    err = ioutil.WriteFile(outputImagePath, outputImageData, 0644)
    if err != nil {
        fmt.Println("Error writing image to file:", err)
        return
    }
    fmt.Printf("Image saved at %s.jpg\n", outputImagePath)
    fmt.Println("\nInstances:")
    for _, inst := range respData.Result.Instances {
        fmt.Println(inst)
    }
}
```

</details>

<details>
<summary>C#</summary>

```csharp
using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class Program
{
    static readonly string API_URL = "http://localhost:8080/instance-segmentation";
    static readonly string imagePath = "./demo.jpg";
    static readonly string outputImagePath = "./out.jpg";

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();

        byte[] imageBytes = File.ReadAllBytes(imagePath);
        string image_data = Convert.ToBase64String(imageBytes);

        var payload = new JObject{ { "image", image_data } };
        var content = new StringContent(payload.ToString(), Encoding.UTF8, "application/json");

        HttpResponseMessage response = await httpClient.PostAsync(API_URL, content);
        response.EnsureSuccessStatusCode();

        string responseBody = await response.Content.ReadAsStringAsync();
        JObject jsonResponse = JObject.Parse(responseBody);

        string base64Image = jsonResponse["result"]["image"].ToString();
        byte[] outputImageBytes = Convert.FromBase64String(base64Image);

        File.WriteAllBytes(outputImagePath, outputImageBytes);
        Console.WriteLine($"Output image saved at {outputImagePath}");
        Console.WriteLine("\nInstances:");
        Console.WriteLine(jsonResponse["result"]["instances"].ToString());
    }
}
```

</details>

<details>
<summary>Node.js</summary>

```js
const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/instance-segmentation'
const imagePath = './demo.jpg'
const outputImagePath = "./out.jpg";

let config = {
   method: 'POST',
   maxBodyLength: Infinity,
   url: API_URL,
   data: JSON.stringify({
    'image': encodeImageToBase64(imagePath)
  })
};

function encodeImageToBase64(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString('base64');
}

axios.request(config)
.then((response) => {
    const result = response.data["result"];
    const imageBuffer = Buffer.from(result["image"], 'base64');
    fs.writeFile(outputImagePath, imageBuffer, (err) => {
      if (err) throw err;
      console.log(`Output image saved at ${outputImagePath}`);
    });
    console.log("\nInstances:");
    console.log(result["instances"]);
})
.catch((error) => {
  console.log(error);
});
```

</details>

<details>
<summary>PHP</summary>

```php
<?php

$API_URL = "http://localhost:8080/instance-segmentation";
$image_path = "./demo.jpg";
$output_image_path = "./out.jpg";

$image_data = base64_encode(file_get_contents($image_path));
$payload = array("image" => $image_data);

$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true)["result"];
file_put_contents($output_image_path, base64_decode($result["image"]));
echo "Output image saved at " . $output_image_path . "\n";
echo "\nInstances:\n";
print_r($result["instances"]);

?>
```

</details>
</details>
<br/>

📱 <b>Edge Deployment</b>: Edge deployment is a method that places computing and data processing functions on the user's device itself, allowing the device to process data directly without relying on remote servers. PaddleX supports deploying models on edge devices such as Android. For detailed edge deployment procedures, please refer to the [PaddleX Edge Deployment Guide](../../../pipeline_deploy/edge_deploy.en.md).
You can choose the appropriate deployment method for your model pipeline based on your needs and proceed with subsequent AI application integration.

## 4. CCustom Development
If the default model weights provided by the general instance segmentation pipeline do not meet your requirements for accuracy or speed in your scenario, you can try to further <b>fine-tune</b> the existing model using <b>data specific to your domain or application scenario</b> to improve the recognition effect of the general instance segmentation pipeline in your scenario.

### 4.1 Model Fine-tuning
Since the general instance segmentation pipeline includes an instance segmentation module, if the performance of the pipeline does not meet expectations, you need to refer to the [Custom Development](../../../module_usage/tutorials/cv_modules/instance_segmentation.en.md#iv-custom-development) section in the [Instance Segmentation Module Development Tutorial](../../../module_usage/tutorials/cv_modules/instance_segmentation.en.md).

### 4.2 Model Application
After you complete fine-tuning training using your private dataset, you will obtain local model weight files.

If you need to use the fine-tuned model weights, simply modify the pipeline configuration file by replacing the local path of the fine-tuned model weights to the corresponding location in the pipeline configuration file:

```python
......
Pipeline:
  model: Mask-RT-DETR-S  # Can be modified to the local path of the fine-tuned model
  device: "gpu"
  batch_size: 1
......
```

Then, refer to the command line method or Python script method in the local experience to load the modified pipeline configuration file.

## 5. Multi-Hardware Support
PaddleX supports various mainstream hardware devices such as NVIDIA GPUs, Kunlun XPU, Ascend NPU, and Cambricon MLU. <b>Simply modify the `--device` parameter</b> to seamlessly switch between different hardware.

For example, if you use an NVIDIA GPU for instance segmentation pipeline inference, the Python command is:

```bash
paddlex --pipeline instance_segmentation --input general_instance_segmentation_004.png --device gpu:0
``````
At this point, if you wish to switch the hardware to Ascend NPU, simply modify the `--device` in the Python command to `npu:0`:

```bash
paddlex --pipeline instance_segmentation --input general_instance_segmentation_004.png --device npu:0
```

If you want to use the General Instance Segmentation Pipeline on more types of hardware, please refer to the [PaddleX Multi-Device Usage Guide](../../../other_devices_support/multi_devices_use_guide.en.md).
