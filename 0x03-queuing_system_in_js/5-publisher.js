import { createClient } from "redis";

const publisher = createClient();

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

async function publishMessage(message, time) {
  setTimeout(async () => {
    console.log(`About to send ${message}`)
    await publisher.publish('holberton school channel', message);
  }, time);
}

publisher.connect()
 .then(() => {
  publishMessage("Holberton Student #1 starts course");
  publishMessage("Holberton Student #2 starts course");
  publishMessage("KILL_SERVER", 300);
  publishMessage("Holberton Student #3 starts course", 400);
 });
 