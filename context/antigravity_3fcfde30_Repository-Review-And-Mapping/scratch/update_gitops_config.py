import json

target_file = r"e:\Work\dev-ops\vaults-gitops\stg\cci\scm\scm-web-mssql\configs\appsettings.json"

content = {
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "CommonConfig": {
    "VersionJS": "13",
    "CurrentTheme": "menu-on-top smart-style-3",
    "APIDebug": "true",
    "MaxSizeUpload": "29",
    "ClientName": "scm.concung.com",
    "ClientUrl": "https://scm-stg10.concung.vn/",
    "IndexName4Log": "scm",
    "TracingName": "scm",
    "IsUseElasticLogger": True,
    "Environment": "STG",
    "TrustedSSLCert": "true",
    "UploadFile": "E:\\\\UploadFile",
    "UploadFileFolderAPI": "E:\\\\UploadFile",
    "FileServingLink": "",
    "TimeOffLogin": "0-6",
    "isUseSeqLog": "false",
    "SeqURI": "http://log.concung.com:7777",
    "VaultIsEnable": "false",
    "VaultApi": "https://10.10.13.174:8200",
    "VaultSecret": "Coc_HRM_WEB_Sprint_Config",
    "VaultToken": "60fqiiEA6XR2SwokFz1i0CWk",
    "IsRedirectONL": "https://online-stg4.concung.vn/",
    "CRMKey": "8YG29YQ6tfV58GC4PYpG",
    "CRMSecretKey": "yX7EHnN47JS5WqW25WlBu33hf",
    "CRMservice": "https://smsservice.concung.com/",
    "ClearMemoryCacheCMD": "clearsubcache",
    "versionFont": "v1.0",
    "Oauth2ForWeb": {
      "OauthClientSecret": "61405A",
      "OauthClientScope": "scm-api",
      "OauthClientName": "scm.concung.com"
    }
  },
  "URLConnectionConfig": {
    "ApiUrl": "https://scm-api-stg4.concung.vn/",
    "MDMUrl": "https://mdm-api-stg.concung.vn/",
    "LuckyUrl": "https://sca-api5-uat.concung.vn/",
    "ACCUrl": "https://acc-api-stg4.concung.vn/",
    "SCAUrl": "https://sca-api-stg4.concung.vn/",
    "PromotionUrl": "https://promotion-api-uat.concung.vn/",
    "SOMUrl": "https://som-stg4.concung.vn/",
    "CDPUrl": "https://cdp-uat.concung.vn",
    "ApiSOMUrl": "https://som-api-stg4.concung.vn/",
    "ONLUrl": "https://online-api-stg4.concung.vn/",
    "ONLWebUrl": "https://online-stg4.concung.vn/",
    "MBMUrl": "https://mbm-stg4.concung.vn/",
    "PrintUrl": "https://print-api-uat.concung.vn/",
    "GCSApiUrl": "https://gcs-api-stg.concung.vn/",
    "WAPGCSApiUrl": "https://wap-gcs-api-stg.concung.vn/",
    "AdminApiUrl": "https://admin-api-stg4.concung.vn/",
    "EInvoiceApiUrl": "https://einvoice-api-uat.concung.vn/",
    "CDPApiUrl": "https://cdp-api-uat.concung.vn/",
    "FileHandlerUrl": "https://filehandler-api-stg.concung.vn/",
    "EvoucherPortalUrl": "https://evoucher-uat.concung.vn"
  }
}

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(content, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Successfully written to", target_file)
