templateFile="template.json"
paramFile="params.json"

az deployment group create --resource-group tpstest_group --template-file $templateFile --parameters $paramFile
