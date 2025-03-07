## 使用须知
### 1. 安装本地的轮子
```shell
# 内网安装某轮子
pip3 install --index-url=http://192.168.1.82:8091/repository/pypi-group/simple --trusted-host=192.168.1.82 pywxbase==0.1
# 外网安装某轮子
pip3 install --index-url=http://36.249.183.216:8091/repository/pypi-group/simple --trusted-host=36.249.183.216 pywxbase==0.1
# 内网安装 requirements.txt
pip3 install -r requirements.txt --index-url=http://192.168.1.82:8091/repository/pypi-group/simple --trusted-host=192.168.1.82
# 外网安装 requirements.txt
pip3 install -r requirements.txt --index-url=http://36.249.183.216:8091/repository/pypi-group/simple --trusted-host=36.249.183.216
# 或者
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# window 外部安装轮子
pip3 install pyside6~=6.6.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install ..\pywxbase-1.1.1-py3-none-any.whl
``` 

### 注意
```text
如果你已经正确地配置了 .pyi 文件，但仍然没有得到代码提示，可能需要检查 IDE 的设置。
例如，PyCharm 需要确保“Type hints”功能已经启用，并且能够正确读取 .pyi 文件。

如果你使用的是 PyCharm，可以尝试：

Invalidate Caches / Restart：PyCharm -> File -> Invalidate Caches / Restart，来刷新缓存。
```