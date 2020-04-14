
import asyncio # 将asyncio理解为协程池

from CxExtractor import CxExtractor,RunCxExtractor
cx = RunCxExtractor(threshold=186)
# html = cx.getHtml("http://www.bbc.com/news/world-europe-40885324")
# html = cx.getHtml("https://www.secpulse.com/archives/95634.html")
# content = cx.filter_tags(html)
# s = cx.getText(content)

loop = asyncio.get_event_loop()   # asyncip已经实现事件循环，只需要调用asyncio.get_event_loop()就可以完成select的操作
#get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))  # 等效未loop.create_task()
task = loop.create_task( cx.run("https://www.secpulse.com/archives/128005.html"))
loop.run_until_complete(task)
print(task.result())
# content = cx.filter_tags(task.result())
# s = cx.getText(content)

# task = loop.create_task(cx.getText(cx.filter_tags(task.result())))
# loop.run_until_complete(task)
# print(task.result())