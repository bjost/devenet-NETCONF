from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

#print("#Supported Capabilities (YANG models):")
#for capability in m.server_capabilities:
#    print(capability)

#netconf_reply = m.get_config(source="running")
#print(netconf_reply)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" /> 
</filter>
"""
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CSR1kv</hostname>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)

#netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
