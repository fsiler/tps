#Prompt

Azure ARM template definition to create a VNET, a subnet, and then a small 2 core 8 gb ram VM using the VNET and subnet.

#Solution

Files `template.json` and `params.json` largely came from the "Start VM" wizard.  However, I modified them to include things like a default password.  In the "real world", you would not do this and would instead use either some centralized form of authentication (AD/Kerberos) or have a tightly controlled set of SSH keys used for access.  However, for the purposes of getting a VM up quickly and demonstrating templating, I thought this was sufficient.