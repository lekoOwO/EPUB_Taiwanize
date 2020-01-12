if ((Get-Item $args[0]) -is [System.IO.DirectoryInfo]) {
    Set-Location -Path $args[0]
    Get-ChildItem "." -Filter *.epub |
    Foreach-Object {
        pythonw $PSScriptRoot/main.py $_.FullName
    }
}
else {
    pythonw $PSScriptRoot/main.py $args[0]
}
