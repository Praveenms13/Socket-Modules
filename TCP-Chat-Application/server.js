const s = require("net");
const os = require("os");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Define server host and port
const interfaces = os.networkInterfaces();
const addresses = [];
for (let iface in interfaces) {
  interfaces[iface].forEach((info) => {
    if (info.family === "IPv4" && !info.internal) {
      addresses.push(info.address);
    }
  });
}
console.log(`IP Addresses: ${addresses}`);
const host = "127.0.1.1";
readline.question("Enter port number: ", (port) => {
  // Create client socket and connect to server
  const client_socket = s.createConnection({ host: host, port: port }, () => {
    console.log(`Connected to ${host}:${port}`);
  });

  // Continuously send messages to server
  readline.on("line", (input) => {
    // Send message to server
    client_socket.write(input);
  });

  // Close client socket
  client_socket.on("end", () => {
    console.log("Disconnected from server");
  });
});
