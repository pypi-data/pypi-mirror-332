cat > setup_user/setup_user.py << 'EOF'
import os
import subprocess

def setup_user(username="lanbot", password="Lz147369"):
    # 检查当前用户是否为root
    if os.geteuid() != 0:
        print("请以root权限运行此脚本")
        return

    # 检查用户是否已存在
    if subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        print(f"用户 {username} 已存在，跳过创建")
    else:
        # 创建用户
        subprocess.run(["useradd", "-m", "-s", "/bin/bash", username], check=True)
        # 设置密码
        subprocess.run(["chpasswd"], input=f"{username}:{password}", text=True, check=True)
        print(f"用户 {username} 已创建")

    # 将用户添加到sudo组
    if "sudo" not in subprocess.run(["groups", username], capture_output=True, text=True).stdout:
        subprocess.run(["usermod", "-aG", "sudo", username], check=True)
        print(f"用户 {username} 已添加到sudo组")
    else:
        print(f"用户 {username} 已经在sudo组中")

    print(f"用户 {username} 的默认密码为: {password}")
    print("请登录后立即修改密码以确保安全")

if __name__ == "__main__":
    setup_user()
EOF
