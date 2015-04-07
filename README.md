# Sockets-in-python
TCP proxy between sockets for communication between two clients.

Usage:

First, run python3 tcp_client_receive.py bind_ip bind_port
--> This will make the data receiving client to bind to 'bind_ip' ip address and port 'bind_port' and start listening for data.

Second, run python3 proxy.py proxy_ip proxy_port
--> This will make the proxy script wait for any incoming data and forward it to the ipaddress and port sent to it. So the proxy is binded to 'proxy_ip' ip address and port 'proxy_port'.

Third, run python3 tcp_client_send.py proxy_ip proxy_port dest_ip dest_port
--> This will connect to the proxy script with "proxy_ip" ip address and port "proxy_port" and send the destip and destport to the proxy script which will then connect to that destination and forward the data.

Example:

1.) python3 tcp_client_receive.py 127.0.0.1 4040    -- destination client starts listening

2.) python3 proxy.py 127.0.0.1 5050                 -- proxy started, starts listening

3.) python3 tcp_client_send.py 127.0.0.1 5050 127.0.0.1 4040  -- uses first two arguments as proxy, and last two arguments as destination.

(Anything sent from (3) will go to (2) and get forwarded to (1). So, At receiving client, the IP address and port is that of proxy.)
