$py = (Get-Item $PSScriptRoot/main.py).FullName
if ((Get-Item $args[0]) -is [System.IO.DirectoryInfo]) {
    Set-Location -Path $args[0]
    Get-ChildItem -Path $args[0] -Filter *.epub |
        Foreach-Object -Parallel {
            pythonw $using:py $_.FullName
        } -ThrottleLimit 99999 -AsJob | Receive-Job -Wait
}
else {
    pythonw $py $args[0]
}
