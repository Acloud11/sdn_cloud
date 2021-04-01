# Copyright (C) 2016 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet


class FlowController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    flowMatrix = []
    flowMatrix.append([[0,1,0],[1,0,0],[0,0,0]])
    flowMatrix.append([[0,1,1],[1,0,0],[1,0,0]])

    def __init__(self, *args, **kwargs):
        super(FlowController, self).__init__(*args, **kwargs)

        self.ofp_brick = app_manager.lookup_service_brick('ofp_event')
        
	for i in range(len(self.flowMatrix)):
            event = ofp_event.EventOFChangeFlow(matrix = self.flowMatrix)
            self.ofp_brick.send_event_to_observers(event, MAIN_DISPATCHER)

	    for sec in range(100):
		print(sec+1)
		time.sleep(1)







