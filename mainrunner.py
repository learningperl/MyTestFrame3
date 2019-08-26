# coding:utf8
from common.Excel import *
from common.mysql import Mysql
from interface.inter import *
from web.Web import Browser
from app.App import APP
from common import logger, config
from common.excelresult import Res
from common.mail import Mail
import inspect, datetime

"""
    这是整个自动化框架的主代码运行入口
    powered by will
    at: 2019/08/05
"""


def runcase(line, f):
    # # 使用条件语句，判断字符串，然后调用指定方法
    # if line[3] == 'post':
    #     http.post(line[4],line[5],line[6])
    #     return
    #
    # if line[3] == 'assertequals':
    #     http.assertequals(line[4],line[5])
    #     return

    # 分组信息，不用执行
    if len(line[0]) > 0 or len(line[1]) > 0:
        return

    # 反射获取关键字函数
    func = getattr(f, line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('args=') + 5:args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')
    # 不接收参数的调用
    if len(args) == 0:
        func()
        return

    if len(args) == 1:
        func(line[4])
        return

    if len(args) == 2:
        func(line[4], line[5])
        return

    if len(args) == 3:
        func(line[4], line[5], line[6])
        return

    print('warning：目前只支持3个参数的关键字')


# 接口自动化运行
reader = Reader()
casename = "HTTP接口用例"
reader.open_excel('./lib/' + casename + '.xls')
sheetname = reader.get_sheets()

# 读取配置文件
config.get_config('./lib/conf.properties')
logger.info(config.config)

# 数据库初始化
mysql = Mysql()
mysql.init_mysql('./lib/userinfo.sql')

writer = Writer()
writer.copy_open('./lib/' + casename + '.xls', './lib/result-' + casename + '.xls')

writer.set_sheet(sheetname[0])
writer.write(1, 3, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

reader.readline()
http = None
casetype = reader.readline()[1]
if casetype == 'HTTP':
    http = HTTP(writer)
if casetype == 'SOAP':
    http = SOAP(writer)
if casetype == 'WEB':
    http = Browser(writer)
if casetype == 'APP':
    http = APP(writer)

for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    # 保持读写在同一个sheet页面
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        writer.row = i
        line = reader.readline()
        print(line)
        runcase(line, http)

writer.set_sheet(sheetname[0])
writer.write(1, 4, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
writer.save_close()

# 解析结果，得到报告数据
res = Res()
r = res.get_res('./lib/result-' + casename + '.xls')
logger.info(r)

# 修改邮件数据
html = config.config['mailtxt']
html = html.replace('title', r['title'])
html = html.replace('runtype', r['runtype'])
html = html.replace('passrate', r['passrate'])
html = html.replace('status', r['status'])
if r['status'] == "Fail":
    html = html.replace('#00d800', 'red')
html = html.replace('casecount', r['casecount'])
html = html.replace('starttime', r['starttime'])
html = html.replace('endtime', r['endtime'])

# 发送邮件
mail = Mail()
mail.send(html)
