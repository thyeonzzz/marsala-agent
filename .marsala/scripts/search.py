"""
Marsala 搜索引擎脚本 —— 连接到已有 Edge 浏览器搜索。
使用前请先手动启动 Edge: msedge --remote-debugging-port=9222
用法: python .reasonix/scripts/search.py <平台> <搜索词> [城市]
"""
import sys, time, os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import quote

DEBUG_PORT = 9222

DIANPING_CITIES = {
    "北京": 2, "上海": 1, "广州": 4, "深圳": 7,
    "杭州": 3, "成都": 8, "重庆": 9, "武汉": 6, "南京": 5, "苏州": 17,
    "西安": 10, "长沙": 15, "厦门": 26, "天津": 11, "青岛": 21,
    "郑州": 14, "大连": 19, "宁波": 18, "福州": 22, "合肥": 23,
    "无锡": 16, "东莞": 20, "佛山": 13, "沈阳": 12, "昆明": 34,
    "贵阳": 35, "南宁": 29, "海口": 42, "三亚": 43,
    "哈尔滨": 48, "长春": 46, "济南": 25, "太原": 31, "石家庄": 28,
    "兰州": 36, "乌鲁木齐": 50, "呼和浩特": 104, "银川": 45, "西宁": 27,
    "拉萨": 44, "南昌": 30, "温州": 33,
}

PLATFORMS = {
    "baidu":    ("https://www.baidu.com/s?wd={q}", False),
    "weibo":    ("https://s.weibo.com/weibo?q={q}", False),
    "xiaohongshu": ("https://www.xiaohongshu.com/search_result?keyword={q}", True),
    "dianping": ("dp", True),
    "douyin":   ("https://www.douyin.com/search/{q}", True),
}

def get_driver():
    opts = Options()
    opts.use_chromium = True
    opts.add_experimental_option("debuggerAddress", f"127.0.0.1:{DEBUG_PORT}")
    driver = webdriver.Edge(options=opts)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def main():
    platform = sys.argv[1] if len(sys.argv) > 1 else "baidu"
    query = sys.argv[2] if len(sys.argv) > 2 else input("搜索词: ")
    city = sys.argv[3] if len(sys.argv) > 3 else None
    
    if platform not in PLATFORMS:
        print(f"平台可选: {list(PLATFORMS.keys())}")
        return

    search_tpl, need_login = PLATFORMS[platform]

    if platform == "dianping":
        city_id = 7
        if city and city in DIANPING_CITIES:
            city_id = DIANPING_CITIES[city]
            print(f"大众点评城市: {city}")
        search_url = f"https://www.dianping.com/search/keyword/{city_id}/0_{quote(query)}"
    else:
        search_url = search_tpl.format(q=quote(query))

    try:
        driver = get_driver()
    except Exception as e:
        print(f"无法连接浏览器。请先手动启动 Edge：msedge --remote-debugging-port=9222")
        return

    if need_login:
        print(f"⏳ {platform} 需要登录态。如未登录请先在浏览器窗口中完成登录。")
        time.sleep(3)

    driver.get(search_url)
    print(f"搜索 {platform}: {query}")
    time.sleep(8)

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 600)")
        time.sleep(2)

    body = driver.find_element(By.TAG_NAME, "body")
    text = body.text
    print(f"\n=== {platform} ({len(text)} 字符) ===")
    skip_words = ["ICP", "营业执照", "隐私政策", "用户协议", "沪公网安", "行吟信息", "9501-3888", "© 2014", "地址：上海市"]
    lines = [l.strip() for l in text.split("\n") if l.strip() and len(l.strip()) > 10]
    useful = [l for l in lines if not any(w in l for w in skip_words)]
    for line in useful[:20]:
        print(f"  {line[:120]}")
    if not useful:
        print("  ⚠️ 未获取到有效内容（可能未登录，请在浏览器窗口中登录后重试）")

    print(f"\n浏览器保持打开，下一次搜索继续使用此窗口。")

if __name__ == "__main__":
    main()
