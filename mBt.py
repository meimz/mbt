#coding: utf-8
# +-------------------------------------------------------------------
# | 宝塔Linux面板
# +-------------------------------------------------------------------
# | Copyright (c) 2015-2099 宝塔软件(http://bt.cn) All rights reserved.
# +-------------------------------------------------------------------
# | 感谢: 黄文良 <2879625666@qq.com> && Youngxj
# +-------------------------------------------------------------------
# +-------------------------------------------------------------------
# | Author: 葱先生 zh-lei@foxmail.com
# +-------------------------------------------------------------------
# +-------------------------------------------------------------------
# | 使用方式参考 https://www.bt.cn/bbs/thread-23895-1-1.html
# +-------------------------------------------------------------------

import time,hashlib,sys,os,json
class mBt:
    __BT_KEY = '秘钥'
    __BT_PANEL = '地址'

    #如果希望多台面板，可以在实例化对象时，将面板地址与密钥传入
    def __init__(self,bt_panel = None,bt_key = None):
        if bt_panel:
            self.__BT_PANEL = bt_panel
            self.__BT_KEY = bt_key

    #取面板日志
    def get_logs(self,table='logs',limit=10,tojs='test'):
        url = self.__BT_PANEL + '/data?action=getData'
        p_data = {}
        p_data['table'] = table
        p_data['limit'] = limit
        p_data['tojs'] = tojs
        return self._getData(url, p_data)

    def _getData(self,url,data={}):
        p_data = self.__get_key_data()  # 取签名
        for (k,v) in data.items():
            p_data[k]=v
        result = self.__http_post_cookie(url, p_data)
        # 解析JSON数据
        return json.loads(result)
    # 获取系统基础统计
    def GetSystemTotal(self):
        url = self.__BT_PANEL + '/system?action=GetSystemTotal'
        p_data={}
        return self._getData(url, p_data)

    # 获取磁盘分区信息
    def GetDiskInfo(self):
        url = self.__BT_PANEL + '/system?action=GetDiskInfo'
        p_data={}
        return self._getData(url, p_data)

    # 获取实时状态信息(CPU、内存、网络、负载)
    def GetNetWork(self):
        url = self.__BT_PANEL + '/system?action=GetNetWork'
        p_data={}
        return self._getData(url, p_data)

    # 检查是否有安装任务
    def GetTaskCount(self):
        url = self.__BT_PANEL + '/ajax?action=GetTaskCount'
        p_data={}
        return self._getData(url, p_data)

    # 检查面板更新
    def UpdatePanel(self):
        url = self.__BT_PANEL + '/ajax?action=UpdatePanel'
        p_data={}
        return self._getData(url, p_data)

    # 获取网站列表
    def Websites(self, search='', page='1', limit='15', type='-1', order='id desc', tojs=''):
        url = self.__BT_PANEL + '/data?action=getData&table=sites'
        p_data={}
        p_data['p'] = page;
        p_data['limit'] = limit;
        p_data['type'] = type;
        p_data['order'] = order;
        p_data['tojs'] = tojs;
        p_data['search'] = search;
        return self._getData(url, p_data)

    # 获取网站分类
    def Webtypes(self):
        url = self.__BT_PANEL + '/site?action=get_site_types'
        p_data={}
        return self._getData(url, p_data)

    # 获取已安装的PHP版本列表
    def GetPHPVersion(self):
        url = self.__BT_PANEL + '/site?action=GetPHPVersion'
        p_data={}
        return self._getData(url, p_data)

    # 获取指定网站运行的PHP版本
    def GetSitePHPVersion(self):
        url = self.__BT_PANEL + '/site?action=GetSitePHPVersion'
        p_data={}
        return self._getData(url, p_data)

    # 修改指定网站的PHP版本
    def SetPHPVersion(self):
        url = self.__BT_PANEL + '/site?action=SetPHPVersion'
        p_data={}
        return self._getData(url, p_data)

    # 开启并设置网站密码访问
    def SetHasPwd(self,id,username,password):
        url = self.__BT_PANEL + '/site?action=SetHasPwd'
        p_data={}
        p_data['id'] = id;
        p_data['username'] = username;
        p_data['password'] = password;
        return self._getData(url, p_data)

    # 关闭网站密码访问
    def CloseHasPwd(self,id):
        url = self.__BT_PANEL + '/site?action=CloseHasPwd'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 获取网站几项开关（防跨站、日志、密码访问）
    def GetDirUserINI(self,id,path):
        url = self.__BT_PANEL + '/site?action=GetDirUserINI'
        p_data={}
        p_data['id'] = id;
        p_data['path'] = path;
        return self._getData(url, p_data)

    # 新增网站 webname 网站域名 json 格式 path 网站路径 type_id 网站分类ID type 网站类型 version PHP版本 port 网站端口 ps 网站备注 ftp 网站是否开通FTP ftp_username FTP用户名 ftp_password FTP密码 sql 网站是否开通数据库 codeing 数据库编码类型 utf8|utf8mb4|gbk|big5 datauser 数据库账号 datapassword 数据库密码	 */

    def WebAddSite(self,webname,path,type_id,type,version,port,ps,ftp,ftp_username,ftp_password,sql,codeing,datauser,datapassword):
        url = self.__BT_PANEL + '/site?action=AddSite'
        p_data={}
        p_data['webname'] = webname;
        p_data['path'] = path;
        p_data['type_id'] = type_id;
        p_data['type'] = type;
        p_data['version'] = version;
        p_data['port'] = port;
        p_data['ps'] = ps;
        p_data['ftp'] = ftp;
        p_data['ftp_username'] = ftp_username;
        p_data['ftp_password'] = ftp_password;
        p_data['sql'] = sql;
        p_data['codeing'] = codeing;
        p_data['datauser'] = datauser;
        p_data['datapassword'] = datapassword;
        return self._getData(url, p_data)

    # 删除网站
    def WebDeleteSite(self,id,webname,ftp,database,path):
        url = self.__BT_PANEL + '/site?action=DeleteSite'
        p_data={}
        p_data['id'] = id;
        p_data['webname'] = webname;
        p_data['ftp'] = ftp;
        p_data['database'] = database;
        p_data['path'] = path;
        return self._getData(url, p_data)

    # 停用网站
    def WebSiteStop(self,id,webname):
        url = self.__BT_PANEL + '/site?action=SiteStop'
        p_data={}
        p_data['id'] = id;
        p_data['webname'] = webname;
        return self._getData(url, p_data)

    # 启用网站
    def WebSiteStart(self,id,webname):
        url = self.__BT_PANEL + '/site?action=SiteStart'
        p_data={}
        p_data['id'] = id;
        p_data['webname'] = webname;
        return self._getData(url, p_data)

    # 设置网站有效期 edate 网站到期时间 格式：2019-01-01，永久：0000-00-00
    def WebSetEdate(self,id,edate):
        url = self.__BT_PANEL + '/site?action=SetEdate'
        p_data={}
        p_data['id'] = id;
        p_data['edate'] = edate;
        return self._getData(url, p_data)

    # 修改网站备注
    def WebSetPs(self,id,ps):
        url = self.__BT_PANEL + '/data?action=setPs&table=sites'
        p_data={}
        p_data['id'] = id;
        p_data['ps'] = ps;
        return self._getData(url, p_data)

    # 获取网站备份列表
    def WebBackupList(self,id,page='1',limit='5',type='0',tojs=''):
        url = self.__BT_PANEL + '/data?action=getData&table=backup'
        p_data={}
        p_data['p'] = page;
        p_data['limit'] = limit;
        p_data['type'] = type;
        p_data['tojs'] = tojs;
        p_data['search'] = id;
        return self._getData(url, p_data)

    # 创建网站备份
    def WebToBackup(self,id):
        url = self.__BT_PANEL + '/site?action=ToBackup'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 删除网站备份
    def WebDelBackup(self,id):
        url = self.__BT_PANEL + '/site?action=DelBackup'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 获取网站域名列表
    def WebDoaminList(self,id,list=True):
        url = self.__BT_PANEL + '/data?action=getData&table=domain'
        p_data={}
        p_data['search'] = id;
        p_data['list'] = list;
        return self._getData(url, p_data)

    # 获取网站域名绑定二级目录信息
    def GetDirBinding(self,id):
        url = self.__BT_PANEL + '/site?action=GetDirBinding'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 添加网站子目录域名
    def AddDirBinding(self,id,domain,dirName):
        url = self.__BT_PANEL + '/site?action=AddDirBinding'
        p_data={}
        p_data['id'] = id;
        p_data['domain'] = domain;
        p_data['dirName'] = dirName;
        return self._getData(url, p_data)

    # 删除网站绑定子目录
    def DelDirBinding(self,dirid):
        url = self.__BT_PANEL + '/site?action=DelDirBinding'
        p_data={}
        p_data['id'] = dirid;
        return self._getData(url, p_data)

    # 获取网站子目录伪静态规则
    def GetDirRewrite(self,dirid,type=0):
        url = self.__BT_PANEL + '/site?action=GetDirRewrite'
        p_data={}
        p_data['id'] = dirid;
        if type!=0:
            p_data['add'] = 1;

        return self._getData(url, p_data)

    # 添加网站域名
    def WebAddDomain(self):
        url = self.__BT_PANEL + '/site?action=AddDomain'
        p_data={}
        return self._getData(url, p_data)

    # 删除网站域名
    def WebDelDomain(self):
        url = self.__BT_PANEL + '/site?action=DelDomain'
        p_data={}
        return self._getData(url, p_data)

    # 获取网站日志
    def GetSiteLogs(self,site):
        url = self.__BT_PANEL + '/site?action=GetSiteLogs'
        p_data={}
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 获取网站盗链状态及规则信息
    def GetSecurity(self,id,site):
        url = self.__BT_PANEL + '/site?action=GetSecurity'
        p_data={}
        p_data['id'] = id;
        p_data['name'] = site;
        return self._getData(url, p_data)

    # 设置网站盗链状态及规则信息
    def SetSecurity(self,id,site,fix,domains,status):
        url = self.__BT_PANEL + '/site?action=SetSecurity'
        p_data={}
        p_data['id'] = id;
        p_data['name'] = site;
        p_data['fix'] = fix;
        p_data['domains'] = domains;
        p_data['status'] = status;
        return self._getData(url, p_data)

    # 获取SSL状态及证书详情
    def GetSSL(self,site):
        url = self.__BT_PANEL + '/site?action=GetSSL'
        p_data={}
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 强制HTTPS
    def HttpToHttps(self,site):
        url = self.__BT_PANEL + '/site?action=HttpToHttps'
        p_data={}
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 关闭强制HTTPS
    def CloseToHttps(self,site):
        url = self.__BT_PANEL + '/site?action=CloseToHttps'
        p_data={}
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 设置SSL证书
    def SetSSL(self,type,site,key,csr):
        url = self.__BT_PANEL + '/site?action=SetSSL'
        p_data={}
        p_data['type'] = type;
        p_data['siteName'] = site;
        p_data['key'] = key;
        p_data['csr'] = csr;
        return self._getData(url, p_data)

    # 关闭SSL
    def CloseSSLConf(self,updateOf,site):
        url = self.__BT_PANEL + '/site?action=CloseSSLConf'
        p_data={}
        p_data['updateOf'] = updateOf;
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 获取网站默认文件
    def WebGetIndex(self,id):
        url = self.__BT_PANEL + '/site?action=GetIndex'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 设置网站默认文件
    def WebSetIndex(self,id,index):
        url = self.__BT_PANEL + '/site?action=SetIndex'
        p_data={}
        p_data['id'] = id;
        p_data['Index'] = index;
        return self._getData(url, p_data)

    # 获取网站流量限制信息
    def GetLimitNet(self,id):
        url = self.__BT_PANEL + '/site?action=GetLimitNet'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 设置网站流量限制信息
    def SetLimitNet(self,id,perserver,perip,limit_rate):
        url = self.__BT_PANEL + '/site?action=SetLimitNet'
        p_data={}
        p_data['id'] = id;
        p_data['perserver'] = perserver;
        p_data['perip'] = perip;
        p_data['limit_rate'] = limit_rate;
        return self._getData(url, p_data)

    # 关闭网站流量限制
    def CloseLimitNet(self,id):
        url = self.__BT_PANEL + '/site?action=CloseLimitNet'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 获取网站301重定向信息
    def Get301Status(self,site):
        url = self.__BT_PANEL + '/site?action=Get301Status'
        p_data={}
        p_data['siteName'] = site;
        return self._getData(url, p_data)

    # 设置网站301重定向信息
    def Set301Status(self,site,toDomain,srcDomain,type):
        url = self.__BT_PANEL + '/site?action=Set301Status'
        p_data={}
        p_data['siteName'] = site;
        p_data['toDomain'] = toDomain;
        p_data['srcDomain'] = srcDomain;
        p_data['type'] = type;
        return self._getData(url, p_data)

    # 获取可选的预定义伪静态列表
    def GetRewriteList(self,site):
        url = self.__BT_PANEL + '/site?action=GetRewriteList'
        p_data={}
        p_data['sitename'] = site;
        return self._getData(url, p_data)

    # 获取指定预定义伪静态规则内容(获取文件内容)
    def GetFileBody(self,path,type=0):
        url = self.__BT_PANEL + '/files?action=GetFileBody'
        p_data={}
        if type!=0:
            path_dir ='vhost/rewrite'
        else:
            path_dir ='rewrite/nginx'
        p_data['path'] = '/www/server/panel/'+path_dir+'/'+path+'.conf';
        return self._getData(url, p_data)

    # 保存伪静态规则内容(保存文件内容)
    def SaveFileBody(self,path,data,encoding='utf-8',type=0):
        url = self.__BT_PANEL + '/files?action=SaveFileBody'
        p_data={}
        if type!=0:
            path_dir = '/www/server/panel/vhost/rewrite/'+path+'.conf';
        else:
            path_dir = path;
        p_data['path'] = path_dir;
        p_data['data'] = data;
        p_data['encoding'] = encoding;
        return self._getData(url, p_data)

    # 获取网站反代信息及状态
    def GetProxyList(self):
        url = self.__BT_PANEL + '/site?action=GetProxyList'
        p_data={}
        return self._getData(url, p_data)

    # 添加网站反代信息
    def CreateProxy(self,cache,proxyname,cachetime,proxydir,proxysite,todomain,advanced,sitename,subfilter,type):
        url = self.__BT_PANEL + '/site?action=CreateProxy'
        p_data={}
        p_data['cache'] = cache;
        p_data['proxyname'] = proxyname;
        p_data['cachetime'] = cachetime;
        p_data['proxydir'] = proxydir;
        p_data['proxysite'] = proxysite;
        p_data['todomain'] = todomain;
        p_data['advanced'] = advanced;
        p_data['sitename'] = sitename;
        p_data['subfilter'] = subfilter;
        p_data['type'] = type;
        return self._getData(url, p_data)

    # 修改网站反代信息
    def ModifyProxy(self,cache,proxyname,cachetime,proxydir,proxysite,todomain,advanced,sitename,subfilter,type):
        url = self.__BT_PANEL + '/site?action=ModifyProxy'
        p_data={}
        p_data['cache'] = cache;
        p_data['proxyname'] = proxyname;
        p_data['cachetime'] = cachetime;
        p_data['proxydir'] = proxydir;
        p_data['proxysite'] = proxysite;
        p_data['todomain'] = todomain;
        p_data['advanced'] = advanced;
        p_data['sitename'] = sitename;
        p_data['subfilter'] = subfilter;
        p_data['type'] = type;
        return self._getData(url, p_data)

    # 获取FTP信息列表
    def WebFtpList(self, search='', page='1', limit='15', type='-1', order='id desc', tojs=''):
        url = self.__BT_PANEL + '/data?action=getData&table=ftps'
        p_data={}
        p_data['p'] = page;
        p_data['limit'] = limit;
        p_data['type'] = type;
        p_data['order'] = order;
        p_data['tojs'] = tojs;
        p_data['search'] = search;
        return self._getData(url, p_data)

    # 修改FTP账号密码
    def SetUserPassword(self,id,ftp_username,new_password):
        url = self.__BT_PANEL + '/ftp?action=SetUserPassword'
        p_data={}
        p_data['id'] = id;
        p_data['ftp_username'] = ftp_username;
        p_data['new_password'] = new_password;
        return self._getData(url, p_data)

    # 启用/禁用FTP
    def SetStatus(self,id,username,status):
        url = self.__BT_PANEL + '/ftp?action=SetStatus'
        p_data={}
        p_data['id'] = id;
        p_data['username'] = username;
        p_data['status'] = status;
        return self._getData(url, p_data)

    # 获取SQL信息列表
    def WebSqlList(self, search='', page='1', limit='15', type='-1', order='id desc', tojs=''):
        url = self.__BT_PANEL + '/data?action=getData&table=databases'
        p_data={}
        p_data['p'] = page;
        p_data['limit'] = limit;
        p_data['type'] = type;
        p_data['order'] = order;
        p_data['tojs'] = tojs;
        p_data['search'] = search;
        return self._getData(url, p_data)

    # 修改SQL账号密码
    def ResDatabasePass(self,id,name,password):
        url = self.__BT_PANEL + '/database?action=ResDatabasePassword'
        p_data={}
        p_data['id'] = id;
        p_data['name'] = name;
        p_data['password'] = password;
        return self._getData(url, p_data)

    # 创建sql备份
    def SQLToBackup(self,id):
        url = self.__BT_PANEL + '/database?action=ToBackup'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 删除sql备份
    def SQLDelBackup(self,id):
        url = self.__BT_PANEL + '/database?action=DelBackup'
        p_data={}
        p_data['id'] = id;
        return self._getData(url, p_data)

    # 下载备份文件(目前暂停使用)
    def download(self):
        url = self.__BT_PANEL + '/download?filename='
        p_data={}
        return self._getData(url, p_data)

    # 宝塔一键部署列表
    def deployment(self,search=''):
        url = self.__BT_PANEL + '/plugin?action=a&name=deployment&s=GetList&type=0'
        p_data={}
        p_data['search'] =search
        return self._getData(url, p_data)

    # 部署任务
    def SetupPackage(self,dname,site_name,php_version):
        url = self.__BT_PANEL + '/plugin?action=a&name=deployment&s=SetupPackage'
        p_data={}
        p_data['dname'] = dname;
        p_data['site_name'] = site_name;
        p_data['php_version'] = php_version;
        return self._getData(url, p_data)




    #计算MD5
    def __get_md5(self,s):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()

    #构造带有签名的关联数组
    def __get_key_data(self):
        now_time = int(time.time())
        p_data = {'request_token':self.__get_md5(str(now_time) + '' + self.__get_md5(self.__BT_KEY)), 'request_time':now_time}
        return p_data


    #发送POST请求并保存Cookie
    #@url 被请求的URL地址(必需)
    #@data POST参数，可以是字符串或字典(必需)
    #@timeout 超时时间默认1800秒
    #return string
    def __http_post_cookie(self,url,p_data,timeout=1800):
        cookie_file = './' + self.__get_md5(self.__BT_PANEL) + '.cookie';
        if sys.version_info[0] == 2:
            #Python2
            import urllib,urllib2,ssl,cookielib

            #创建cookie对象
            cookie_obj = cookielib.MozillaCookieJar(cookie_file)

            #加载已保存的cookie
            if os.path.exists(cookie_file):cookie_obj.load(cookie_file,ignore_discard=True,ignore_expires=True)

            ssl._create_default_https_context = ssl._create_unverified_context

            data = urllib.urlencode(p_data)
            req = urllib2.Request(url, data)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_obj))
            response = opener.open(req,timeout=timeout)

            #保存cookie
            cookie_obj.save(ignore_discard=True, ignore_expires=True)
            return response.read()
        else:
            #Python3
            import urllib.request,ssl,http.cookiejar
            cookie_obj = http.cookiejar.MozillaCookieJar(cookie_file)
            cookie_obj.load(cookie_file,ignore_discard=True,ignore_expires=True)
            handler = urllib.request.HTTPCookieProcessor(cookie_obj)
            data = urllib.parse.urlencode(p_data).encode('utf-8')
            req = urllib.request.Request(url, data)
            opener = urllib.request.build_opener(handler)
            response = opener.open(req,timeout = timeout)
            cookie_obj.save(ignore_discard=True, ignore_expires=True)
            result = response.read()
            if type(result) == bytes: result = result.decode('utf-8')
            return result


if __name__ == '__main__':
    #实例化宝塔API对象
    my_api = mBt()

    #调用get_logs方法
    r_data = my_api.GetNetWork()
    #打印响应数据
    print(r_data)