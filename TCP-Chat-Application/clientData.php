<?php
// Define server host and port
$host = '172.20.16.104'; // gethostname();
$hostIP = gethostbyname($host);
$port = readline("Enter port number: ");

// Create client socket and connect to server
$client_socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($client_socket, $host, $port) or die("Failed to connect to $host:$port");

// Get file path from user
$filePath = readline("Enter file path to send: ");
$fileName = basename($filePath);
$fileSize = filesize($filePath);

// send file path and name
socket_write($client_socket, $filePath, strlen($filePath));
socket_write($client_socket, "\n", strlen("\n"));

// send file data
$totalBytes = 0;
while ($totalBytes < $fileSize) {
    $data = fread(fopen($filePath, "rb"), 1024);
    socket_write($client_socket, $data, strlen($data));
    $totalBytes += strlen($data);
}

echo "File sent successfully: " . $filePath . "\n";

// receive response
$response = socket_read($client_socket, 1024);
echo "Server response: " . $response . "\n";

// Close client socket
socket_close($client_socket);
?>
