import redis from 'redis'

const {createClient, print} = redis;

const client = createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Explicitly connect to Redis
client.connect().catch((err) => {
  console.error(`Failed to connect to Redis: ${err.message}`);
});

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // Use redis.print to log the confirmation
}

// Function to retrieve and log the value of a key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for key ${schoolName}: ${err.message}`);
      return;
    }
    console.log(reply); // Log the value of the key
  });
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
