# 此仓库为一个常见图像分类网络的一个合集

Dataset中放置自定义数据集

model_data中存放自定义数据集类别的txt文件

修改主干网络可堆train.py文件中的64行进行修改，具体输入可参考nets/init.py中定义，也可在该文件中进行自定义，nets/目录下相较于原仓库代码新增mobilenetv2、mobilenetv3、RepVGG等分类主干网络，同时nets/录路径下新增ASPP多尺度特征提取结构、CBAM注意力机制、CA注意力机制、NAM注意力机制等

新增dir_predict.py，对指定目录下所有图像进行预测

[原仓库地址](https://github.com/bubbliiiing/classification-pytorch)



