import subprocess
subprocess.run(["powershell", "-Command", "Get-AppxPackage Microsoft.549981C3F5F10 | Remove-AppxPackage -AllUsers"])
subprocess.run(["powershell", "-Command", "Get-AppxPackage Microsoft.MicrosoftEdge | Remove-AppxPackage -AllUsers"])
subprocess.run(["powershell", "-Command", "Get-AppxProvisionedPackage -Online | where-object {$_.PackageName -like '*Microsoft.549981C3F5F10*'} | Remove-AppxProvisionedPackage -Online"])
subprocess.run(["powershell", "-Command", "Get-AppxProvisionedPackage -Online | where-object {$_.PackageName -like '*Microsoft.MicrosoftEdge*'} | Remove-AppxProvisionedPackage -Online"])
