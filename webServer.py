# tcp socket server
#encoding=utf-8
import socket
import multiprocessing

HTML_ROOT_DIR = "./"


def handle_cli(cli_socket):
    '''处理客户端请求 '''
    # 获取客户端请求数据
    request_data = cli_socket.recv(1024)
    #print(request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello python!"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data is:",response)
    
    # 向客户端返回响应数据
    cli_socket.send(bytes(response,"utf-8"))
    
    # 关闭客户端连接
    cli_socket.close()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',8878))
    server_socket.listen(128)

    while True:
        cli_socket, cli_address = server_socket.accept()
        print("[%s,%s]user has connected"%(cli_address[0],cli_address[1]))
        handle_client_process = multiprocessing.Process(target=handle_cli,args=(cli_socket,))
        handle_client_process.start()
        cli_socket.close()

'''
def fun(cli_socket):
    #接收数据
    request_data = recv()
    print(request_data)
    
    
    try:
        file = open( HTML_ROOT_DIR + "index.html")
        data = file.read()
        file.close()
    except IOError:
        HTTP1.1 404 Note Found \r\n
'''