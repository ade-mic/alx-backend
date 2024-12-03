import redis from 'redis'
import { promisify } from 'util'

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
  });
  if (callback) callback();
}

const getAsync = promisify(client.get).bind(client)

async function displaySchoolValue(schoolName, callback) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`)
  }
  if (callback) callback();
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
