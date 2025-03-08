#Standard Library
import os
import re
import logging
import json

#Installed
import requests

import getpass


from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Default Logger
logging.basicConfig()
py_logger = logging.getLogger("pcpi")
py_logger.setLevel(10)

#Local
from .saas_session_manager import SaaSSessionManager
from .onprem_session_manager import CWPSessionManager

def __c_print(*args, **kwargs):
    '''
    Uses ascii codes to enable colored print statements. Works on Mac, Linux and Windows terminals
    '''

    #Magic that makes colors work on windows terminals
    os.system('')
    
    #Define Colors for more readable output
    c_gray = '\033[90m'
    c_red = '\033[91m'
    c_green = '\033[92m'
    c_yellow = '\033[93m'
    c_blue = '\033[94m'
    c_end = '\033[0m'

    color = c_end
    if 'color' in kwargs:
        c = kwargs['color'].lower()
        if c == 'gray' or c == 'grey':
            color = c_gray
        elif c ==  'red':
            color = c_red
        elif c == 'green':
            color = c_green
        elif c == 'yellow':
            color = c_yellow
        elif c == 'blue':
            color = c_blue
        else:
            color = c_end

    _end = '\n'
    if 'end' in kwargs:
        _end = kwargs['end']

    print(f'{color}', end='')
    for val in args:
        print(val, end='')
    print(f'{c_end}', end=_end)

#==============================================================================

def __validate_onprem_credentials(name, _url, uname, passwd, verify, proxies) -> bool:
    '''
    This function creates a session with the supplied credentials to test 
    if the user successfully entered valid credentials.
    '''

    headers = {
    'content-type': 'application/json; charset=UTF-8'
    }

    payload = {
        "username": uname,
        "password": passwd,
    }

    url = f'{_url}/api/v1/authenticate'

    try:
        __c_print('API - Validating credentials')
        res = requests.request("POST", url, headers=headers, json=payload, verify=verify, proxies=proxies)
        print(res.status_code)

        if res.status_code == 200:
            __c_print('SUCCESS', color='green')
            print()
            return True
        else:
            return False
    except:
        __c_print('ERROR', end=' ', color='red')
        print('Could not connect to Prisma Cloud API.')
        print()
        print('Steps to troubleshoot:')
        __c_print('1) Please disconnect from any incompatible VPN', color='blue')
        print()
        __c_print('2) Please ensure you have entered a valid Prisma Cloud URL.', color='blue')
        print()
        return False

def __validate_credentials(a_key, s_key, url, verify, proxies) -> bool:
    '''
    This function creates a session with the supplied credentials to test 
    if the user successfully entered valid credentials.
    '''

    headers = {
    'content-type': 'application/json; charset=UTF-8'
    }

    payload = {
        "username": f"{a_key}",
        "password": f"{s_key}"
    }

    try:
        __c_print('API - Validating credentials')
        response = requests.request("POST", f'{url}/login', headers=headers, json=payload, verify=verify, proxies=proxies)

        if response.status_code == 200:
            __c_print('SUCCESS', color='green')
            print()
            return True
        else:
            return False
    except:
        __c_print('ERROR', end=' ', color='red')
        print('Could not connect to Prisma Cloud API.')
        print()
        print('Steps to troubleshoot:')
        __c_print('1) Please disconnect from any incompatible VPN', color='blue')
        print()
        __c_print('2) Please ensure you have entered a valid Prisma Cloud URL.', color='blue')
        print('EX: https://app.prismacloud.io or https://app2.eu.prismacloud.io')
        print()
        return False

def __universal_validate_credentials(name, url, _id, secret, verify, proxies):
    if verify.lower() == 'true':
        verify = True
    else:
        verify = False
    if 'prismacloud.io' in url or 'prismacloud.cn' in url:
        return __validate_credentials(_id, secret, url, verify, proxies)
    else:
        return __validate_onprem_credentials(name, url, _id, secret, verify, proxies)

#==============================================================================

def __validate_url(url):
    if "prismacloud.io" not in (url):
        if 'https://' not in url and 'http://' not in url:
            url = 'https://' + url
        return url

    if len(url) >= 3:
        if 'https://' not in url:
            if url[:3] == 'app' or url[:3] == 'api':
                url = 'https://' + url
            
    url = url.replace('app', 'api')

    url = re.sub(r'prismacloud\.io\S*', 'prismacloud.io', url)

    return url

#==============================================================================

def __get_config():
    __c_print('Enter Prisma URL. (SaaS EX: https://app.ca.prismacloud.io, On-Prem EX: https://yourdomain.com):', color='blue')
    url = input()
    print()
    new_url = __validate_url(url)
    if new_url != url:
        __c_print('Adjusted URL:',color='yellow')
        print(new_url)
        print()

    __c_print('Enter identity (Access Key or Username):', color='blue')
    _id = input()
    print()

    __c_print('Enter secret (Secret Key or Password):', color='blue')
    secret = getpass.getpass(prompt='')
    print()

    __c_print('Certificate verification: (True/False/<path_to_.pem> file)', color='blue')
    __c_print('Leave blank to use default value (True).', color='yellow')
    verify = input()
    print()

    __c_print('Proxy section. HTTP first, HTTPS second. Leave blank to not use a proxy.', color='yellow')

    __c_print('Enter HTTP proxy address.', color='blue')
    __c_print('If you are not using a proxy, leave blank.', color='yellow')
    http_proxy = input()
    print()

    __c_print('Enter HTTPS proxy address.', color='blue')
    __c_print('If you are not using a proxy, leave blank.', color='yellow')
    https_proxy = input()
    print()
    
    proxies = None
    if http_proxy:
        proxies = {
            'http': http_proxy
        }
    if https_proxy:
        if proxies:
            proxies.update({'https': https_proxy})
        else:
            proxies = {
                'https': https_proxy
            }

    #If there is non-prisma URL, then ask if its a self hosted project
    project_flag = 'false'
    if 'prismacloud.io' not in new_url and 'prismacloud.cn' not in new_url:
        __c_print('CWP Project (True/False)', color='blue')
        __c_print('Leave blank to use default value (False).', color='yellow')
        project_flag = input()
        print()
        if project_flag.lower() == 'true':
            project_flag = 'true'
        else:
            project_flag = 'false'
    
    name = 'DEFAULT_NAME'
    if project_flag == 'true':
        __c_print('Enter project ID:', color='blue')
        name = input()
    else:
        __c_print('Enter tenant/console name (Optional):', color='blue')
        name = input()

    print()

    verify = verify.strip()

    if verify == '':
        verify = 'true'
    elif verify.lower() == 'true':
        verify = 'true'
    elif verify.lower() == 'false':
        verify = 'false'
    else:
        pass
    

    return name, _id, secret, new_url, verify, proxies, project_flag


def __build_config_json(name, _id, secret, url, verify, proxies, project_flag):
    session_dict = {
        'name': name,
        'url': url,
        'identity': _id,
        'secret': secret,
        'verify': verify,
        'proxies': proxies,
        'project_flag': project_flag
    }
    return session_dict

#==============================================================================

def __get_config_from_user(num_tenants, min_tenants):
        #Gets the source tenant credentials and ensures that are valid
    credentials = []

    if num_tenants != -1 and min_tenants == -1:
        for i in range(num_tenants):
            valid = False
            while not valid:
                __c_print('Enter Prisma Cloud Credentials', color='blue')
                print()
                name, _id, secret, url, verify, proxies, project_flag = __get_config()
                
                valid = __universal_validate_credentials(name, url, _id, secret, verify, proxies)
                if valid == False:
                    __c_print('FAILED', end=' ', color='red')
                    print('Invalid credentials. Please re-enter your credentials')
                    print()
                else:
                    credentials.append(__build_config_json(name, _id, secret, url, verify, proxies, project_flag))
    elif num_tenants == -1 and min_tenants != -1:
        tenant_count = 0
        while True:
            valid = False
            while not valid:
                __c_print('Enter Prisma Cloud Credentials', color='blue')
                print()
                name, _id, secret, url, verify, proxies, project_flag = __get_config()
                
                valid = __universal_validate_credentials(name, url, _id, secret, verify, proxies)
                if valid == False:
                    __c_print('FAILED', end=' ', color='red')
                    print('Invalid credentials. Please re-enter your credentials')
                    print()
                else:
                    credentials.append(__build_config_json(name, _id, secret, url, verify, proxies, project_flag))
                    tenant_count +=1
            
            if tenant_count >= min_tenants:
                __c_print('Would you like to add another Prisma Cloud credential? Y/N')
                choice = input().lower()
                if choice != 'yes' and choice != 'y':
                    break
    else:
        while True:
            valid = False
            while not valid:
                __c_print('Enter Prisma Cloud Credentials', color='blue')
                print()
                name, _id, secret, url, verify, proxies, project_flag = __get_config()
                
                valid = __universal_validate_credentials(name, url, _id, secret, verify, proxies)
                if valid == False:
                    __c_print('FAILED', end=' ', color='red')
                    print('Invalid credentials. Please re-enter your credentials')
                    print()
                else:
                    credentials.append(__build_config_json(name, _id, secret, url, verify, proxies, project_flag))
            
            __c_print('Would you like to add another Prisma Cloud credential? Y/N')
            choice = input().lower()

            if choice != 'yes' and choice != 'y':
                break

    return credentials

def load_config(file_path='', num_tenants=-1, min_tenants=-1, logger=py_logger):
    if num_tenants != -1 and min_tenants != -1:
        logger.error('ERROR: Incompatible options. Exiting...')
        # print('Incompatible Options. Exiting...')
        exit()

    if file_path == '':
        config_dir = os.path.join(os.environ['HOME'], '.prismacloud')
        config_path = os.path.join(config_dir, 'credentials.json')
        if not os.path.exists(config_dir):
            os.mkdir(config_dir)
    else:
        config_path = file_path

    tenant_sessions = []

    if not os.path.exists(config_path):
        config = __get_config_from_user(num_tenants, min_tenants)
        with open(config_path, 'w') as outfile:
            json.dump(config, outfile)

    config_data = {}
    with open(config_path, 'r') as infile:
        try:
            config_data = json.load(infile)
        except Exception as e:
            logger.error('Failed to load credentials file. Exiting...')
            logger.log(e)
            # print('Credential File Load Error. Exiting...')
            # print(e)
            exit()

    for blob in config_data:
        verify = blob['verify']
        if verify.lower().strip() == 'false':
            verify = False
        elif verify.lower().strip() == 'true':
            verify = True
        else:
            verify = verify

        proxies = None
        try:
            proxies = blob['proxies']
        except:
            pass    

        if 'prismacloud.io' in blob['url'] or 'prismacloud.cn' in blob['url']:
            tenant_sessions.append(SaaSSessionManager(blob['name'], blob['identity'], blob['secret'], blob['url'], verify, proxies, logger=logger))
        else:
            project_flag = False
            project_flag_in = blob.get('project_flag', None)
            if project_flag_in:
                if project_flag_in.lower().strip() == 'true':
                    project_flag = True

            tenant_sessions.append(CWPSessionManager(blob['name'], blob['url'], blob['identity'], blob['secret'], verify, proxies, project_flag, logger=logger))

    return tenant_sessions

def load_config_user(num_tenants=-1, min_tenants=-1, logger=py_logger):
    if num_tenants != -1 and min_tenants != -1:
        logger.error('ERROR: Incompatible options. Exiting...')
        # print('Incompatible cmd arguments. Exiting...')
        exit()

    config = __get_config_from_user(num_tenants, min_tenants)

    tenant_sessions = []

    for tenant in config:
        if 'prismacloud.io' in tenant['url'] or 'prismacloud.cn' in tenant['url']:
            tenant_sessions.append(SaaSSessionManager(tenant['name'], tenant['identity'], tenant['secret'], tenant['url'], tenant['verify'], logger=logger))
        else:
            project_flag = False
            project_flag_in = tenant.get('project_flag', None)
            if project_flag_in:
                if project_flag_in.lower().strip() == 'true':
                    project_flag = True
            tenant_sessions.append(CWPSessionManager(tenant['name'], tenant['url'], tenant['identity'], tenant['secret'], tenant['verify'], project_flag, logger=logger))

    return tenant_sessions

def load_config_env(prisma_name='PRISMA_PCPI_NAME', identifier_name='PRISMA_PCPI_ID', secret_name='PRISMA_PCPI_SECRET', api_url_name='PRISMA_PCPI_URL', verify_name='PRISMA_PCPI_VERIFY', http_name='PC_HTTP_PROXY', https_name='PC_HTTPS_PROXY', project_flag_name='PRISMA_PCPI_PROJECT_FLAG',  logger=py_logger):
    error_exit = False

    name = 'Tenant'
    try:
        name = os.environ[prisma_name]
    except:
        logger.warning(f'Missing \'{prisma_name}\' environment variable. Using default name.')
    
    api_url = ''
    api = None
    try:
        api_url = os.environ[api_url_name]
        api = __validate_url(api_url)
    except:
        logger.error(f'Missing \'{api_url_name}\' environment variable.')
        error_exit = True

    a_key = None
    try:
        a_key = os.environ[identifier_name]
    except:
        logger.error(f'Missing \'{identifier_name}\' environment variable.')
        error_exit = True

    s_key = None
    try:
        s_key = os.environ[secret_name]
    except:
        logger.error(f'Missing \'{secret_name}\' environment variable.')
        error_exit = True

    verify = True
    try:
        verify = os.environ[verify_name]
        if verify.lower() == 'false':
            verify = False
        if verify.lower() == 'true':
            verify = True
    except:
        logger.warning(f'\'{verify_name}\' not set. Using default value...')

    proxies = None
    http_proxy = None
    https_proxy = None
    try:
        http_proxy = os.environ[http_name]
    except:
        logger.warning(f'\'{http_name}\' not set. No HTTP proxy will be used.')

    try:
        https_proxy = os.environ[https_name]
    except:
        logger.warning(f'\'{https_name}\' not set. No HTTPS proxy will be used.')

    if http_proxy or https_proxy:
        proxies = {
            'http': http_proxy,
            'https': https_proxy
        }
    
    project_flag =  False
    try:
        project_flag = os.environ[project_flag_name]
        if project_flag.lower().strip() == 'true':
            project_flag = True
    except:
        logger.warning(f'\'{project_flag_name}\' not set. Using default value...')

    if error_exit:
        logger.info('Missing required environment variables. Exiting...')
        # print('Missing env variables. Exiting...')
        exit()

    if 'prismacloud.io' in api or 'prismacloud.cn' in api:
        return SaaSSessionManager(name, a_key, s_key, api, verify, proxies, logger=logger)
    else:
        return CWPSessionManager(name, api, a_key, s_key, verify, proxies, project_flag, logger=logger)


# def __build_cwp_session_dict(name, url, uname, passwd, verify, proxies):
#     session_dict = {
#         name: {
#             'url': url,
#             'uname': uname,
#             'passwd': passwd,
#             'verify': verify,
#             'proxies': proxies
#             }
#     }
#     return session_dict

# def __build_session_dict(name, a_key, s_key, url, verify, proxies):
#     session_dict = {
#         name: {
#             'access_key': a_key,
#             'secret_key': s_key,
#             'api_url': url,
#             'verify': verify,
#             'proxies': proxies
#             }
#     }
#     return session_dict

# def __get_tenant_credentials():

#     __c_print('Enter tenant name or any preferred identifier (optional):', color='blue')
#     name = input()

#     __c_print('Enter tenant url. (ex: https://app.ca.prismacloud.io):', color='blue')
#     url = input()
#     print()
#     new_url = __validate_url(url)
#     if new_url != url:
#         __c_print('Adjusted URL:',color='yellow')
#         print(new_url)
#         print()

#     __c_print('Enter tenant access key:', color='blue')
#     a_key = input()
#     print()

#     __c_print('Enter tenant secret key:', color='blue')
#     s_key = input()
#     print()

#     __c_print('Certificate verification: (True/False/<path to .pem file>)', color='blue')
#     __c_print('Leave blank to use default value.', color='yellow')
#     verify = input()
#     print()

#     __c_print('Proxy section. HTTP first, HTTPS second. Leave blank to not use a proxy.', color='blue')

#     __c_print('Enter HTTP proxy address.', color='blue')
#     __c_print('If you are not using a proxy, leave blank.', color='yellow')
#     http_proxy = input()
#     print()

#     __c_print('Enter HTTPS proxy address.', color='blue')
#     __c_print('If you are not using a proxy, leave blank.', color='yellow')
#     https_proxy = input()
#     print()
    
#     proxies = None
#     if http_proxy or https_proxy:
#         proxies = {
#             'http': http_proxy,
#             'https': https_proxy
#         }

#     if verify == '':
#         verify = True
#     elif verify.lower() == 'true':
#         verify = True
#     elif verify.lower() == 'false':
#         verify = False
#     else:
#         pass
    

#     return name, a_key, s_key, new_url, verify, proxies

#==============================================================================

# def __get_min_cwp_credentials_from_user(min_tenants):
#     credentials = []
#     tenants_added = 0

#     while True:
#         valid = False
#         while not valid:
#             __c_print('Enter credentials for the console', color='blue')
#             print()
#             name, url, uname, passwd, verify, proxies = __get_cwp_tenant_credentials()
            
#             valid = __validate_cwp_credentials(name, url, uname, passwd, verify, proxies)
#             if valid == False:
#                 __c_print('FAILED', end=' ', color='red')
#                 print('Invalid credentials. Please re-enter your credentials')
#                 print()
#             else:
#                 credentials.append(__build_cwp_session_dict(name, url, uname, passwd, verify, proxies))
#                 tenants_added += 1
        
#         if tenants_added >= min_tenants:
#             __c_print('Would you like to add an other tenant? Y/N')
#             choice = input().lower()

#             if choice != 'yes' and choice != 'y':
#                 break

#     return credentials

# def __get_cwp_credentials_from_user(num_tenants):
#     #Gets the source tenant credentials and ensures that are valid
#     credentials = []

#     if num_tenants != -1:
#         for i in range(num_tenants):
#             valid = False
#             while not valid:
#                 __c_print('Enter credentials for the console', color='blue')
#                 print()
#                 name, url, uname, passwd, verify, proxies = __get_cwp_tenant_credentials()
                
#                 valid = __validate_cwp_credentials(name, url, uname, passwd, verify, proxies)
#                 if valid == False:
#                     __c_print('FAILED', end=' ', color='red')
#                     print('Invalid credentials. Please re-enter your credentials')
#                     print()
#                 else:
#                     credentials.append(__build_cwp_session_dict(name, url, uname, passwd, verify, proxies))

#         return credentials
#     else:
#         while True:
#             valid = False
#             while not valid:
#                 __c_print('Enter credentials for the console', color='blue')
#                 print()
#                 name, url, uname, passwd, verify, proxies = __get_cwp_tenant_credentials()
                
#                 valid = __validate_cwp_credentials(name, url, uname, passwd, verify, proxies)
#                 if valid == False:
#                     __c_print('FAILED', end=' ', color='red')
#                     print('Invalid credentials. Please re-enter your credentials')
#                     print()
#                 else:
#                     credentials.append(__build_cwp_session_dict(name, url, uname, passwd, verify, proxies))
            
#             __c_print('Would you like to add an other tenant? Y/N')
#             choice = input().lower()

#             if choice != 'yes' and choice != 'y':
#                 break

#         return credentials


# def __get_min_credentials_from_user(min_tenants):
#     credentials = []
#     tenants_added = 0
#     while True:
#         valid = False
#         while not valid:
#             __c_print('Enter credentials for the tenant', color='blue')
#             print()
#             src_name, src_a_key, src_s_key, src_url, verify, proxies = __get_tenant_credentials()
            
#             valid = __validate_credentials(src_a_key, src_s_key, src_url, verify, proxies)
#             if valid == False:
#                 __c_print('FAILED', end=' ', color='red')
#                 print('Invalid credentials. Please re-enter your credentials')
#                 print()
#             else:
#                 credentials.append(__build_session_dict(src_name, src_a_key, src_s_key, src_url, verify, proxies))
#                 tenants_added += 1
        
#         if tenants_added >= min_tenants:
#             __c_print('Would you like to add an other tenant? Y/N')
#             choice = input().lower()

#             if choice != 'yes' and choice != 'y':
#                 break

#     return credentials

# def __get_cwp_tenant_credentials():

#     __c_print('Enter console name or any preferred identifier (optional):', color='blue')
#     name = input()

#     __c_print('Enter console base url with port number:', color='blue')
#     url = input()
#     print()

#     __c_print('Enter console username:', color='blue')
#     uname = input()
#     print()

#     __c_print('Enter console password:', color='blue')
#     passwd = input()
#     print()

#     __c_print('Certificate verification: (True/False/<path to .pem file>)', color='blue')
#     __c_print('Leave blank to use default value.', color='yellow')
#     verify = input()
#     print()

#     __c_print('Proxy section. HTTP first, HTTPS second. Leave blank to not use a proxy.', color='blue')

#     __c_print('Enter HTTP proxy address.', color='blue')
#     __c_print('If you are not using a proxy, leave blank.', color='yellow')
#     http_proxy = input()
#     print()

#     __c_print('Enter HTTPS proxy address.', color='blue')
#     __c_print('If you are not using a proxy, leave blank.', color='yellow')
#     https_proxy = input()
#     print()
    
#     proxies = None
#     if http_proxy or https_proxy:
#         proxies = {
#             'http': http_proxy,
#             'https': https_proxy
#         }

#     if verify == '':
#         verify = True
#     elif verify.lower() == 'true':
#         verify = True
#     elif verify.lower() == 'false':
#         verify = False
#     else:
#         pass

#     return name, url, uname, passwd, verify, proxies


# def __get_credentials_from_user(num_tenants):
#     #Gets the source tenant credentials and ensures that are valid
#     credentials = []

#     if num_tenants != -1:
#         for i in range(num_tenants):
#             valid = False
#             while not valid:
#                 __c_print('Enter credentials for the tenant', color='blue')
#                 print()
#                 src_name, src_a_key, src_s_key, src_url, verify, proxies = __get_tenant_credentials()
                
#                 valid = __validate_credentials(src_a_key, src_s_key, src_url, verify, proxies)
#                 if valid == False:
#                     __c_print('FAILED', end=' ', color='red')
#                     print('Invalid credentials. Please re-enter your credentials')
#                     print()
#                 else:
#                     credentials.append(__build_session_dict(src_name, src_a_key, src_s_key, src_url, verify, proxies))

#         return credentials
#     else:
#         while True:
#             valid = False
#             while not valid:
#                 __c_print('Enter credentials for the tenant', color='blue')
#                 print()
#                 src_name, src_a_key, src_s_key, src_url, verify, proxies = __get_tenant_credentials()
                
#                 valid = __validate_credentials(src_a_key, src_s_key, src_url, verify, proxies)
#                 if valid == False:
#                     __c_print('FAILED', end=' ', color='red')
#                     print('Invalid credentials. Please re-enter your credentials')
#                     print()
#                 else:
#                     credentials.append(__build_session_dict(src_name, src_a_key, src_s_key, src_url, verify, proxies))
            
#             __c_print('Would you like to add an other tenant? Y/N')
#             choice = input().lower()

#             if choice != 'yes' and choice != 'y':
#                 break

#         return credentials
    
# def __load_uuid_yaml(file_name, logger=py_logger):
#     with open(file_name, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     credentials = cfg['credentials']
#     entity_type = cfg['type']
#     uuid = cfg['uuid']
#     cmp_type = cfg['cmp_type']

#     tenant_sessions = []
#     for tenant in credentials:
#         tenant_name = ''
#         tenant_keys = tenant.keys()
#         for name in tenant_keys:
#             tenant_name = name     

#         a_key = tenant[tenant_name]['access_key']
#         s_key = tenant[tenant_name]['secret_key']
#         api_url = tenant[tenant_name]['api_url']

#         tenant_sessions.append(SaaSSessionManager(tenant_name, a_key, s_key, api_url, logger))

#     return tenant_sessions, entity_type, uuid, cmp_type

#==============================================================================

# def onprem_load_from_env(logger=py_logger) -> object:
#     error_exit = False

#     name = 'Console'
#     try:
#         name = os.environ['PC_CONSOLE_NAME']
#     except:
#         logger.warning('Missing \'PC_CONSOLE_NAME\' environment variable. Using default name.')
    
#     api_url = ''
#     api = None
#     try:
#         api_url = os.environ['PC_CONSOLE_URL']
#         api = __validate_url(api_url)
#     except:
#         logger.error('Missing \'PC_CONSOLE_URL\' environment variable.')
#         error_exit = True

#     uname = None
#     try:
#         uname = os.environ['PC_CONSOLE_USERNAME']
#     except:
#         logger.error('Missing \'PC_CONSOLE_USERNAME\' environment variable.')
#         error_exit = True

#     passwd = None
#     try:
#         passwd = os.environ['PC_CONSOLE_PASSWORD']
#     except:
#         logger.error('Missing \'PC_CONSOLE_PASSWORD\' environment variable.')
#         error_exit = True

#     verify = True
#     try:
#         verify = os.environ['PC_API_VERIFY']
#         if verify.lower() == 'false':
#             verify = False
#         if verify.lower() == 'true':
#             verify = True
#     except:
#         logger.warning('Missing \'PC_API_VERIFY\' environment variable. Using default value...')
    

#     if error_exit:
#         logger.info('Missing required environment variables. Exiting...')
#         # print('Missing Env Variables. Exiting...')
#         exit()

#     return CWPSessionManager(name, api_url, uname, passwd, verify, False, logger)

# #==============================================================================
# def onprem_load_min_from_file(min_tenants, file_path='console_credentials.yml', logger=py_logger):
#     '''
#     Reads console_credentials.yml or specified file path to load
#     self hosted CWP console credentials to create a session.
#     Returns a CWP session object.
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_min_cwp_credentials_from_user(min_tenants)
#         with open(file_path, 'w') as yml_file: 
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     cfg = {}
#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         uname = cfg[tenant]['uname']
#         passwd = cfg[tenant]['passwd']
#         api_url = cfg[tenant]['url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(CWPSessionManager(tenant, api_url, uname=uname, passwd=passwd, verify=verify, project_flag=False, logger=logger))

#     return tenant_sessions

# def onprem_load_multi_from_file(file_path='console_credentials.yml', logger=py_logger, num_tenants=-1) -> list:
#     '''
#     Reads console_credentials.yml or specified file path to load
#     self hosted CWP console credentials to create a session.
#     Returns a CWP session object.
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_cwp_credentials_from_user(num_tenants)
#         with open(file_path, 'w') as yml_file: 
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     cfg = {}
#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         uname = cfg[tenant]['uname']
#         passwd = cfg[tenant]['passwd']
#         api_url = cfg[tenant]['url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(CWPSessionManager(tenant, api_url, uname=uname, passwd=passwd, verify=verify, project_flag=False, logger=logger))


#     return tenant_sessions

# def onprem_load_from_file(file_path='console_credentials.yml', logger=py_logger) -> list:
#     '''
#     Reads console_credentials.yml or specified file path to load
#     self hosted CWP console credentials to create a session.
#     Returns a CWP session object.
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_cwp_credentials_from_user(1)
#         with open(file_path, 'w') as yml_file: 
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     cfg = {}
#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         uname = cfg[tenant]['uname']
#         passwd = cfg[tenant]['passwd']
#         api_url = cfg[tenant]['url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(CWPSessionManager(tenant, api_url, uname=uname, passwd=passwd, verify=verify, project_flag=False, logger=logger))

#     try:   
#         return tenant_sessions[0]
#     except:
#         logger.error('Error - No credentials found. Exiting...')
#         # print('Missing Credentials. Exiting...')
#         exit()

# def load_min_from_file(min_tenants, file_path='tenant_credentials.yml', logger=py_logger) -> list:
#     '''
#     Reads config.yml and generates a Session object for the tenant
#     Returns:
#     Tenant Session object
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_min_credentials_from_user(min_tenants)
#         with open(file_path, 'w') as yml_file:
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         a_key = cfg[tenant]['access_key']
#         s_key = cfg[tenant]['secret_key']
#         api_url = cfg[tenant]['api_url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(SaaSSessionManager(tenant, a_key, s_key, api_url, verify, logger))
       
#     return tenant_sessions

# def load_multi_from_file(file_path='tenant_credentials.yml', logger=py_logger, num_tenants=-1) -> list:
#     '''
#     Reads config.yml and generates a Session object for the tenant
#     Returns:
#     Tenant Session object
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_credentials_from_user(num_tenants)
#         with open(file_path, 'w') as yml_file:
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         a_key = cfg[tenant]['access_key']
#         s_key = cfg[tenant]['secret_key']
#         api_url = cfg[tenant]['api_url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(SaaSSessionManager(tenant, a_key, s_key, api_url, verify, logger))
       

#     return tenant_sessions

# def load_from_file(file_path='tenant_credentials.yml', logger=py_logger) -> list:
#     '''
#     Reads config.yml and generates a Session object for the tenant
#     Returns:
#     Tenant Session object
#     '''
#     #Open and load config file
#     if not os.path.exists(file_path):
#         #Create credentials yml file
#         __c_print('No credentials file found. Generating...', color='yellow')
#         print()
#         tenants = __get_credentials_from_user(1)
#         with open(file_path, 'w') as yml_file: 
#             for tenant in tenants:
#                 yaml.dump(tenant, yml_file, default_flow_style=False)

#     with open(file_path, "r") as file:
#         cfg = yaml.load(file, Loader=yaml.BaseLoader)

#     #Parse cfg for tenant names and create tokens for each tenant
#     tenant_sessions = []
#     for tenant in cfg:
#         a_key = cfg[tenant]['access_key']
#         s_key = cfg[tenant]['secret_key']
#         api_url = cfg[tenant]['api_url']
#         verify = True
#         try:
#             verify = cfg[tenant]['verify']
#             if verify.lower() == 'false':
#                 verify = False
#             if verify.lower() == 'true':
#                 verify = True
#         except:
#             pass

#         tenant_sessions.append(SaaSSessionManager(tenant, a_key, s_key, api_url, verify, logger))

#     try:   
#         return tenant_sessions[0]
#     except:
#         logger.error('Error - No credentials found. Exiting...')
#         # print('No Creds Found. Exiting...')
#         exit()

# def load_from_env(logger=py_logger) -> object:
#     error_exit = False

#     name = 'Tenant'
#     try:
#         name = os.environ['PC_TENANT_NAME']
#     except:
#         logger.warning('Missing \'PC_TENANT_NAME\' environment variable. Using default name.')
    
#     api_url = ''
#     api = None
#     try:
#         api_url = os.environ['PC_TENANT_API']
#         api = __validate_url(api_url)
#     except:
#         logger.error('Missing \'PC_TENANT_API\' environment variable.')
#         error_exit = True

#     a_key = None
#     try:
#         a_key = os.environ['PC_TENANT_A_KEY']
#     except:
#         logger.error('Missing \'PC_TENANT_A_KEY\' environment variable.')
#         error_exit = True

#     s_key = None
#     try:
#         s_key = os.environ['PC_TENANT_S_KEY']
#     except:
#         logger.error('Missing \'PC_TENANT_S_KEY\' environment variable.')
#         error_exit = True

#     verify = True
#     try:
#         verify = os.environ['PC_API_VERIFY']
#         if verify.lower() == 'false':
#             verify = False
#         if verify.lower() == 'true':
#             verify = True
#     except:
#         logger.warning('Missing \'PC_API_VERIFY\' environment variable. Using default value...')

#     if error_exit:
#         logger.info('Missing required environment variables. Exiting...')
#         # print('Missing Environment variables. Exiting...')
#         exit()

#     return SaaSSessionManager(name, a_key, s_key, api_url, verify, logger)

# def load_min_from_user(min_tenants, logger=py_logger):
#     tenant_sessions = []
#     tenants = __get_min_credentials_from_user(min_tenants)
#     for tenant in tenants:
#         for key in tenant:
#             name = key
#             verify = True
#             try:
#                 verify = tenant[name]['verify']
#                 if verify.lower() == 'false':
#                     verify = False
#                 if verify.lower() == 'true':
#                     verify = True
#             except:
#                 pass

#             tenant_sessions.append(SaaSSessionManager(name, tenant[name]['access_key'], tenant[name]['secret_key'], tenant[name]['api_url'], verify, logger))
            
#     return tenant_sessions

# def load_multi_from_user(logger=py_logger, num_tenants=-1) -> list:
#     tenant_sessions = []
#     tenants = __get_credentials_from_user(num_tenants)
#     for tenant in tenants:
#         for key in tenant:
#             name = key
#             verify = True
#             try:
#                 verify = tenant[name]['verify']
#                 if verify.lower() == 'false':
#                     verify = False
#                 if verify.lower() == 'true':
#                     verify = True
#             except:
#                 pass

#             tenant_sessions.append(SaaSSessionManager(name, tenant[name]['access_key'], tenant[name]['secret_key'], tenant[name]['api_url'], verify, logger))
            
#     return tenant_sessions

# def load_from_user(logger=py_logger) -> list:
#     tenant_sessions = []
#     tenants = __get_credentials_from_user(1)
#     for tenant in tenants:
#         for key in tenant:
#             name = key
#             verify = True
#             try:
#                 verify = tenant[name]['verify']
#                 if verify.lower() == 'false':
#                     verify = False
#                 if verify.lower() == 'true':
#                     verify = True
#             except:
#                 pass

#             tenant_sessions.append(SaaSSessionManager(name, tenant[name]['access_key'], tenant[name]['secret_key'], tenant[name]['api_url'], verify, logger))
            
#     return tenant_sessions[0]

