# sdn_cloud
最好将my_switch.py 和 old-flowController.py复制到 ryu/app文件夹中

1/启动现在ryu/app中启动 `sudo ryu-manager ofctl_rest.py my_switch.py`(错误示范中example_switch_13.py的重命名)
~~~
错误的启动过程，服了，被坑了好久，太猪了
1、在ryu/app 中启动`sudo ryu-manager ofctl_rest.py`
2、在当前文件夹爱启动交换机`sudo ryu-manager example_switch_13.py`
~~~

~~~
当时为了能够启动wireshark，修改了用户组以及/usr/bin/dump文件权限为750，导致1/2步骤命令需要加上sudo，否则无返回值

sudo chgrp xxxxxxx /usr/bin/dumpcap
sudo chmod 750 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap
~~~
3、启动topo `sudo python MiniNAM.py --custom topo.py --topo mytopo,4 --controller=remote`
4、启动控制脚本`python old-flowController.py`


