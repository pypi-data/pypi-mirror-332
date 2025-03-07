from VisualShape3D.Shape3D import Shape
from VisualShape3D.Visual import VisualShape3D

# 定义盒子的尺寸
length = 6
width = 5
height = 3

# 创建盒子的六个面

# 前面（YZ 平面）
front_face = Shape('rectangle', width, height)

# 后面（YZ 平面，平移到盒子后方）
back_face = Shape('rectangle', width, height)
back_face = back_face.transform(to=(0, 0, length))

# 左面（XZ 平面，旋转 90 度）
left_face = Shape('rectangle', length, height)
left_face = left_face.transform(alpha=90)

# 右面（XZ 平面，平移到盒子右侧并旋转 90 度）
right_face = Shape('rectangle', length, height)
right_face = right_face.transform(to=(width, 0, 0))
right_face = right_face.transform(alpha=90)

# 顶面（XY 平面，旋转并平移到盒子顶部）
top_face = Shape('rectangle', length, width)
top_face = top_face.transform(alpha=90)
top_face = top_face.transform(beta=90)
top_face = top_face.transform(to=(0, height, 0))

# 底面（XY 平面）
bottom_face = Shape('rectangle', length, width)

# 创建可视化对象
vs3d = VisualShape3D()

# 将各个面添加到可视化对象中
vs3d.add_shape(front_face)
vs3d.add_shape(back_face)
vs3d.add_shape(left_face)
vs3d.add_shape(right_face)
vs3d.add_shape(top_face)
vs3d.add_shape(bottom_face)

# 显示立体盒子
vs3d.show()