import { createClient } from "redis";

async function nodeRedisStart() {
  try {
    const client = createClient();
    await client.connect();

    const hashSet = await client.hSet('HolbertonSchools', {
      'Portland': 50,
      'Seattle': 80,
      'New York': 20,
      'Bogota': 20,
      'Cali': 40,
      'Paris': 2,
    });
    console.log(hashSet);
    const res = await client.hGetAll('HolbertonSchools')
    console.log(res);
    await client.quit();
  } catch(e) {
    console.error(e);
  } 
}

nodeRedisStart();