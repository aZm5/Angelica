材料：原始相似性文件   目标：转成带编号的不同类型的相似性文件

1.使用shell_script_generator.py生成脚本命令bit_score_generator.sh文件（注意路径问题）
2.git bash中运行上述.sh文件--->得到去重的相似性文件
3.运行coverage.py生成不同类型的相似性文件（会有将原始蛋白质名转换成物种加编号的过程）