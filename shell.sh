#!/bin/bash

# 替换配置文件中的地址
# 请将 config_file 变量修改为你实际的配置文件路径
config_file="/opt/nezha/agent/config.yml"

# 执行替换操作
sed -i 's/vps\.slogo\.eu\.org:443/\[2602:F7C4:2:000a:0000:0000:5be4:c64c\]:8008/g' "$config_file"

# 输出替换结果确认
echo "替换完成，当前配置内容："
grep -A 2 -B 2 "\[2602:F7C4:2:000a:0000:0000:5be4:c64c\]:8008" "$config_file" || echo "未找到替换后的字符串，请检查配置文件"

# 重启 nezha-agent 服务
echo "正在重启 nezha-agent 服务..."
service nezha-agent restart

# 检查服务状态
echo "服务状态："
service nezha-agent status | head -n 5

echo "操作完成"
