# classicML-server: classicML 的 web 服务

classicML-server 是一个将 classicML 训练完成的模型部署在服务器上的命令行工具。

## 实例

在你的服务器上启动服务.

```shell
classicML-server \
--service_mode='predict_service' \
--model_type='LDA' \
--model_path='/path/to/model.h5'
```

以Python客户端示例.

```python
import json
import requests

import numpy as np


url = 'http://127.0.0.1:8051/v0/predict/'  # URL构建规则: host:port/v0/predict/
data = json.dumps({
    'x': np.asarray([[0.697, 0.774], [0.666, 0.091]]).tolist(),
})
headers = {'content-type': 'application/json'}

response = requests.post(url=url, data=data, headers=headers)
y_pred = np.asarray(response.json()['predictions'])
print(y_pred)
```

