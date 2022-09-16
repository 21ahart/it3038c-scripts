
$IP =  (get-netipaddress).ipv4address | Select-String "192*"
$USER = $env:USERNAME
$HOSTNAME = hostname
$VERMA = $HOST.Version.Major
$DAY = (Get-Date).DayOfWeek
$DATEDAY = (Get-Date).Day
$DATEMON = (get-date).Month
$DATEYEA = (get-date).Year

$BODY = "This Machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $VERMA. Today's Date is $DAY, $DATEMON $DATEDAY $DATEYEA"