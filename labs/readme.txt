In this lab I used a PowerShell module that adds in a bunch of new cmdlets and functions to powershell.

To install this module to your PowerShell all you need to do is open up a powershell window on your machine and enter 
"Install-Module -Name Pscx -AllowPrerelease".

The goal of this script is to show some file info that you cannot get with the base PowerShell cmdlets. When running this 
script you'll be able to see the file version info, the tail of the file, and the file hash using the MD5 algorithm.

All you need to do to run this file is open it in power shell, complete the prompt with the file path of the file you
want to look at and then all of the results should be displayed in the powershell window.
