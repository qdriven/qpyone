#!/usr/bin/env python
import os

import paramiko

from loguru import logger


class RemoteServe:
    """远程服务器"""

    def __init__(
        self,
        host: str,
        port: int = 22,
        username: str = "root",
        password: str = None,
        private_key_file: str = None,
        private_password: str = None,
    ):
        # 进行SSH连接
        self.trans = paramiko.Transport((host, port))
        self.host = host
        if password is None:
            self.trans.connect(
                username=username,
                pkey=paramiko.RSAKey.from_private_key_file(
                    private_key_file, private_password
                ),
            )
        else:
            self.trans.connect(username=username, password=password)
        # 将sshclient的对象的transport指定为以上的trans
        self.ssh = paramiko.SSHClient()
        logger.success("SSH客户端创建成功.")
        self.ssh._transport = self.trans
        # 创建SFTP客户端
        self.ftp_client = paramiko.SFTPClient.from_transport(self.trans)
        logger.success("SFTP客户端创建成功.")

    def execute_cmd(self, cmd: str):
        """
        :param cmd: 服务器下对应的命令
        """
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        error = stderr.read().decode()
        logger.info(f"输入命令: {cmd} -> 输出结果: {stdout.read().decode()}")
        logger.warning(f"异常信息: {error}")
        return error

    def files_action(
        self, post: bool, local_path: str = os.getcwd(), remote_path: str = "/root"
    ):
        """
        :param post: 动作 为 True 就是上传， False就是下载
        :param local_path: 本地的文件路径， 默认当前脚本所在的工作目录
        :param remote_path: 服务器上的文件路径，默认在/root目录下
        """
        if post:  # 上传文件
            self.execute_cmd("mkdir backup_sql")
            self.ftp_client.put(
                localpath=local_path,
                remotepath=f"{remote_path}{os.path.split(local_path)[1]}",
            )
            logger.info(
                f"文件上传成功: {local_path} -> {self.host}:{remote_path}{os.path.split(local_path)[1]}"
            )
        else:  # 下载文件
            if not os.path.exists(local_path):
                os.mkdir(local_path)
            file_path = local_path + os.path.split(remote_path)[1]
            self.ftp_client.get(remotepath=remote_path, localpath=file_path)
            logger.info(f"文件下载成功: {self.host}:{remote_path} -> {file_path}")

    def ssh_close(self):
        """关闭连接"""
        self.trans.close()
        logger.info("已关闭SSH连接...")
