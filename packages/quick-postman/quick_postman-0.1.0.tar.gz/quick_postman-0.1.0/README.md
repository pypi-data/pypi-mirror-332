# Quick Poster

一个简单易用的邮件发送工具，基于Python实现。

## 项目简介

Easy Mail Sender是一个轻量级的邮件发送库，旨在简化Python应用程序中的邮件发送流程。它提供了简洁的API，使您能够轻松地发送电子邮件，而无需处理底层的SMTP细节。

## 特性

- 简单易用的API
- 支持SSL加密连接
- 基于环境变量的配置管理
- 使用数据类进行邮件信息的结构化管理

## 安装

使用PDM安装:

```bash
pdm add easy-mail-sender
```

或者使用pip:

```bash
pip install easy-mail-sender
```

## 配置

在使用之前，您需要设置以下环境变量:

```
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

您可以创建一个`.env`文件在项目根目录下，或者直接在环境中设置这些变量。

## 使用示例

```python
from easy_mail_sender import MailInfo, MailWorker

# 创建邮件信息
mail_info = MailInfo(
    receiver_email="recipient@example.com",
    subject="测试邮件",
    body="这是一封测试邮件的内容。"
)

# 创建邮件工作器并发送邮件
worker = MailWorker(mail_info)
worker.send()
```

## 自定义SMTP服务器

默认情况下，Easy Mail Sender使用腾讯企业邮箱的SMTP服务器。如果您需要使用其他SMTP服务器，可以在创建`MailWorker`实例后修改相关属性：

```python
worker = MailWorker(mail_info)
worker.mail_server = "smtp.gmail.com"
worker.port = 587
worker.send()
```

## 开发

### 环境设置

1. 克隆仓库:
```bash
git clone https://github.com/yourusername/easy-mail-sender.git
cd easy-mail-sender
```

2. 使用PDM安装依赖:
```bash
pdm install
```

### 运行测试

```bash
pdm run pytest
```

## 许可证

本项目采用MIT许可证 - 详情请参阅LICENSE文件。

## 贡献

欢迎提交问题和拉取请求！
