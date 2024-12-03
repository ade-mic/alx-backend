import redis from 'redis'

const {createClient, print} = redis;

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message()}`);
})

client.connect().catch((err) => {
  console.error(`Failed to connect to Redis: ${err.message}`);
});


function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(`Error setting key "${schoolName}": ${err.message}`);
      return;
    }
    console.log(reply)
    if (callback) callback();
  });
}

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error retrieving "${schoolName}": ${err.message}`)
    }
    console.log(reply);
    if (callback) callback();
  })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
