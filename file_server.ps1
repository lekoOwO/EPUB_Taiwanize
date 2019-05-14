$json = Get-Content -Raw -Path config.json | ConvertFrom-Json

Write-Host "File Server running on: http://$($json.apiHost):$($json.apiPort)"
iex "waitress-serve --listen=$($json.apiHost):$($json.apiPort) file_server:app"
