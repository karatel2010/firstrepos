import requests

# def get_info_by_ip(ip='127.0.0.1'):
#     try:
#         response=requests.get(url='http://ip-api.com/json/'+ip).json()
#         print(response)
#     except requests.exceptions.ConnectionError:
#         print('ok')
# def main():
#     ip=input('ip:')
#     get_info_by_ip(ip=ip)
#
# if __name__=='__main__':
#     main()
#
#

def get_info_by_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        # print(response)
        data = {
            "[IP]": response.get("query"),
            "[Int Prov]": response.get("isp"),
            "[Org]": response.get("org"),
            "[Country]": response.get("country"),
            "[Region name]": response.get("regionName"),
            "[City]": response.get("city"),
            "[ZIP]": response.get("zip"),
            "[Lat]": response.get("lat"),
            "[Long]": response.get("lon"),
        }

        for k,v in data.items():
            print(f"{k} : {v}")

        # area = folium.Map(location=[response.get("lat"), response.get("lon")])
        # area.save(f'{response.get("query")}_{response.get("country")}.html')
    except requests.exceptions.ConnectionError:
        print("Bad conntention. Check connection and try again.")

def main():
    ip = input("please enter a target IP: ")
    get_info_by_ip(ip)


if __name__ == "__main__":
    main()