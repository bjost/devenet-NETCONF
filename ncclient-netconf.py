from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

'''
print("#Supported Capabilities (YANG models): ")
for capability in m.server_capabilities:
    print(capability)
'''

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
'''
netconf_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface operation="delete">
        <Loopback>
        <name>1</name>
        <description>My firts NETCONF loopback</description>
        <ip>
          <address>
            <primary>
              <address>10.1.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""
'''

RSTForum_netconf_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                        <name>Loopback1</name>
                </interface>
        </interfaces>
</config>
"""

netconf_reply = m.edit_config(target="running", config=RSTForum_netconf_template)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#netconf_reply = m.get_config(source="running")
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
