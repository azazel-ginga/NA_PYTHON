#!/usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class SshclientConnect:

    def __init__(self, _hostname, _username, _password, _port):
        self._hostname = _hostname
        self._username = _username
        self._password = _password
        self._port = _port
        self._ssh = None
        self._transport = None
        self._scp = None
        self.sshconnect
        self.sshclose

    def sshconnect(self):
        trans = paramiko.Transport(self._hostname, self._port)
        trans.connect(username=self._username, password=self._password)
        self._transport = trans

    def commandin(self, command):
    	self.sshconnect()
        self._ssh = paramiko.SSHClient()
        self._ssh._transport = self._transport
        stdin, stdout, stderr = self._ssh.exec_command(command)
        print stdout.read().decode()
        self.sshclose()

    def download(self, remotedirname, loaldirname):
        if self._scp is None:
            self._scp = paramiko.SFTPClient.from_transport(self._transport)
        self._scp.get(remotedir, loaldir)

    def upload(self, loaldirname, remotedirname):
        if self._scp is None:
            self._scp = paramiko.SFTPClient.from_transport(self._transport)
        self._scp.put(loaldir, remotedir)

    def sshclose(self):
        if self._transport:
            self._transport.close()
        if self._ssh:
            self._ssh.close()

