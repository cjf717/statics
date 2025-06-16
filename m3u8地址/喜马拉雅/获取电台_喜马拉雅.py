# -*- coding: utf-8 -*-
# @Time    : 2023/10/16 11:00
# 电台节目信息：https://live.ximalaya.com/live-web/v1/getProgramSchedules?radioId=966&device=ios
# 电台信息：https://live.ximalaya.com/live-web/v1/radio?radioId=966
# 广东地区电台列表：https://mobile.ximalaya.com/radio-first-page-app/search?locationId=440000&locationTypeId=0&categoryId=0&pageNum=1&pageSize=48
# 网络台信息 url = "https://mobile.ximalaya.com/radio-first-page-app/search?locationId=0&locationTypeId=4&categoryId=0&pageNum=1&pageSize=48"
import requests
import os


class XimalayaRadio:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }

    def getInfos(self, url, file_name, play_types=["aac64"]):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            res = response.json()
            radios = res.get("data", {}).get("radios", [])
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return
        if not os.path.isdir(file_name):
            os.makedirs(file_name)
        for play_type in play_types:
            file = open(f"{file_name}/{file_name}_{play_type}.csv", "w", encoding="utf-8-sig")
            file.write("电台ID,电台名称,分类名称,播放地址\n")
            file_m3u = open(f"{file_name}/{file_name}_{play_type}.m3u8", "w", encoding="utf-8")
            file_m3u.write("#EXTM3U\n")
            for radio in radios:
                radio_id = radio.get("id")
                radio_name = radio.get("name")
                category_name = radio.get("categoryName", "")
                playUrl = radio.get("playUrl").get(play_type)
                # print(f"电台ID: {radio_id}, 电台名称: {radio_name}, 分类名称: {category_name}")
                file.write(f"{radio_id},{radio_name},{category_name},{playUrl}\n")
                file_m3u.write(f"#EXTINF:-1,{radio_name}\n")
                file_m3u.write(f"{playUrl}\n")
            file.close()
            file_m3u.close()


if __name__ == "__main__":
    play_types = ["aac24", "ts24", "aac64", "ts64"]
    ximalaya = XimalayaRadio()
    url_guangdong = "https://mobile.ximalaya.com/radio-first-page-app/search?locationId=440000&locationTypeId=0&categoryId=0&pageNum=1&pageSize=48"
    ximalaya.getInfos(url_guangdong, "广东地区电台_喜马拉雅", play_types)
    url_net = "https://mobile.ximalaya.com/radio-first-page-app/search?locationId=0&locationTypeId=4&categoryId=0&pageNum=1&pageSize=48"
    ximalaya.getInfos(url_net, "网络台_喜马拉雅", play_types)
