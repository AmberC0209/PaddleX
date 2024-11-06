[简体中文](time_series_anomaly_detection.md) | English

# Time Series Anomaly Detection Pipeline Tutorial

## 1. Introduction to the General Time Series Anomaly Detection Pipeline
Time series anomaly detection is a technique for identifying abnormal patterns or behaviors in time series data. It is widely applied in fields such as network security, equipment monitoring, and financial fraud detection. By analyzing normal trends and patterns in historical data, it discovers events that significantly deviate from expected behaviors, such as sudden spikes in network traffic or unusual transaction activities. Time series anomaly detection enable automatic identification of anomalies in data. This technology provides real-time alerts for enterprises and organizations, helping them promptly address potential risks and issues. It plays a crucial role in ensuring system stability and security.

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/05.png">

<b>The General Time Series Anomaly Detection Pipeline includes a time series anomaly detection module. If you prioritize model accuracy, choose a model with higher precision. If you prioritize inference speed, select a model with faster inference. If you prioritize model storage size, choose a model with a smaller storage footprint.</b>

<details>
   <summary> 👉Model List Details</summary>

<table>
<thead>
<tr>
<th>Model Name</th>
<th>Precision</th>
<th>Recall</th>
<th>F1-Score</th>
<th>Model Storage Size (M)</th>
</tr>
</thead>
<tbody>
<tr>
<td>AutoEncoder_ad</td>
<td>99.36</td>
<td>84.36</td>
<td>91.25</td>
<td>52K</td>
</tr>
<tr>
<td>DLinear_ad</td>
<td>98.98</td>
<td>93.96</td>
<td>96.41</td>
<td>112K</td>
</tr>
<tr>
<td>Nonstationary_ad</td>
<td>98.55</td>
<td>88.95</td>
<td>93.51</td>
<td>1.8M</td>
</tr>
<tr>
<td>PatchTST_ad</td>
<td>98.78</td>
<td>90.70</td>
<td>94.57</td>
<td>320K</td>
</tr>
<tr>
<td>TimesNet_ad</td>
<td>98.37</td>
<td>94.80</td>
<td>96.56</td>
<td>1.3M</td>
</tr>
</tbody>
</table>
<b>Note: The above precision metrics are measured on the </b>[PSM](https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ts_anomaly_examples.tar)<b> dataset. All model GPU inference times are based on an NVIDIA Tesla T4 machine with FP32 precision. CPU inference speeds are based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>

</details>

## 2. Quick Start
The pre-trained model pipelines provided by PaddleX allow for quick experience of their effects. You can experience the effects of the General Time Series Anomaly Detection Pipeline online or locally using command line or Python.

### 2.1 Online Experience
You can [experience online](https://aistudio.baidu.com/community/app/105706/webUI?source=appCenter) the effects of the General Time Series Anomaly Detection Pipeline using the official demo for recognition, for example:

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/06.png">

If you are satisfied with the pipeline's performance, you can directly integrate and deploy it. If not, you can also use your private data to <b>fine-tune the model within the pipeline online</b>.

<b>Note</b>: Due to the close relationship between time series data and scenarios, the official built-in models for online experience of time series tasks are only model solutions for a specific scenario and are not universal. They are not applicable to other scenarios. Therefore, the experience mode does not support using arbitrary files to experience the effects of the official model solutions. However, after training a model for your own scenario data, you can select your trained model solution and use data from the corresponding scenario for online experience.

### 2.2 Local Experience
Before using the General Time Series Anomaly Detection Pipeline locally, ensure you have installed the PaddleX wheel package following the [PaddleX Local Installation Tutorial](../../../installation/installation.en.md).

#### 2.2.1 Command Line Experience
A single command is all you need to quickly experience the effects of the time series anomaly detection pipeline:

Experience the image anomaly detection pipeline with a single command，Use the [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv), and replace `--input` with the local path to perform prediction.

```bash
paddlex --pipeline ts_ad --input ts_ad.csv --device gpu:0
```
Parameter Explanation:

```
--pipeline: The name of the pipeline, here it's the image anomaly detection pipeline.
--input: The local path or URL of the input image to be processed.
--device: The GPU index to use (e.g., gpu:0 for the first GPU, gpu:1,2 for the second and third GPUs). CPU can also be selected (--device cpu).
```

When executing the above command, the default image anomaly detection pipeline configuration file is loaded. If you need to customize the configuration file, you can run the following command to obtain it:

<details>
   <summary> 👉Click to expand</summary>

```bash
paddlex --get_pipeline_config ts_ad --save_path ./my_path
```

After obtaining the pipeline configuration file, you can replace `--pipeline` with the configuration file save path to make the configuration file take effect. For example, if the configuration file save path is `./ts_ad.yaml`, simply execute:

```bash
paddlex --pipeline ./ts_ad.yaml --input ts_ad.csv --device gpu:0
```

Here, parameters such as `--model` and `--device` do not need to be specified, as they will use the parameters in the configuration file. If parameters are still specified, the specified parameters will take precedence.

</details>

After running, the result obtained is:

```json
{'input_path': 'ts_ad.csv', 'anomaly':            label
timestamp
220226         0
220227         0
220228         0
220229         0
220230         0
...          ...
220317         1
220318         1
220319         1
220320         1
220321         0

[96 rows x 1 columns]}
```

#### 2.2.2 Python Script Integration
A few lines of code can complete the rapid inference of the pipeline. Taking the general time series anomaly detection pipeline as an example:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="ts_ad")

output = pipeline.predict("ts_ad.csv")
for res in output:
    res.print()  # Print the structured output of the prediction
    res.save_to_csv("./output/")  # Save the result in CSV format
```

The result obtained is the same as that of the command line method.

In the above Python script, the following steps are executed:

（1）Instantiate the  production line object using `create_pipeline`: Specific parameter descriptions are as follows:

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
<td>The name of the production line or the path to the production line configuration file. If it is the name of the production line, it must be supported by PaddleX.</td>
<td><code>str</code></td>
<td>None</td>
</tr>
<tr>
<td><code>device</code></td>
<td>The device for production line model inference. Supports: "gpu", "cpu".</td>
<td><code>str</code></td>
<td><code>gpu</code></td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>Whether to enable high-performance inference, only available if the production line supports it.</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>
（2）Invoke the `predict` method of the  production line object for inference prediction: The `predict` method parameter is `x`, which is used to input data to be predicted, supporting multiple input methods, as shown in the following examples:

<table>
<thead>
<tr>
<th>Parameter Type</th>
<th>Parameter Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python Var</td>
<td>Supports directly passing in Python variables, such as numpy.ndarray representing image data.</td>
</tr>
<tr>
<td>str</td>
<td>Supports passing in the path of the file to be predicted, such as the local path of an image file: <code>/root/data/img.jpg</code>.</td>
</tr>
<tr>
<td>str</td>
<td>Supports passing in the URL of the file to be predicted, such as the network URL of an image file: <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv">Example</a>.</td>
</tr>
<tr>
<td>str</td>
<td>Supports passing in a local directory, which should contain files to be predicted, such as the local path: <code>/root/data/</code>.</td>
</tr>
<tr>
<td>dict</td>
<td>Supports passing in a dictionary type, where the key needs to correspond to a specific task, such as "img" for image classification tasks. The value of the dictionary supports the above types of data, for example: <code>{"img": "/root/data1"}</code>.</td>
</tr>
<tr>
<td>list</td>
<td>Supports passing in a list, where the list elements need to be of the above types of data, such as <code>[numpy.ndarray, numpy.ndarray], ["/root/data/img1.jpg", "/root/data/img2.jpg"], ["/root/data1", "/root/data2"], [{"img": "/root/data1"}, {"img": "/root/data2/img.jpg"}]</code>.</td>
</tr>
</tbody>
</table>
（3）Obtain the prediction results by calling the `predict` method: The `predict` method is a `generator`, so prediction results need to be obtained through iteration. The `predict` method predicts data in batches, so the prediction results are in the form of a list.

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
<td>save_to_csv</td>
<td>Saves results as a csv file</td>
<td><code>- save_path</code>: str, the path to save the file, when it's a directory, the saved file name is consistent with the input file type;<br><code>- indent</code>: int, json formatting setting, default is 4;<br><code>- ensure_ascii</code>: bool, json formatting setting, default is False;</td>
</tr>
<tr>
<td>save_to_xlsx</td>
<td>Saves results as table file</td>
<td><code>- save_path</code>: str, the path to save the file, when it's a directory, the saved file name is consistent with the input file type;</td>
</tr>
</tbody>
</table>
If you have a configuration file, you can customize the configurations of the image anomaly detection pipeline by simply modifying the `pipeline` parameter in the `create_pipeline` method to the path of the pipeline configuration file.

For example, if your configuration file is saved at `./my_path/ts_ad.yaml`, you only need to execute:

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/ts_ad.yaml")
output = pipeline.predict("ts_ad.csv")
for res in output:
    res.print()  # Print the structured output of prediction
    res.save_to_csv("./output/")  # Save results in CSV format
```

## 3. Development Integration/Deployment
If the pipeline meets your requirements for inference speed and accuracy in production, you can proceed with development integration/deployment.

If you need to directly apply the pipeline in your Python project, refer to the example code in [2.2.2 Python Script Integration](#222-python-script-integration).

Additionally, PaddleX provides three other deployment methods, detailed as follows:

🚀 <b>High-Performance Inference</b>: In actual production environments, many applications have stringent standards for the performance metrics of deployment strategies (especially response speed) to ensure efficient system operation and smooth user experience. To this end, PaddleX provides high-performance inference plugins aimed at deeply optimizing model inference and pre/post-processing for significant end-to-end speedups. For detailed high-performance inference procedures, refer to the [PaddleX High-Performance Inference Guide](../../../pipeline_deploy/high_performance_inference.en.md).

☁️ <b>Service-Oriented Deployment</b>: Service-oriented deployment is a common deployment form in actual production environments. By encapsulating inference functions as services, clients can access these services through network requests to obtain inference results. PaddleX enables users to achieve low-cost service-oriented deployment of pipelines. For detailed service-oriented deployment procedures, refer to the [PaddleX Service-Oriented Deployment Guide](../../../pipeline_deploy/service_deploy.en.md).

Below are the API references and multi-language service invocation examples:

<details>
<summary>API Reference</summary>

For all operations provided by the service:

- Both the response body and the request body for POST requests are JSON data (JSON objects).
- When the request is processed successfully, the response status code is `200`, and the properties of the response body are as follows:

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
<td>Error description. Fixed as <code>"Success"</code>.</td>
</tr>
</tbody>
</table>
    The response body may also have a `result` property of type `object`, which stores the operation result information.

- When the request is not processed successfully, the properties of the response body are as follows:

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
<td>Error description.</td>
</tr>
</tbody>
</table>
Operations provided by the service:

- <b>`infer`</b>

    Performs time-series anomaly detection.

    `POST /time-series-anomaly-detection`

    - Attributes of the request body:

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
<td><code>csv</code></td>
<td><code>string</code></td>
<td>The URL of a CSV file accessible by the service or the Base64 encoded result of the CSV file content. The CSV file must be encoded in UTF-8.</td>
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
<td><code>csv</code></td>
<td><code>string</code></td>
<td>Time-series anomaly detection results in CSV format. Encoded in UTF-8+Base64.</td>
</tr>
</tbody>
</table>
        An example of `result` is as follows:

        ```json
        {
          "csv": "xxxxxx"
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

API_URL = "http://localhost:8080/time-series-anomaly-detection"
csv_path = "./test.csv"
output_csv_path = "./out.csv"

with open(csv_path, "rb") as file:
    csv_bytes = file.read()
    csv_data = base64.b64encode(csv_bytes).decode("ascii")

payload = {"csv": csv_data}

response = requests.post(API_URL, json=payload)

assert response.status_code == 200
result = response.json()["result"]
with open(output_csv_path, "wb") as f:
    f.write(base64.b64decode(result["csv"]))
print(f"Output time-series data saved at  {output_csv_path}")
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
    const std::string csvPath = "./test.csv";
    const std::string outputCsvPath = "./out.csv";

    httplib::Headers headers = {
        {"Content-Type", "application/json"}
    };

    std::ifstream file(csvPath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> buffer(size);
    if (!file.read(buffer.data(), size)) {
        std::cerr << "Error reading file." << std::endl;
        return 1;
    }
    std::string bufferStr(reinterpret_cast<const char*>(buffer.data()), buffer.size());
    std::string encodedCsv = base64::to_base64(bufferStr);

    nlohmann::json jsonObj;
    jsonObj["csv"] = encodedCsv;
    std::string body = jsonObj.dump();

    auto response = client.Post("/time-series-anomaly-detection", headers, body, "application/json");
    if (response && response->status == 200) {
        nlohmann::json jsonResponse = nlohmann::json::parse(response->body);
        auto result = jsonResponse["result"];

        encodedCsv = result["csv"];
        decodedString = base64::from_base64(encodedCsv);
        std::vector<unsigned char> decodedCsv(decodedString.begin(), decodedString.end());
        std::ofstream outputCsv(outputCsvPath, std::ios::binary | std::ios::out);
        if (outputCsv.is_open()) {
            outputCsv.write(reinterpret_cast<char*>(decodedCsv.data()), decodedCsv.size());
            outputCsv.close();
            std::cout << "Output time-series data saved at " << outputCsvPath << std::endl;
        } else {
            std::cerr << "Unable to open file for writing: " << outputCsvPath << std::endl;
        }
    } else {
        std::cout << "Failed to send HTTP request." << std::endl;
        std::cout << response->body << std::endl;
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
        String API_URL = "http://localhost:8080/time-series-anomaly-detection";
        String csvPath = "./test.csv";
        String outputCsvPath = "./out.csv";

        File file = new File(csvPath);
        byte[] fileContent = java.nio.file.Files.readAllBytes(file.toPath());
        String csvData = Base64.getEncoder().encodeToString(fileContent);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode params = objectMapper.createObjectNode();
        params.put("csv", csvData);

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

                String base64Csv = result.get("csv").asText();
                byte[] csvBytes = Base64.getDecoder().decode(base64Csv);
                try (FileOutputStream fos = new FileOutputStream(outputCsvPath)) {
                    fos.write(csvBytes);
                }
                System.out.println("Output time-series data saved at " + outputCsvPath);
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
    API_URL := "http://localhost:8080/time-series-anomaly-detection"
    csvPath := "./test.csv";
    outputCsvPath := "./out.csv";

    csvBytes, err := ioutil.ReadFile(csvPath)
    if err != nil {
        fmt.Println("Error reading csv file:", err)
        return
    }
    csvData := base64.StdEncoding.EncodeToString(csvBytes)

    payload := map[string]string{"csv": csvData}
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
            Csv string `json:"csv"`
        } `json:"result"`
    }
    var respData Response
    err = json.Unmarshal([]byte(string(body)), &respData)
    if err != nil {
        fmt.Println("Error unmarshaling response body:", err)
        return
    }

    outputCsvData, err := base64.StdEncoding.DecodeString(respData.Result.Csv)
    if err != nil {
        fmt.Println("Error decoding base64 csv data:", err)
        return
    }
    err = ioutil.WriteFile(outputCsvPath, outputCsvData, 0644)
    if err != nil {
        fmt.Println("Error writing csv to file:", err)
        return
    }
    fmt.Printf("Output time-series data saved at %s.csv", outputCsvPath)
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
    static readonly string API_URL = "http://localhost:8080/time-series-anomaly-detection";
    static readonly string csvPath = "./test.csv";
    static readonly string outputCsvPath = "./out.csv";

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();

        byte[] csvBytes = File.ReadAllBytes(csvPath);
        string csvData = Convert.ToBase64String(csvBytes);

        var payload = new JObject{ { "csv", csvData } };
        var content = new StringContent(payload.ToString(), Encoding.UTF8, "application/json");

        HttpResponseMessage response = await httpClient.PostAsync(API_URL, content);
        response.EnsureSuccessStatusCode();

        string responseBody = await response.Content.ReadAsStringAsync();
        JObject jsonResponse = JObject.Parse(responseBody);

        string base64Csv = jsonResponse["result"]["csv"].ToString();
        byte[] outputCsvBytes = Convert.FromBase64String(base64Csv);
        File.WriteAllBytes(outputCsvPath, outputCsvBytes);
        Console.WriteLine($"Output time-series data saved at {outputCsvPath}");
    }
}
```

</details>

<details>
<summary>Node.js</summary>

```js
const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/time-series-anomaly-detection'
const csvPath = "./test.csv";
const outputCsvPath = "./out.csv";

let config = {
   method: 'POST',
   maxBodyLength: Infinity,
   url: API_URL,
   data: JSON.stringify({
    'csv': encodeFileToBase64(csvPath)
  })
};

function encodeFileToBase64(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString('base64');
}

axios.request(config)
.then((response) => {
    const result = response.data["result"];

    const csvBuffer = Buffer.from(result["csv"], 'base64');
    fs.writeFile(outputCsvPath, csvBuffer, (err) => {
      if (err) throw err;
      console.log(`Output time-series data saved at ${outputCsvPath}`);
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

$API_URL = "http://localhost:8080/time-series-anomaly-detection";
$csv_path = "./test.csv";
$output_csv_path = "./out.csv";

$csv_data = base64_encode(file_get_contents($csv_path));
$payload = array("csv" => $csv_data);

$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true)["result"];

file_put_contents($output_csv_path, base64_decode($result["csv"]));
echo "Output time-series data saved at " . $output_csv_path . "\n";

?>
```

</details>
</details>
<br/>

📱 <b>Edge Deployment</b>: Edge deployment is a method that places computing and data processing capabilities on user devices themselves, allowing devices to process data directly without relying on remote servers. PaddleX supports deploying models on edge devices such as Android. For detailed edge deployment procedures, refer to the [PaddleX Edge Deployment Guide](../../../pipeline_deploy/edge_deploy.md).
Choose the appropriate deployment method for your model pipeline based on your needs, and proceed with subsequent AI application integration.

## 4. Custom Development
If the default model weights provided by the General Time Series Anomaly Detection Pipeline do not meet your requirements for accuracy or speed in your specific scenario, you can try to further fine-tune the existing model using <b>your own domain-specific or application-specific data</b> to improve the recognition performance of the pipeline in your scenario.

### 4.1 Model Fine-tuning
Since the General Time Series Anomaly Detection Pipeline includes a time series anomaly detection module, if the performance of the pipeline does not meet expectations, you need to refer to the [Customization](../../../module_usage/tutorials/time_series_modules/time_series_anomaly_detection.en.md#iv-custom-development) section in the [Time Series Modules Development Tutorial](../../../module_usage/tutorials/time_series_modules/time_series_anomaly_detection.en.md) to fine-tune the time series anomaly detection model using your private dataset.

### 4.2 Model Application
After fine-tuning with your private dataset, you will obtain local model weights files.

To use the fine-tuned model weights, simply modify the pipeline configuration file by replacing the local path of the fine-tuned model weights to the corresponding location in the pipeline configuration file:

```python
......
Pipeline:
  model: DLinear_ad  # Can be modified to the local path of the fine-tuned model
  batch_size: 1
  device: "gpu:0"
......
```

Then, refer to the command line method or Python script method in the local experience section to load the modified pipeline configuration file.

## 5. Multi-hardware Support
PaddleX supports various mainstream hardware devices such as NVIDIA GPUs, Kunlun XPU, Ascend NPU, and Cambricon MLU. <b>Simply modify the `--device` parameter</b> to seamlessly switch between different hardware.

For example, if you use an NVIDIA GPU for inference of the time series anomaly detection pipeline, the Python command is:

```bash
paddlex --pipeline ts_ad --input ts_ad.csv --device gpu:0
``````
At this point, if you wish to switch the hardware to Ascend NPU, simply modify the `--device` in the Python command to `npu:0`:

```bash
paddlex --pipeline ts_ad --input ts_ad.csv --device npu:0
```
If you want to use the General Time-Series Anomaly Detection Pipeline on more diverse hardware, please refer to the [PaddleX Multi-Device Usage Guide](../../../other_devices_support/multi_devices_use_guide.en.md).
