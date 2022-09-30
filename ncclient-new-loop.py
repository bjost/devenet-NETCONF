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

netconf_loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>101</name>
            <description>My first NETCONF loopback</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                "ianaift:softwareLoopback"
            </type>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                  <ip>172.16.101.1</ip>
                  <netmask>255.255.255.0</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)

#netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
