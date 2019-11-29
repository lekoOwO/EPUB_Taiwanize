Set-Location -Path $args[0]
Get-ChildItem "." -Filter *.epub |
Foreach-Object {
    pythonw $PSScriptRoot/main.py $_.FullName
}