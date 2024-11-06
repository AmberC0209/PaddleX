[简体中文](semantic_segmentation.md) | English

# General Semantic Segmentation Pipeline Tutorial

## 1. Introduction to the General Semantic Segmentation Pipeline
Semantic segmentation is a computer vision technique that aims to assign each pixel in an image to a specific category, enabling a detailed understanding of the image content. Semantic segmentation not only identifies the types of objects in an image but also classifies each pixel, allowing regions of the same category to be fully labeled. For example, in a street scene image, semantic segmentation can distinguish pedestrians, cars, the sky, and roads pixel by pixel, forming a detailed label map. This technology is widely used in autonomous driving, medical image analysis, and human-computer interaction, often relying on deep learning models (such as SegFormer, etc.) to extract features by CNN or Transformer, and achieve high-precision pixel-level classification, providing a foundation for further intelligent analysis.

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/semantic_segmentation/01.png">

<details>
   <summary> 👉 Model List Details</summary>

<table>
<thead>
<tr>
<th>Model Name</th>
<th>mIoU (%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time (ms)</th>
<th>Model Size (M)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Deeplabv3_Plus-R50</td>
<td>80.36</td>
<td>61.0531</td>
<td>1513.58</td>
<td>94.9 M</td>
</tr>
<tr>
<td>Deeplabv3_Plus-R101</td>
<td>81.10</td>
<td>100.026</td>
<td>2460.71</td>
<td>162.5 M</td>
</tr>
<tr>
<td>Deeplabv3-R50</td>
<td>79.90</td>
<td>82.2631</td>
<td>1735.83</td>
<td>138.3 M</td>
</tr>
<tr>
<td>Deeplabv3-R101</td>
<td>80.85</td>
<td>121.492</td>
<td>2685.51</td>
<td>205.9 M</td>
</tr>
<tr>
<td>OCRNet_HRNet-W18</td>
<td>80.67</td>
<td>48.2335</td>
<td>906.385</td>
<td>43.1 M</td>
</tr>
<tr>
<td>OCRNet_HRNet-W48</td>
<td>82.15</td>
<td>78.9976</td>
<td>2226.95</td>
<td>249.8 M</td>
</tr>
<tr>
<td>PP-LiteSeg-T</td>
<td>73.10</td>
<td>7.6827</td>
<td>138.683</td>
<td>28.5 M</td>
</tr>
<tr>
<td>PP-LiteSeg-B</td>
<td>75.25</td>
<td>-</td>
<td>-</td>
<td>47.0 M</td>
</tr>
<tr>
<td>SegFormer-B0 (slice)</td>
<td>76.73</td>
<td>11.1946</td>
<td>268.929</td>
<td>13.2 M</td>
</tr>
<tr>
<td>SegFormer-B1 (slice)</td>
<td>78.35</td>
<td>17.9998</td>
<td>403.393</td>
<td>48.5 M</td>
</tr>
<tr>
<td>SegFormer-B2 (slice)</td>
<td>81.60</td>
<td>48.0371</td>
<td>1248.52</td>
<td>96.9 M</td>
</tr>
<tr>
<td>SegFormer-B3 (slice)</td>
<td>82.47</td>
<td>64.341</td>
<td>1666.35</td>
<td>167.3 M</td>
</tr>
<tr>
<td>SegFormer-B4 (slice)</td>
<td>82.38</td>
<td>82.4336</td>
<td>1995.42</td>
<td>226.7 M</td>
</tr>
<tr>
<td>SegFormer-B5 (slice)</td>
<td>82.58</td>
<td>97.3717</td>
<td>2420.19</td>
<td>229.7 M</td>
</tr>
</tbody>
</table>
<b>The accuracy metrics of the above models are measured on the [Cityscapes](https://www.cityscapes-dataset.com/) dataset. GPU inference time is based on an NVIDIA Tesla T4 machine with FP32 precision. CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>


<table>
<thead>
<tr>
<th>Model Name</th>
<th>mIoU (%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time (ms)</th>
<th>Model Size (M)</th>
</tr>
</thead>
<tbody>
<tr>
<td>SeaFormer_base(slice)</td>
<td>40.92</td>
<td>24.4073</td>
<td>397.574</td>
<td>30.8 M</td>
</tr>
<tr>
<td>SeaFormer_large (slice)</td>
<td>43.66</td>
<td>27.8123</td>
<td>550.464</td>
<td>49.8 M</td>
</tr>
<tr>
<td>SeaFormer_small (slice)</td>
<td>38.73</td>
<td>19.2295</td>
<td>358.343</td>
<td>14.3 M</td>
</tr>
<tr>
<td>SeaFormer_tiny (slice)</td>
<td>34.58</td>
<td>13.9496</td>
<td>330.132</td>
<td>6.1M</td>
</tr>
</tbody>
</table>
<b>The accuracy metrics of the SeaFormer series models are measured on the [ADE20k](https://groups.csail.mit.edu/vision/datasets/ADE20K/) dataset. GPU inference time is based on an NVIDIA Tesla T4 machine with FP32 precision. CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>

</details>

## 2. Quick Start
PaddleX's pre-trained model pipelines can be quickly experienced. You can experience the effects of the General Semantic Segmentation Pipeline online or locally using command line or Python.

### 2.1 Online Experience
You can [experience online](https://aistudio.baidu.com/community/app/100062/webUI?source=appCenter) the effects of the General Semantic Segmentation Pipeline, using the official demo images for recognition, for example:

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/semantic_segmentation/02.png">

If you are satisfied with the pipeline's performance, you can directly integrate and deploy it. If not, you can also use your private data to <b>fine-tune the model in the pipeline online</b>.

### 2.2 Local Experience
Before using the General Semantic Segmentation Pipeline locally, ensure you have installed the PaddleX wheel package following the [PaddleX Local Installation Tutorial](../../../installation/installation.en.md).

#### 2.2.1 Command Line Experience
Experience the semantic segmentation pipeline with a single command, Use the [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/application/semantic_segmentation/makassaridn-road_demo.png), and replace `--input` with the local path to perform prediction.


```bash
paddlex --pipeline semantic_segmentation --input makassaridn-road_demo.png --device gpu:0
```

Parameter Explanation:

```
--pipeline: The name of the pipeline, here it is the semantic segmentation pipeline
--input: The local path or URL of the input image to be processed
--device: The GPU index to use (e.g., gpu:0 for the first GPU, gpu:1,2 for the second and third GPUs), or choose to use CPU (--device cpu)
```

When executing the above command, the default semantic segmentation pipeline configuration file is loaded. If you need to customize the configuration file, you can execute the following command to obtain it:

<details>
   <summary> 👉Click to expand</summary>

```bash
paddlex --get_pipeline_config semantic_segmentation
```
After execution, the semantic segmentation pipeline configuration file will be saved in the current path. If you wish to customize the save location, execute the following command (assuming the custom save location is `./my_path`):

```bash
paddlex --get_pipeline_config semantic_segmentation --save_path ./my_path
```

After obtaining the pipeline configuration file, replace `--pipeline` with the configuration file save path to make the configuration file take effect. For example, if the configuration file save path is `./semantic_segmentation.yaml`, simply execute:

```bash
paddlex --pipeline ./semantic_segmentation.yaml --input makassaridn-road_demo.png --device gpu:0
```

Here, parameters such as `--model` and `--device` do not need to be specified, and the parameters in the configuration file will be used. If parameters are still specified, the specified parameters will take precedence.

</details>

After running, the result is:

```bash
{'input_path': 'general_object_detection_002.png'}
```

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/semantic_segmentation/03.png">

The visualized image not saved by default. You can customize the save path through `--save_path`, and then all results will be saved in the specified path.

#### 2.2.2 Python Script Integration
A few lines of code can complete the quick inference of the pipeline. Taking the general semantic segmentation pipeline as an example:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="semantic_segmentation")

output = pipeline.predict("makassaridn-road_demo.png")
for res in output:
    res.print()  # Print the structured output of the prediction
    res.save_to_img("./output/")  # Save the visualization image of the result
    res.save_to_json("./output/")  # Save the structured output of the prediction
```
The results obtained are the same as those from the command line method.

In the above Python script, the following steps are executed:

(1) Instantiate the `create_pipeline` to create a pipeline object: The specific parameter descriptions are as follows:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Type</th>
<th>Default Value</th>
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
<td><code>enable_hpi</code></td>
<td>Whether to enable high-performance inference, which is only available when the pipeline supports it.</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>
(2) Call the `predict` method of the pipeline object for inference prediction: The `predict` method parameter is `x`, which is used to input data to be predicted, supporting multiple input methods, as shown in the following examples:

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
<td>Supports passing the URL of the file to be predicted, such as the network URL of an image file: <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_object_detection_002.png">Example</a>.</td>
</tr>
<tr>
<td><code>str</code></td>
<td>Supports passing a local directory, which should contain files to be predicted, such as the local path: <code>/root/data/</code>.</td>
</tr>
<tr>
<td><code>dict</code></td>
<td>Supports passing a dictionary type, where the key needs to correspond to a specific task, such as "img" for image classification tasks, and the value of the dictionary supports the above data types, e.g., <code>{"img": "/root/data1"}</code>.</td>
</tr>
<tr>
<td><code>list</code></td>
<td>Supports passing a list, where the list elements need to be the above data types, such as <code>[numpy.ndarray, numpy.ndarray], ["/root/data/img1.jpg", "/root/data/img2.jpg"], ["/root/data1", "/root/data2"], [{"img": "/root/data1"}, {"img": "/root/data2/img.jpg"}]</code>.</td>
</tr>
</tbody>
</table>
(3) Obtain the prediction results by calling the `predict` method: The `predict` method is a `generator`, so prediction results need to be obtained by calling it. The `predict` method predicts data in batches, so the prediction results are in the form of a list representing a set of prediction results.

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

For example, if your configuration file is saved at `./my_path/semantic_segmentation.yaml`, you only need to execute:

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/semantic_segmentation.yaml")
output = pipeline.predict("makassaridn-road_demo.png")
for res in output:
    res.print()  # Print the structured output of prediction
    res.save_to_img("./output/")  # Save the visualized image of the result
    res.save_to_json("./output/")  # Save the structured output of prediction
```

## 3. Development Integration/Deployment
If the pipeline meets your requirements for inference speed and accuracy, you can proceed with development integration/deployment.

If you need to directly apply the pipeline in your Python project, refer to the example code in [2.2.2 Python Script Integration](#222-python-script-integration).

Additionally, PaddleX provides three other deployment methods, detailed as follows:

🚀 <b>High-Performance Inference</b>: In actual production environments, many applications have stringent standards for the performance metrics of deployment strategies (especially response speed) to ensure efficient system operation and smooth user experience. To this end, PaddleX provides high-performance inference plugins that aim to deeply optimize model inference and pre/post-processing for significant end-to-end speedups. For detailed high-performance inference procedures, refer to the [PaddleX High-Performance Inference Guide](../../../pipeline_deploy/high_performance_inference.en.md).

☁️ <b>Service-Oriented Deployment</b>: Service-oriented deployment is a common deployment form in actual production environments. By encapsulating inference functions as services, clients can access these services through network requests to obtain inference results. PaddleX supports users in achieving low-cost service-oriented deployment of pipelines. For detailed service-oriented deployment procedures, refer to the [PaddleX Service-Oriented Deployment Guide](../../../pipeline_deploy/service_deploy.en.md).

Below are the API references and multi-language service invocation examples:

<details>
<summary>API Reference</summary>

For all operations provided by the service:

- Both the response body and the request body for POST requests are JSON data (JSON objects).
- When the request is processed successfully, the response status code is `200`, and the response body properties are as follows:

    | Name | Type | Description |
    |------|------|-------------|
    |`errorCode`|`integer`|Error code. Fixed as `0`.|
    |`errorMsg`|`string`|Error description. Fixed as `"Success"`.|

    The response body may also have a `result` property of type `object`, which stores the operation result information.

- When the request is not processed successfully, the response body properties are as follows:

    | Name | Type | Description |
    |------|------|-------------|
    |`errorCode`|`integer`|Error code. Same as the response status code.|
    |`errorMsg`|`string`|Error description.|

Operations provided by the service are as follows:

- <b>`infer`</b>

    Performs semantic segmentation on an image.

    `POST /semantic-segmentation`

    - The request body properties are as follows:

        | Name | Type | Description | Required |
        |------|------|-------------|----------|
        |`image`|`string`|The URL of an image file accessible by the service or the Base64 encoded result of the image file content.|Yes|

    - When the request is processed successfully, the `result` of the response body has the following properties:

        | Name | Type | Description |
        |------|------|-------------|
        |`labelMap`|`array`|Records the class label of each pixel in the image (arranged in row-major order).|
        |`size`|`array`|Image shape. The elements in the array are the height and width of the image, respectively.|
        |`image`|`string`|The semantic segmentation result image. The image is in JPEG format and encoded using Base64.|

        An example of `result` is as follows:

        ```json
        {
          "labelMap": [
            0,
            0,
            1,
            2
          ],
          "size": [
            2,
            2
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

API_URL = "http://localhost:8080/semantic-segmentation"
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

    auto response = client.Post("/semantic-segmentation", headers, body, "application/json");
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
        String API_URL = "http://localhost:8080/semantic-segmentation";
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
                JsonNode labelMap = result.get("labelMap");

                byte[] imageBytes = Base64.getDecoder().decode(base64Image);
                try (FileOutputStream fos = new FileOutputStream(outputImagePath)) {
                    fos.write(imageBytes);
                }
                System.out.println("Output image saved at " + outputImagePath);
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
    API_URL := "http://localhost:8080/semantic-segmentation"
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
            Labelmap []map[string]interface{} `json:"labelMap"`
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
    static readonly string API_URL = "http://localhost:8080/semantic-segmentation";
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
    }
}
```

</details>

<details>
<summary>Node.js</summary>

```js
const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/semantic-segmentation'
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

$API_URL = "http://localhost:8080/semantic-segmentation";
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
?>
```

</details>

</details>
<br/>

📱 <b>Edge Deployment</b>: Edge deployment is a method that places computing and data processing functions on user devices themselves, allowing devices to process data directly without relying on remote servers. PaddleX supports deploying models on edge devices such as Android. For detailed edge deployment procedures, refer to the [PaddleX Edge Deployment Guide](../../../pipeline_deploy/edge_deploy.md).
Choose the appropriate deployment method for your model pipeline based on your needs, and proceed with subsequent AI application integration.

## 4. Custom Development
If the default model weights provided by the general semantic segmentation pipeline do not meet your requirements for accuracy or speed in your specific scenario, you can try to further fine-tune the existing model using <b>your own domain-specific or application-specific data</b> to improve the recognition performance of the general semantic segmentation pipeline in your scenario.

### 4.1 Model Fine-tuning
Since the general semantic segmentation pipeline includes a semantic segmentation module, if the performance of the pipeline does not meet expectations, you need to refer to the [Customization](../../../module_usage/tutorials/cv_modules/semantic_segmentation.en.md#iv-custom-development) section in the [Semantic Segmentation Module Development Tutorial](../../../module_usage/tutorials/cv_modules/semantic_segmentation.en.md) (GitHub can directly link to headings) and use your private dataset to fine-tune the semantic segmentation model.

### 4.2 Model Application
After you complete fine-tuning training using your private dataset, you will obtain local model weight files.

If you need to use the fine-tuned model weights, simply modify the pipeline configuration file by replacing the local path of the fine-tuned model weights to the corresponding location in the pipeline configuration file:

```python
......
Pipeline:
  model: PP-LiteSeg-T  # Can be modified to the local path of the fine-tuned model
  device: "gpu"
  batch_size: 1
......
```
Then, refer to the command line method or Python script method in the local experience section to load the modified pipeline configuration file.

## Multi-hardware Support
PaddleX supports various mainstream hardware devices such as NVIDIA GPUs, Kunlun XPU, Ascend NPU, and Cambricon MLU. <b>Simply modify the `--device` parameter</b> to seamlessly switch between different hardware.

For example, if you use an NVIDIA GPU for semantic segmentation pipeline inference, the Python command is:

```bash
paddlex --pipeline semantic_segmentation --input makassaridn-road_demo.png --device gpu:0
``````
At this point, if you wish to switch the hardware to Ascend NPU, simply modify the `--device` flag in the Python command to `npu:0`:

```bash
paddlex --pipeline semantic_segmentation --input makassaridn-road_demo.png --device npu:0
```
If you want to use the General Semantic Segmentation Pipeline on a wider range of hardware, please refer to the [PaddleX Multi-Device Usage Guide](../../../other_devices_support/multi_devices_use_guide.en.md).
