# 示例验证记录

日期：2026-11-13。

环境：Python 3.12.10，NumPy 2.5.3，Matplotlib 3.11.2。

执行命令：

```sh
python courses/cad/bspline/cad_bspline.py
python courses/cad/bspline/verify_example.py
```

结果：两条命令均退出 0。基函数非负性、单位分解、有限性和端点插值检查通过。有理数 de Boor 与基函数曲线求值共比较 801 个参数点，最大坐标差约 1.42e-14，超出参数区间的输入被拒绝。

两张输出图已人工查看，无身份信息，标题、图例与曲线显示正常。验证覆盖该固定示例，不覆盖所有节点向量或自定义输入。
