
# VOC目标检测实验：Mask R-CNN 与 Sparse R-CNN

本项目基于 [MMDetection](https://github.com/open-mmlab/mmdetection)，在 PASCAL VOC 数据集上训练和测试 Mask R-CNN 与 Sparse R-CNN 两种模型，完成实例分割与目标检测的对比分析。

---

---

## 📦 环境配置

请使用以下命令配置 Python 环境（推荐使用 conda）：

```bash
conda create -n mmdet python=3.11
conda activate mmdet
pip install -r requirements.txt

##文件处理
将voc文件加入configs文件夹中
将__init__.py替换mmdet中的相同文件（这样可以保证mmdet成功安装）

## 模型训练
CUDA_VISIBLE_DEVICES=2 python tools/train.py \
configs/mask_rcnn/mask_rcnn_r50_fpn_1x_voc.py \
--work-dir work_dirs/maskrcnn_voc0712


CUDA_VISIBLE_DEVICES=3 python tools/train.py \
configs/sparse_rcnn/sparse_rcnn_r50_fpn_1x_voc.py \
--work-dir work_dirs/sparsercnn_voc0712

##模型测试
CUDA_VISIBLE_DEVICES=2 python tools/test.py \
configs/mask_rcnn/mask_rcnn_r50_fpn_1x_voc.py \
work_dirs/maskrcnn_voc0712/epoch_12.pth \
--show-dir work_dirs/maskrcnn_voc0712/test_vis \
--show

CUDA_VISIBLE_DEVICES=3 python tools/test.py \
configs/sparse_rcnn/sparse_rcnn_r50_fpn_1x_voc.py \
work_dirs/sparsercnn_voc0712/epoch_12.pth \
--show-dir work_dirs/sparsercnn_voc0712/test_vis \
--show


