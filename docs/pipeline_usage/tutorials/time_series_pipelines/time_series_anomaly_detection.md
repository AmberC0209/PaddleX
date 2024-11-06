简体中文 | [English](time_series_anomaly_detection.en.md)

# 时序异常检测产线使用教程

## 1. 通用时序异常检测产线介绍
时序异常检测是一种识别时间序列数据中异常模式或行为的技术，广泛应用于网络安全、设备监控和金融欺诈检测等领域。它通过分析历史数据中的正常趋势和规律，来发现与预期行为显著不同的事件，例如突然增加的网络流量或异常的交易活动。时序异常检测能够自动识别数据中的异常点，为企业和组织提供实时警报，帮助及时应对潜在风险和问题。这项技术在保障系统稳定性和安全性方面发挥着重要作用。

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/05.png">


<b>通用</b><b>时序异常检测</b><b>产线中包含了</b><b>时序异常检测</b><b>模块，如您更考虑模型精度，请选择精度较高的模型，如您更考虑模型推理速度，请选择推理速度较快的模型，如您更考虑模型存储大小，请选择存储大小较小的模型</b>。



<details><summary> 👉模型列表详情</summary>

<table>
<thead>
<tr>
<th>模型名称</th>
<th>precison</th>
<th>recall</th>
<th>f1_score</th>
<th>模型存储大小（M)</th>
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

<p><b>注：以上精度指标测量自 </b><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ts_anomaly_examples.tar">PSM</a><b> 数据集。以上所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。</b></p></details>


## 2. 快速开始
PaddleX 所提供的预训练的模型产线均可以快速体验效果，你可以在线体验通用时序异常检测产线的效果，也可以在本地使用命令行或 Python 体验通用时序异常检测产线的效果。

### 2.1 在线体验
您可以[在线体验](https://aistudio.baidu.com/community/app/105706/webUI?source=appCenter)通用时序异常检测产线的效果，用官方提供的 demo 进行识别，例如：

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/06.png">

如果您对产线运行的效果满意，可以直接对产线进行集成部署，如果不满意，您也可以利用私有数据<b>对产线中的模型进行在线微调</b>。

<b>注</b>：由于时序数据和场景紧密相关，时序任务的在线体验官方内置模型仅是在一个特定场景下的模型方案，并非通用方案，不适用其他场景，因此体验方式不支持使用任意的文件来体验官方模型方案效果。但是，在完成自己场景数据下的模型训练之后，可以选择自己训练的模型方案，并使用对应场景的数据进行在线体验。

### 2.2 本地体验
在本地使用通用时序异常检测产线前，请确保您已经按照[PaddleX本地安装教程](../../../installation/installation.md)完成了PaddleX的wheel包安装。

#### 2.2.1 命令行方式体验
一行命令即可快速体验时序异常检测产线效果，使用 [测试文件](https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv)，并将 `--input` 替换为本地路径，进行预测

```bash
paddlex --pipeline ts_ad --input ts_ad.csv --device gpu:0
```
参数说明：

```
--pipeline：产线名称，此处为时序异常检测产线
--input：待处理的输入序列的本地路径或URL
--device 使用的GPU序号（例如gpu:0表示使用第0块GPU，gpu:1,2表示使用第1、2块GPU），也可选择使用CPU（--device cpu）
```

在执行上述 Python 脚本时，加载的是默认的时序异常检测产线配置文件，若您需要自定义配置文件，可执行如下命令获取：

<details><summary> 👉点击展开</summary>

<pre><code>paddlex --get_pipeline_config ts_ad
</code></pre>
<p>执行后，时序异常检测产线配置文件将被保存在当前路径。若您希望自定义保存位置，可执行如下命令（假设自定义保存位置为 <code>./my_path</code> ）：</p>
<pre><code>paddlex --get_pipeline_config ts_ad --save_path ./my_path
</code></pre>
<p>获取产线配置文件后，可将<code>--pipeline</code> 替换为配置文件保存路径，即可使配置文件生效。例如，若配置文件保存路径为 <code>./ts_ad.yaml</code>，只需执行：</p>
<pre><code class="language-bash">paddlex --pipeline ./ts_ad.yaml --input ts_ad.cs --device gpu:0
</code></pre>
<p>其中，<code>--model</code>、<code>--device</code> 等参数无需指定，将使用配置文件中的参数。若依然指定了参数，将以指定的参数为准。</p></details>

运行后，得到的结果为：

```
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

#### 2.2.2 Python脚本方式集成
几行代码即可完成产线的快速推理，以通用时序异常检测产线为例：

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="ts_ad")

output = pipeline.predict("ts_ad.cs")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_csv("./output/") ## 保存csv格式结果
```
得到的结果与命令行方式相同。

在上述 Python 脚本中，执行了如下几个步骤：

（1）实例化 `create_pipeline` 实例化产线对象：具体参数说明如下：

<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
<th>参数类型</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pipeline</code></td>
<td>产线名称或是产线配置文件路径。如为产线名称，则必须为 PaddleX 所支持的产线。</td>
<td><code>str</code></td>
<td>无</td>
</tr>
<tr>
<td><code>device</code></td>
<td>产线模型推理设备。支持：“gpu”，“cpu”。</td>
<td><code>str</code></td>
<td><code>gpu</code></td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>是否启用高性能推理，仅当该产线支持高性能推理时可用。</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>

（2）调用产线对象的 `predict` 方法进行推理预测：`predict` 方法参数为`x`，用于输入待预测数据，支持多种输入方式，具体示例如下：

<table>
<thead>
<tr>
<th>参数类型</th>
<th>参数说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python Var</td>
<td>支持直接传入Python变量，如numpy.ndarray表示的图像数据。</td>
</tr>
<tr>
<td>str</td>
<td>支持传入待预测数据文件路径，如图像文件的本地路径：<code>/root/data/img.jpg</code>。</td>
</tr>
<tr>
<td>str</td>
<td>支持传入待预测数据文件URL，如图像文件的网络URL：<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv">示例</a>。</td>
</tr>
<tr>
<td>str</td>
<td>支持传入本地目录，该目录下需包含待预测数据文件，如本地路径：<code>/root/data/</code>。</td>
</tr>
<tr>
<td>dict</td>
<td>支持传入字典类型，字典的key需与具体任务对应，如图像分类任务对应\"img\"，字典的val支持上述类型数据，例如：<code>{\"img\": \"/root/data1\"}</code>。</td>
</tr>
<tr>
<td>list</td>
<td>支持传入列表，列表元素需为上述类型数据，如<code>[numpy.ndarray, numpy.ndarray]，[\"/root/data/img1.jpg\", \"/root/data/img2.jpg\"]</code>，<code>[\"/root/data1\", \"/root/data2\"]</code>，<code>[{\"img\": \"/root/data1\"}, {\"img\": \"/root/data2/img.jpg\"}]</code>。</td>
</tr>
</tbody>
</table>

（3）调用`predict`方法获取预测结果：`predict` 方法为`generator`，因此需要通过调用获得预测结果，`predict`方法以batch为单位对数据进行预测，因此预测结果为list形式表示的一组预测结果。

（4）对预测结果进行处理：每个样本的预测结果均为`dict`类型，且支持打印，或保存为文件，支持保存的类型与具体产线相关，如：

<table>
<thead>
<tr>
<th>方法</th>
<th>说明</th>
<th>方法参数</th>
</tr>
</thead>
<tbody>
<tr>
<td>save_to_csv</td>
<td>将结果保存为csv格式的文件</td>
<td><code>- save_path</code>：str类型，保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致；</td>
</tr>
<tr>
<td>save_to_xlsx</td>
<td>将结果保存为表格格式的文件</td>
<td><code>- save_path</code>：str类型，保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致；</td>
</tr>
</tbody>
</table>

若您获取了配置文件，即可对时序异常检测产线各项配置进行自定义，只需要修改 `create_pipeline` 方法中的 `pipeline` 参数值为产线配置文件路径即可。

例如，若您的配置文件保存在 `./my_path/ts_ad.yaml` ，则只需执行：

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/ts_ad.yaml")
output = pipeline.predict("ts_ad.cs")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_csv("./output/") ## 保存csv格式结果
```

## 3. 开发集成/部署
如果产线可以达到您对产线推理速度和精度的要求，您可以直接进行开发集成/部署。

若您需要将产线直接应用在您的Python项目中，可以参考 [2.2.2 Python脚本方式](#222-python脚本方式集成)中的示例代码。

此外，PaddleX 也提供了其他三种部署方式，详细说明如下：

🚀 <b>高性能推理</b>：在实际生产环境中，许多应用对部署策略的性能指标（尤其是响应速度）有着较严苛的标准，以确保系统的高效运行与用户体验的流畅性。为此，PaddleX 提供高性能推理插件，旨在对模型推理及前后处理进行深度性能优化，实现端到端流程的显著提速，详细的高性能推理流程请参考[PaddleX高性能推理指南](../../../pipeline_deploy/high_performance_inference.md)。

☁️ <b>服务化部署</b>：服务化部署是实际生产环境中常见的一种部署形式。通过将推理功能封装为服务，客户端可以通过网络请求来访问这些服务，以获取推理结果。PaddleX 支持用户以低成本实现产线的服务化部署，详细的服务化部署流程请参考[PaddleX服务化部署指南](../../../pipeline_deploy/service_deploy.md)。

下面是API参考和多语言服务调用示例：

<details><summary>API参考</summary>

<p>对于服务提供的所有操作：</p>
<ul>
<li>响应体以及POST请求的请求体均为JSON数据（JSON对象）。</li>
<li>当请求处理成功时，响应状态码为<code>200</code>，响应体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>错误码。固定为<code>0</code>。</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>错误说明。固定为<code>"Success"</code>。</td>
</tr>
</tbody>
</table>

<p>响应体还可能有<code>result</code>属性，类型为<code>object</code>，其中存储操作结果信息。</p>
<ul>
<li>当请求处理未成功时，响应体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>错误码。与响应状态码相同。</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>错误说明。</td>
</tr>
</tbody>
</table>

<p>服务提供的操作如下：</p>
<ul>
<li><b><code>infer</code></b></li>
</ul>
<p>进行时序异常检测。</p>
<p><code>POST /time-series-anomaly-detection</code></p>
<ul>
<li>请求体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
<th>是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>csv</code></td>
<td><code>string</code></td>
<td>服务可访问的CSV文件的URL或CSV文件内容的Base64编码结果。CSV文件需要使用UTF-8编码。</td>
<td>是</td>
</tr>
</tbody>
</table>

<ul>
<li>请求处理成功时，响应体的<code>result</code>具有如下属性：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>csv</code></td>
<td><code>string</code></td>
<td>CSV格式的时序异常检测结果。使用UTF-8+Base64编码。</td>
</tr>
</tbody>
</table>

<p><code>result</code>示例如下：</p>
<pre><code class="language-json">{
&quot;csv&quot;: &quot;xxxxxx&quot;
}
</code></pre></details>

<details><summary>多语言调用服务示例</summary>

<details>
<summary>Python</summary>


<pre><code class="language-python">import base64
import requests

API_URL = &quot;http://localhost:8080/time-series-anomaly-detection&quot; # 服务URL
csv_path = &quot;./test.csv&quot;
output_csv_path = &quot;./out.csv&quot;

# 对本地图像进行Base64编码
with open(csv_path, &quot;rb&quot;) as file:
    csv_bytes = file.read()
    csv_data = base64.b64encode(csv_bytes).decode(&quot;ascii&quot;)

payload = {&quot;csv&quot;: csv_data}

# 调用API
response = requests.post(API_URL, json=payload)

# 处理接口返回数据
assert response.status_code == 200
result = response.json()[&quot;result&quot;]
with open(output_csv_path, &quot;wb&quot;) as f:
    f.write(base64.b64decode(result[&quot;csv&quot;]))
print(f&quot;Output time-series data saved at  {output_csv_path}&quot;)
</code></pre></details>

<details><summary>C++</summary>

<pre><code class="language-cpp">#include &lt;iostream&gt;
#include &quot;cpp-httplib/httplib.h&quot; // https://github.com/Huiyicc/cpp-httplib
#include &quot;nlohmann/json.hpp&quot; // https://github.com/nlohmann/json
#include &quot;base64.hpp&quot; // https://github.com/tobiaslocker/base64

int main() {
    httplib::Client client(&quot;localhost:8080&quot;);
    const std::string csvPath = &quot;./test.csv&quot;;
    const std::string outputCsvPath = &quot;./out.csv&quot;;

    httplib::Headers headers = {
        {&quot;Content-Type&quot;, &quot;application/json&quot;}
    };

    // 进行Base64编码
    std::ifstream file(csvPath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector&lt;char&gt; buffer(size);
    if (!file.read(buffer.data(), size)) {
        std::cerr &lt;&lt; &quot;Error reading file.&quot; &lt;&lt; std::endl;
        return 1;
    }
    std::string bufferStr(reinterpret_cast&lt;const char*&gt;(buffer.data()), buffer.size());
    std::string encodedCsv = base64::to_base64(bufferStr);

    nlohmann::json jsonObj;
    jsonObj[&quot;csv&quot;] = encodedCsv;
    std::string body = jsonObj.dump();

    // 调用API
    auto response = client.Post(&quot;/time-series-anomaly-detection&quot;, headers, body, &quot;application/json&quot;);
    // 处理接口返回数据
    if (response &amp;&amp; response-&gt;status == 200) {
        nlohmann::json jsonResponse = nlohmann::json::parse(response-&gt;body);
        auto result = jsonResponse[&quot;result&quot;];

        // 保存数据
        encodedCsv = result[&quot;csv&quot;];
        decodedString = base64::from_base64(encodedCsv);
        std::vector&lt;unsigned char&gt; decodedCsv(decodedString.begin(), decodedString.end());
        std::ofstream outputCsv(outputCsvPath, std::ios::binary | std::ios::out);
        if (outputCsv.is_open()) {
            outputCsv.write(reinterpret_cast&lt;char*&gt;(decodedCsv.data()), decodedCsv.size());
            outputCsv.close();
            std::cout &lt;&lt; &quot;Output time-series data saved at &quot; &lt;&lt; outputCsvPath &lt;&lt; std::endl;
        } else {
            std::cerr &lt;&lt; &quot;Unable to open file for writing: &quot; &lt;&lt; outputCsvPath &lt;&lt; std::endl;
        }
    } else {
        std::cout &lt;&lt; &quot;Failed to send HTTP request.&quot; &lt;&lt; std::endl;
        std::cout &lt;&lt; response-&gt;body &lt;&lt; std::endl;
        return 1;
    }

    return 0;
}
</code></pre></details>

<details><summary>Java</summary>

<pre><code class="language-java">import okhttp3.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws IOException {
        String API_URL = &quot;http://localhost:8080/time-series-anomaly-detection&quot;;
        String csvPath = &quot;./test.csv&quot;;
        String outputCsvPath = &quot;./out.csv&quot;;

        // 对本地csv进行Base64编码
        File file = new File(csvPath);
        byte[] fileContent = java.nio.file.Files.readAllBytes(file.toPath());
        String csvData = Base64.getEncoder().encodeToString(fileContent);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode params = objectMapper.createObjectNode();
        params.put(&quot;csv&quot;, csvData);

        // 创建 OkHttpClient 实例
        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.Companion.get(&quot;application/json; charset=utf-8&quot;);
        RequestBody body = RequestBody.Companion.create(params.toString(), JSON);
        Request request = new Request.Builder()
                .url(API_URL)
                .post(body)
                .build();

        // 调用API并处理接口返回数据
        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                JsonNode resultNode = objectMapper.readTree(responseBody);
                JsonNode result = resultNode.get(&quot;result&quot;);

                // 保存返回的数据
                String base64Csv = result.get(&quot;csv&quot;).asText();
                byte[] csvBytes = Base64.getDecoder().decode(base64Csv);
                try (FileOutputStream fos = new FileOutputStream(outputCsvPath)) {
                    fos.write(csvBytes);
                }
                System.out.println(&quot;Output time-series data saved at &quot; + outputCsvPath);
            } else {
                System.err.println(&quot;Request failed with code: &quot; + response.code());
            }
        }
    }
}
</code></pre></details>

<details><summary>Go</summary>

<pre><code class="language-go">package main

import (
    &quot;bytes&quot;
    &quot;encoding/base64&quot;
    &quot;encoding/json&quot;
    &quot;fmt&quot;
    &quot;io/ioutil&quot;
    &quot;net/http&quot;
)

func main() {
    API_URL := &quot;http://localhost:8080/time-series-anomaly-detection&quot;
    csvPath := &quot;./test.csv&quot;;
    outputCsvPath := &quot;./out.csv&quot;;

    // 读取csv文件并进行Base64编码
    csvBytes, err := ioutil.ReadFile(csvPath)
    if err != nil {
        fmt.Println(&quot;Error reading csv file:&quot;, err)
        return
    }
    csvData := base64.StdEncoding.EncodeToString(csvBytes)

    payload := map[string]string{&quot;csv&quot;: csvData} // Base64编码的文件内容
    payloadBytes, err := json.Marshal(payload)
    if err != nil {
        fmt.Println(&quot;Error marshaling payload:&quot;, err)
        return
    }

    // 调用API
    client := &amp;http.Client{}
    req, err := http.NewRequest(&quot;POST&quot;, API_URL, bytes.NewBuffer(payloadBytes))
    if err != nil {
        fmt.Println(&quot;Error creating request:&quot;, err)
        return
    }

    res, err := client.Do(req)
    if err != nil {
        fmt.Println(&quot;Error sending request:&quot;, err)
        return
    }
    defer res.Body.Close()

    // 处理返回数据
    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println(&quot;Error reading response body:&quot;, err)
        return
    }
    type Response struct {
        Result struct {
            Csv string `json:&quot;csv&quot;`
        } `json:&quot;result&quot;`
    }
    var respData Response
    err = json.Unmarshal([]byte(string(body)), &amp;respData)
    if err != nil {
        fmt.Println(&quot;Error unmarshaling response body:&quot;, err)
        return
    }

    // 将Base64编码的csv数据解码并保存为文件
    outputCsvData, err := base64.StdEncoding.DecodeString(respData.Result.Csv)
    if err != nil {
        fmt.Println(&quot;Error decoding base64 csv data:&quot;, err)
        return
    }
    err = ioutil.WriteFile(outputCsvPath, outputCsvData, 0644)
    if err != nil {
        fmt.Println(&quot;Error writing csv to file:&quot;, err)
        return
    }
    fmt.Printf(&quot;Output time-series data saved at %s.csv&quot;, outputCsvPath)
}
</code></pre></details>

<details><summary>C#</summary>

<pre><code class="language-csharp">using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class Program
{
    static readonly string API_URL = &quot;http://localhost:8080/time-series-anomaly-detection&quot;;
    static readonly string csvPath = &quot;./test.csv&quot;;
    static readonly string outputCsvPath = &quot;./out.csv&quot;;

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();

        // 对本地csv文件进行Base64编码
        byte[] csvBytes = File.ReadAllBytes(csvPath);
        string csvData = Convert.ToBase64String(csvBytes);

        var payload = new JObject{ { &quot;csv&quot;, csvData } }; // Base64编码的文件内容
        var content = new StringContent(payload.ToString(), Encoding.UTF8, &quot;application/json&quot;);

        // 调用API
        HttpResponseMessage response = await httpClient.PostAsync(API_URL, content);
        response.EnsureSuccessStatusCode();

        // 处理接口返回数据
        string responseBody = await response.Content.ReadAsStringAsync();
        JObject jsonResponse = JObject.Parse(responseBody);

        // 保存csv文件
        string base64Csv = jsonResponse[&quot;result&quot;][&quot;csv&quot;].ToString();
        byte[] outputCsvBytes = Convert.FromBase64String(base64Csv);
        File.WriteAllBytes(outputCsvPath, outputCsvBytes);
        Console.WriteLine($&quot;Output time-series data saved at {outputCsvPath}&quot;);
    }
}
</code></pre></details>

<details><summary>Node.js</summary>

<pre><code class="language-js">const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/time-series-anomaly-detection'
const csvPath = &quot;./test.csv&quot;;
const outputCsvPath = &quot;./out.csv&quot;;

let config = {
   method: 'POST',
   maxBodyLength: Infinity,
   url: API_URL,
   data: JSON.stringify({
    'csv': encodeFileToBase64(csvPath)  // Base64编码的文件内容
  })
};

// 读取csv文件并转换为Base64
function encodeFileToBase64(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString('base64');
}

axios.request(config)
.then((response) =&gt; {
    const result = response.data[&quot;result&quot;];

    // 保存csv文件
    const csvBuffer = Buffer.from(result[&quot;csv&quot;], 'base64');
    fs.writeFile(outputCsvPath, csvBuffer, (err) =&gt; {
      if (err) throw err;
      console.log(`Output time-series data saved at ${outputCsvPath}`);
    });
})
.catch((error) =&gt; {
  console.log(error);
});
</code></pre></details>

<details><summary>PHP</summary>

<pre><code class="language-php">&lt;?php

$API_URL = &quot;http://localhost:8080/time-series-anomaly-detection&quot;; // 服务URL
$csv_path = &quot;./test.csv&quot;;
$output_csv_path = &quot;./out.csv&quot;;

// 对本地csv文件进行Base64编码
$csv_data = base64_encode(file_get_contents($csv_path));
$payload = array(&quot;csv&quot; =&gt; $csv_data); // Base64编码的文件内容

// 调用API
$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// 处理接口返回数据
$result = json_decode($response, true)[&quot;result&quot;];

file_put_contents($output_csv_path, base64_decode($result[&quot;csv&quot;]));
echo &quot;Output time-series data saved at &quot; . $output_csv_path . &quot;\n&quot;;

?&gt;
</code></pre></details>
</details>
<br/>

📱 <b>端侧部署</b>：端侧部署是一种将计算和数据处理功能放在用户设备本身上的方式，设备可以直接处理数据，而不需要依赖远程的服务器。PaddleX 支持将模型部署在 Android 等端侧设备上，详细的端侧部署流程请参考[PaddleX端侧部署指南](../../../pipeline_deploy/edge_deploy.md)。
您可以根据需要选择合适的方式部署模型产线，进而进行后续的 AI 应用集成。

## 4. 二次开发
如果通用时序异常检测产线提供的默认模型权重在您的场景中，精度或速度不满意，您可以尝试利用<b>您自己拥有的特定领域或应用场景的数据</b>对现有模型进行进一步的<b>微调</b>，以提升通用时序异常检测产线的在您的场景中的识别效果。

### 4.1 模型微调
由于通用时序异常检测产线包含时序异常检测模块，如果模型产线的效果不及预期，那么您需要参考[时序预测模块开发教程](../../../module_usage/tutorials/time_series_modules/time_series_anomaly_detection.md)中的[二次开发](../../../module_usage/tutorials/time_series_modules/time_series_anomaly_detection.md#四二次开发)章节，使用您的私有数据集对时序异常检测模型进行微调。

### 4.2 模型应用
当您使用私有数据集完成微调训练后，可获得本地模型权重文件。

若您需要使用微调后的模型权重，只需对产线配置文件做修改，将微调后模型权重的本地路径替换至产线配置文件中的对应位置即可：

```python
......
Pipeline:
  model: DLinear_ad  #可修改为微调后模型的本地路径
  batch_size: 1
  device: "gpu:0"
......
```

随后， 参考本地体验中的命令行方式或 Python 脚本方式，加载修改后的产线配置文件即可。

##  5. 多硬件支持
PaddleX 支持英伟达 GPU、昆仑芯 XPU、昇腾 NPU和寒武纪 MLU 等多种主流硬件设备，<b>仅需修改 `--device` 参数</b>即可完成不同硬件之间的无缝切换。

例如，您使用英伟达 GPU 进行时序异常检测产线的推理，使用的 Python 命令为：

```bash
paddlex --pipeline ts_ad --input ts_ad.cs --device gpu:0
```
此时，若您想将硬件切换为昇腾 NPU，仅需对 Python 命令中的` --device` 修改为 npu:0 即可：

```bash
paddlex --pipeline ts_ad --input ts_ad.cs --device npu:0
```
若您想在更多种类的硬件上使用通用时序异常检测产线，请参考[PaddleX多硬件使用指南](../../../other_devices_support/multi_devices_use_guide.md)。
