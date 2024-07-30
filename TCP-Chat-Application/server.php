<?php

$host = '0.0.0.0'; // gethostname();
$hostIP = gethostbyname($host);
$port = readline("Enter port number: ");

$server = socket_create(AF_INET, SOCK_STREAM, 0) or die("Failed to create socket");
socket_bind($server, $hostIP, $port) or die("Failed to bind to socket");
socket_listen($server);
echo "TCP Server Started\n";
echo "Waiting for a connection, Host IP: $hostIP, Listening on Port: $port\n";

while (true) {
    $conn = socket_accept($server);
    $addr = "";
    socket_getpeername($conn, $addr);
    echo "Connected by $addr[0]:$addr[1]\n";
    socket_write($conn, "Welcome to Praveen's Server (TCP Server)");
    echo "Waiting for Request Data...\n";
    while ($data = socket_read($conn, 1024)) {
        echo "Message From $addr[0]:$addr[1] => " . $data . "\n";
        // socket_write($conn, strtoupper($data)); // Send the data back to the client
    }
    socket_close($conn);
}

socket_close($server);
