
#Chatglm和LLama-index
# ChatFiles
**上传文件然后与之对话.**

## 如何使用

上传文件对话，可以看看这些例子: [Good Example](./doc/Example.md)


### 与文件对话
上传文件。
问与文件有关的内容。

### 与 Chatglm 对话
直接发送消息，而无需上传文件。

## 如何本地运行
### chatfiles-ui

```shell
cd chatfiles-ui
npm install
npm run dev
```

### chatfiles
```shell
cd chatfiles
```


```shell
python3 server.py
```

## 如何部署到 fly.io
- [Deploy to fly.io](./doc/deploy-flyio.md)

## 功能

- [x] 与 GPT-3.5 对话。
- [x] 与你上传的文件对话。
- [x] 上传多个文件，构建同一个 Index，然后与之对话。
