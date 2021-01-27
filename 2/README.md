# Prompt
Create a script to start/stop Azure VM.  You can use whichever scripting language you want.

#Assumptions
I assumed that I would have a machine `tpstest` in RG `tpstest_group`.  Of course, this could be parameterized.

# Solution

I created shell and PowerShell scripts, using the `az` command in the former case and native PowerShell in the second.  Many approaches that could be taken here, depending on use case:

- shell alias or function
- shell or PS1 script, as here
- cron or some other scheduling device, including [Microsoft supported solution](https://docs.microsoft.com/en-us/azure/automation/automation-solution-vm-management)
