<?php

// Define server host and port
$host = '172.20.16.104'; // gethostname();
$hostIP = gethostbyname($host);
$port = readline("Enter port number: ");

// Create client socket and connect to server
$client_socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($client_socket, $host, $port) or die("Failed to connect to $host:$port");

// Continuously send messages to server
while (true) {
    // Get message input from user
    echo "Enter message: ";
    $message = trim(fgets(STDIN));

    // Send message to server
    socket_write($client_socket, $message, strlen($message));
}

// Close client socket
socket_close($client_socket);
