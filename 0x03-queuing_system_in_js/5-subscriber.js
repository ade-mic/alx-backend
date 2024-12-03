import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
  console.log('Redis connected to the server')
});

subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

subscriber.connect()
 .then(() => {
    subscriber.subscribe('Hoberton school channel', (message) => {
      console.log(message)

      if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('Holberton school channel');
        subscriber.quit();
      }
    })
  });
