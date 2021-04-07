# sdn_cloud
1、在ryu/app 中启动`sudo ryu-manager ofctl_rest.py`
2、在当前文件夹爱启动交换机`sudo ryu-manager example_switch_13.py`
~~~
当时为了能够启动wireshark，修改了用户组以及/usr/bin/dump文件权限为750，导致1/2步骤命令需要加上sudo，否则无返回值

sudo chgrp xxxxxxx /usr/bin/dumpcap
sudo chmod 750 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap
~~~
3、启动topo `sudo python MiniNAM.py --custom topo.py --topo mytopo,4 --controller=remote`
4、启动控制脚本`python old-flowController.py`



问题：
有的时候请求成功，有的时候失败

在实体机器上请求总是失败。

请求地址应0.0.0.0


尝试，删除控制器引用wisg服务。
