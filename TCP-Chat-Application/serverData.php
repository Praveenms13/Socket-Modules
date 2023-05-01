<?php

// Define server host and port
$host = '0.0.0.0'; //gethostname();
$hostIP = gethostbyname($host);
$port = readline("Enter port number: ");

// Create server socket and bind to host and port
$server_socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($server_socket, $hostIP, $port) or die("Failed to bind to $hostIP:$port");
socket_listen($server_socket);

echo "TCP Server Started\n";
echo "Waiting for a connection, Host IP: $hostIP, Listening on Port: $port\n";

// Accept incoming connections
while (true) {
    $client_socket = socket_accept($server_socket);
    $client_address = '';
    socket_getpeername($client_socket, $client_address);
    echo "Connected by $client_address[0]:$client_address[1]\n";

    // Receive file path from client
    $filePath = socket_read($client_socket, 1024);
    $filePath = trim($filePath);
    echo "Receiving file $filePath from $client_address[0]:$client_address[1]\n";
    $fileName = basename($filePath);
    // Check if file exists
    if (file_exists($fileName)) {
        echo "File $fileName already exists, overwriting...\n";
    }

    // Open file for writing
    $file = fopen($fileName, "wb") or die("Failed to open file for writing");

    // Receive file data from client and write to file
    $buffer = "";
    while ($data = socket_read($client_socket, 1024)) {
        $buffer .= $data;
        if (strpos($data, "\n") !== false) {
            break;
        }
    }
    fwrite($file, $buffer);

    // Close file and socket
    fclose($file);
    socket_close($client_socket);
}

// Close server socket
socket_close($server_socket);
?>
