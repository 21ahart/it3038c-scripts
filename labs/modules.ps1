function fileinfo($str)
{
    $version = Get-FileVersionInfo $str
    $tail = Get-FileTail $str
    $hash = get-hash $str

    Write-Output "***The file version of $str is:***"
    Write-Output $version
    Write-Output "***The last few lines of the file are:***"
    Write-Output $tail
    Write-Output "***The hash for the file is:***"
    Write-Output $hash
}
$file = read-host "Enter the file you want to look at"
fileinfo($file)