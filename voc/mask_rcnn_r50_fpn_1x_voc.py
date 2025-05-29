_base_ = [
    '../_base_/models/mask-rcnn_r50_fpn.py',
    '../_base_/datasets/voc0712.py',      # 加回 VOC 数据集定义
    '../_base_/schedules/schedule_1x.py',
    '../_base_/default_runtime.py'
]
# 加入 VOC 的数据集配置
dataset_type = 'VOCDataset'


# 定义 VOC 的 20 类
classes = (
    'aeroplane','bicycle','bird','boat','bottle','bus','car','cat',
    'chair','cow','diningtable','dog','horse','motorbike','person',
    'pottedplant','sheep','sofa','train','tvmonitor'
)

model = dict(
    roi_head=dict(
        mask_head=None
    )
)
