import cx_Oracle

#naybolsas_high = (description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.sa-saopaulo-1.oraclecloud.com))(connect_data=
# (service_name=ldn37zrk0zsh2ze_naybolsas_high.adwc.oraclecloud.com))(security=(ssl_server_cert_dn="CN=adb.sa-saopaulo-1.oraclecloud.com,OU=Oracle ADB SAOPAULO,O=Oracle Corporation,L=Redwood City,ST=California,C=US")))
def conecta():
    cx_Oracle.connect('ADMIN/Amx2208163442@naybolsas_high')
