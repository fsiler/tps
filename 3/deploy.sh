templateFile="template.json"
paramFile="params.json"
#az group create \
#  --name myResourceGroupProd \
#  --location "West US"
az deployment group create --resource-group tpstest_group --template-file $templateFile --parameters $paramFile
