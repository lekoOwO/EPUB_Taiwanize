$json = Get-Content -Raw -Path config.json | ConvertFrom-Json

Write-Host "File Server running on: http://$($json.wsHost):$($json.wsPort)"
iex "waitress-serve --listen=$($json.wsHost):$($json.wsPort) file_server:app"