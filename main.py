import requests
import json

# 百度AI API配置（已替换为你的密钥）
API_KEY = "geo371GJIU1xYvyZumnOaQ0N"
SECRET_KEY = "T4aIyHg275rAxej6fpEMTyA9Mpom6nQa"

# 获取access_token（调用API的临时凭证）
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET_KEY
    }
    response = requests.post(url, params=params)
    return response.json().get("access_token")

# 情感倾向分析
def sentiment_analysis(text):
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=" + get_access_token()
    payload = json.dumps({"text": text})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    result = response.json()
    if "items" in result:
        sentiment = result["items"][0]["sentiment"]  # 0:负向 1:中性 2:正向
        sentiment_label = {0: "消极", 1: "中性", 2: "积极"}[sentiment]
        return sentiment_label
    return "分析失败"

# 关键词提取
def keyword_extraction(text):
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword?access_token=" + get_access_token()
    payload = json.dumps({"text": text})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    result = response.json()
    if "items" in result:
        keywords = [item["word"] for item in result["items"]]
        return keywords
    return []

# 主函数：输入文本，输出分析结果
if __name__ == "__main__":
    print("📝 中文文本智能分析工具（基于百度AI）")
    text = input("请输入要分析的文本：")
    print("\n🔍 分析结果：")
    sentiment = sentiment_analysis(text)
    keywords = keyword_extraction(text)
    print(f"情感倾向：{sentiment}")
    print(f"提取关键词：{', '.join(keywords)}")