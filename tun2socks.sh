#!/bin/bash
apt install unzip
# 检查是否为root用户
if [ "$(id -u)" != "0" ]; then
   echo "此脚本需要root权限运行" 
   exit 1
fi

# 1. 创建文件夹并下载tun2socks
echo "步骤1: 创建目录并下载tun2socks..."
mkdir -p /etc/tun2socks
cd /etc/tun2socks

# 下载并解压tun2socks
wget https://ghfast.top/github.com/xjasonlyu/tun2socks/releases/download/v2.5.2/tun2socks-linux-amd64.zip
unzip tun2socks-linux-amd64.zip
mv tun2socks-linux-amd64 tun2socks
chmod +x tun2socks
rm tun2socks-linux-amd64.zip

# 2. 直接在主脚本中处理网卡选择
echo "步骤2: 选择网络接口..."
# 获取除lo和tun之外的所有网卡
interfaces=($(ip -o link show | awk -F': ' '{print $2}' | grep -v "lo\|tun"))

# 显示网卡列表
echo "======================"
echo "可用网卡列表:"
for i in "${!interfaces[@]}"; do
    echo "$((i+1)). ${interfaces[$i]}"
done
echo "======================"

# 获取用户选择
while true; do
    read -p "请选择网卡 (1-${#interfaces[@]}): " choice
    if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le "${#interfaces[@]}" ]; then
        selected_interface=${interfaces[$((choice-1))]}
        echo "已选择网卡: $selected_interface"
        break
    else
        echo "无效选择，请重试"
    fi
done

# 获取默认网关IP
default_gateway=$(ip route | grep "default via" | grep "$selected_interface" | awk '{print $3}')
if [ -z "$default_gateway" ]; then
    default_gateway=$(ip route | grep "$selected_interface" | grep -v "default" | head -n 1 | awk '{print $1}' | cut -d'/' -f1)
    if [ -z "$default_gateway" ]; then
        read -p "无法自动获取默认网关，请手动输入默认网关IP: " default_gateway
    fi
fi

# 获取SOCKS5代理地址
read -p "请输入SOCKS5代理地址 (格式: IP:端口): " socks5_proxy

# 3. 配置网络
echo "步骤3: 配置网络..."
ip tuntap add mode tun dev tun0
ip addr add 198.18.0.1/15 dev tun0
ip link set dev tun0 up
ip route del default
ip route add default via 198.18.0.1 dev tun0 metric 1
ip route add default via $default_gateway dev $selected_interface metric 10

# 4. 创建systemd服务文件
echo "步骤4: 创建自启服务..."
cat > /etc/systemd/system/tun2socks.service << EOF
[Unit]
Description=Tun2socks Service
After=network.target

[Service]
StartLimitInterval=5
StartLimitBurst=10
ExecStart=/etc/tun2socks/tun2socks -device tun0 -proxy socks5://${socks5_proxy} -interface ${selected_interface}

[Install]
WantedBy=multi-user.target
EOF

# 5. 启用并启动服务
echo "步骤5: 注册并启动服务..."
systemctl daemon-reload
systemctl enable tun2socks.service
systemctl start tun2socks.service

# 检查服务状态
status=$(systemctl is-active tun2socks.service)
if [ "$status" = "active" ]; then
    echo "✓ Tun2socks服务已成功启动!"
else
    echo "✗ Tun2socks服务启动失败，状态: $status"
    echo "请使用 'systemctl status tun2socks.service' 查看详细信息"
fi

echo "配置完成！"
echo "现在所有流量都会通过SOCKS5代理: ${socks5_proxy}"
echo "您可以使用以下命令管理服务:"
echo "  启动: systemctl start tun2socks.service"
echo "  停止: systemctl stop tun2socks.service"
echo "  重启: systemctl restart tun2socks.service"
echo "  状态: systemctl status tun2socks.service"
