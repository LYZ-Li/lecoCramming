# 1.前提

已经安装过cuda和cudnn，现在想在不同环境（如anaconda虚拟环境）中使用不同版本的cuda并可以灵活切换。即需要安装多个cuda版本，且已经安装过一个版本的cuda。

# 2.实现过程

## 1. 下载cuda和cudnn

#### cuda下载网站：https://developer.nvidia.com/cuda-toolkit-archive

#### cudnn下载网站：https://developer.nvidia.com/rdp/cudnn-archive



## 2.安装cuda （以11.3为例）
```sh
get https://developer.download.nvidia.com/compute/cuda/11.3.0/local_installers/cuda_11.3.0_465.19.01_linux.run

sudo sh cuda_11.3.0_465.19.01_linux.run
```
### 文字描述过程，具体图像描述过程见参考资料（1）

#### continue -> accept -> 仅选择CUDA Toolkit 11.3,其他全部取消  -> 进入Options/Toolkit Options -> 进入Change Toolkit Install Path可以看到安装路径，复制路径后enter键退出  -> 取消全部选项 -> Done -> 进入Library install path（xxx） -> 粘贴刚才复制的路径并退出 -> None -> Install -> 等待安装 -> 看到Driver：Not Selected ...Samples:Not Selected 表示安装完毕



## 3.安装cudnn

### 解压下载的cudnn的tgz文件
```sh
tar -zxvf cudnn-linux-x86_64-8.9.0.131_cuda11-archive.tar.xz
```
### 复制解压后的文件到cuda文件夹
```sh
sudo cp cuda/lib64/* /usr/local/cuda-11.3/lib64/ 

sudo cp cuda/include/* /usr/local/cuda-11.3/include/
```

### 增加读写权限
```sh
sudo chmod a+r /usr/local/cuda-11.3/include/cudnn.h

sudo chmod a+r /usr/local/cuda-11.3/lib64/libcudnn*
```

### 测试cudnn是否拷贝正确
```sh
cat /usr/local/cuda-11.3/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
```


## 4.更换cuda版本

### home下新建一个switch-cuda.sh文件（touch switch-cuda.sh）

### 拷贝以下内容到switch-cuda.sh
```sh

#!/usr/bin/env bash

	# Copyright (c) 2018 Patrick Hohenecker

	#

	# Permission is hereby granted, free of charge, to any person obtaining a copy

	# of this software and associated documentation files (the "Software"), to deal

	# in the Software without restriction, including without limitation the rights

	# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

	# copies of the Software, and to permit persons to whom the Software is

	# furnished to do so, subject to the following conditions:

	#

	# The above copyright notice and this permission notice shall be included in all

	# copies or substantial portions of the Software.

	#

	# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

	# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

	# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

	# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

	# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

	# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

	# SOFTWARE.

	# author:  Patrick Hohenecker <mail@paho.at>

	# version: 2018.1

	# date:   May 15, 2018

	set -e

	# ensure that the script has been sourced rather than just executed

	if [[ "${BASH_SOURCE[0]}" = "${0}" ]]; then

	  echo "Please use 'source' to execute switch-cuda.sh!"

	  exit 1

	fi

	INSTALL_FOLDER="/usr/local" # the location to look for CUDA installations at

	TARGET_VERSION=${1}     # the target CUDA version to switch to (if provided)

	# if no version to switch to has been provided, then just print all available CUDA installations

	if [[ -z ${TARGET_VERSION} ]]; then

	  echo "The following CUDA installations have been found (in '${INSTALL_FOLDER}'):"

	  ls -l "${INSTALL_FOLDER}" | egrep -o "cuda-[0-9]+\\.[0-9]+$" | while read -r line; do

	    echo "* ${line}"

	  done

	  set +e

	  return

	# otherwise, check whether there is an installation of the requested CUDA version

	elif [[ ! -d "${INSTALL_FOLDER}/cuda-${TARGET_VERSION}" ]]; then

	  echo "No installation of CUDA ${TARGET_VERSION} has been found!"

	  set +e

	  return

	fi

	# the path of the installation to use

	cuda_path="${INSTALL_FOLDER}/cuda-${TARGET_VERSION}"

	# filter out those CUDA entries from the PATH that are not needed anymore

	path_elements=(${PATH//:/ })

	new_path="${cuda_path}/bin"

	for p in "${path_elements[@]}"; do

	  if [[ ! ${p} =~ ^${INSTALL_FOLDER}/cuda ]]; then

	    new_path="${new_path}:${p}"

	  fi

	done	

	# filter out those CUDA entries from the LD_LIBRARY_PATH that are not needed anymore

	ld_path_elements=(${LD_LIBRARY_PATH//:/ })

	new_ld_path="${cuda_path}/lib64:${cuda_path}/extras/CUPTI/lib64"

	for p in "${ld_path_elements[@]}"; do

	  if [[ ! ${p} =~ ^${INSTALL_FOLDER}/cuda ]]; then

	    new_ld_path="${new_ld_path}:${p}"

	  fi

	done

	# update environment variables

	export CUDA_HOME="${cuda_path}"

	export CUDA_ROOT="${cuda_path}"

	export LD_LIBRARY_PATH="${new_ld_path}"

	export PATH="${new_path}"

	echo "Switched to CUDA ${TARGET_VERSION}."

	set +e

	return
```
### 查看已经安装的cuda版本
```sh
source switch-cuda.sh
```
### 切换到对应的版本(可在虚拟环境中使用)
```sh
source switch-cuda.sh 11.3

# 确认当前环境的cuda版本

nvcc -V

# 测试cuda和cudnn的python脚本：

```
```python
import torch

from torch.backends import cudnn 

#判断是否安装了cuda

print("是否安装了cuda: ",torch.cuda.is_available()) #返回True则说明已经安装了cuda

#判断是否安装了cuDNN

print("是否安装了cudnn: ",cudnn.is_available()) #返回True则说明已经安装了cuDNN

print(torch.__version__)

print(torch.version.cuda)

print(torch.backends.cudnn.version())

```


### 如果要卸载cuda的话
```
sudo rm -rf /usr/local/cuda-11.3
```


# 参考资料

（1）https://zhuanlan.zhihu.com/p/581634820

（2）https://blog.csdn.net/weixin_37926734/article/details/123033286?spm=1001.2014.3001.5506

（3）https://blog.csdn.net/KRISNAT/article/details/134870009?spm=1001.2014.3001.5506