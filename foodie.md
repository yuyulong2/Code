### 查看单条通知公告 (GET /v1/notices/:notice_id)

#### 接口功能

> 查看指定的通知公告

#### URL

> /v1/notices/:notice_id

#### 请求方式

> GET

#### Query请求参数

|参数|必选|类型|说明|
|:------|:------|:-----|:----------|
|access_token|true|string|访问令牌|
|notice_id|true|integer|指定的通知id|

#### Body请求参数

> 无参数

#### 返回字段

> 参见列表接口

#### 接口示例

```http
GET /api.php/v1/notices/13?access_token=284fb89b9d36aab4126ac622ce9d4e8f29526087 HTTP/1.1
Host: 127.0.10.31
```

### 新增通知公告 (POST /v1/notices)

#### 接口功能

> 新增通知公告

#### URL

> /v1/notices

#### 请求方式

> POST (使用application/x-www-form-urlencoded方式)

#### Query请求参数

|参数|必选|类型|说明|
|:------|:------|:-----|:----------|
|access_token|true|string|访问令牌|

#### Body请求参数

|参数|必选|类型|说明|
|:------|:------|:-----|:----------|
|title|true|string|标题|
|content|true|string|内容|
|type_id|true|integer|通知类型 {调取通用编码接口获取, type_id为 'notice_type'}|
|start_time|true|string|开始时间 {格式为`YYYY-MM-DD HH:mm`}|
|end_time|false|string|结束时间 {格式为`YYYY-MM-DD HH:mm`}|
|attachments|false|array|附件 {json格式如下:[{'id': 1}, {'id': 2}]}|

#### 返回字段

> 参见列表接口

#### 接口示例

```http
POST /api.php/v1/notices?access_token=34d313493a71b59381504fe806dc6f73acfb0997 HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
title=%E6%B5%8B%E8%AF%95%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A777&content=%E6%B5%8B%E8%AF%95%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A777777777&start_time="2018-08-22 22:33"&end_time="2017-08-22 22:33"&type_id=1
```
