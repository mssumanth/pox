'''
Created on Aug 14, 2011

@author: peymankazemian
'''
from pox.lib.headerspace.NSDI_examples.load_stanford_backbone import *
from pox.lib.headerspace.config_parser.cisco_router_parser import ciscoRouter
from pox.lib.headerspace.headerspace.hs import *
from pox.lib.headerspace.headerspace.applications import *
from time import time, clock

ntf = load_stanford_backbone_ntf()
ttf = load_stanford_backbone_ttf()
(port_map,port_reverse_map) = load_stanford_backbone_port_to_id_map()
cs = ciscoRouter(1)
#add_internet(ntf,ttf,port_map,cs,[("171.64.0.0",14),("128.12.0.0",16)])

all_x = byte_array_get_all_x(ntf.length)
#cs.set_field(all_x, "ip_dst", dotted_ip_to_int("172.0.0.0"), 21)
cs.set_field(all_x, "vlan", 92, 0)
test_pkt = headerspace(ntf.length)
test_pkt.add_hs(all_x)

src_port_id = port_map["yoza_rtr"]["te7/4"]
dst_port_ids = [port_map["roza_rtr"]["te3/3"]]
loop_port_ids = [
                 port_map["bbra_rtr"]["te7/1"],port_map["bbrb_rtr"]["te7/1"],
                 port_map["bbra_rtr"]["te6/3"],port_map["bbrb_rtr"]["te7/4"],
                 port_map["bbra_rtr"]["te7/2"],port_map["bbrb_rtr"]["te1/1"],
                 port_map["bbra_rtr"]["te6/1"],port_map["bbrb_rtr"]["te6/3"],
                 port_map["bbra_rtr"]["te1/4"],port_map["bbrb_rtr"]["te1/3"],
                 port_map["bbra_rtr"]["te1/3"],port_map["bbrb_rtr"]["te7/2"],
                 port_map["bbra_rtr"]["te7/3"],port_map["bbrb_rtr"]["te6/1"],
                 port_map["boza_rtr"]["te2/3"],port_map["coza_rtr"]["te2/3"],
                 port_map["yozb_rtr"]["te1/3"],port_map["yozb_rtr"]["te1/2"],
                 port_map["yoza_rtr"]["te1/1"],port_map["yoza_rtr"]["te1/2"],
                 port_map["bozb_rtr"]["te2/3"],port_map["cozb_rtr"]["te2/3"],
                 port_map["gozb_rtr"]["te2/3"],port_map["pozb_rtr"]["te2/3"],
                 port_map["goza_rtr"]["te2/3"],port_map["poza_rtr"]["te2/3"],
                 port_map["rozb_rtr"]["te2/3"],port_map["sozb_rtr"]["te2/3"],
                 port_map["roza_rtr"]["te2/3"],port_map["soza_rtr"]["te2/3"],
                 ]
test1 = [port_map["goza_rtr"]["te2/3"]]
st = time()

paths = find_reachability(ntf,ttf,src_port_id,dst_port_ids,test_pkt)
en = time()
print_loops(paths, port_reverse_map)
print len(paths)

#loops = detect_loop(ntf,ttf,loop_port_ids,port_reverse_map)
#en = time()
#print_loops(loops, port_reverse_map)
#print len(loops)

print en-st
